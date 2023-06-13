from reportlab.platypus import SimpleDocTemplate, Paragraph, PageBreak, Spacer, Table, Image, TopPadder
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen.canvas import Canvas

from PIL import Image as pilImage

from datetime import datetime

import io

styles = getSampleStyleSheet()

class BaseReport:
    """
    Base class for generating reports in PyBeam QA
    """
    def __init__(self, filename: str, report_name: str):
        self._filename = filename
        self.report_name = report_name

    def setReportName(self, report_name: str):
        self.report_name = report_name
    
    def titlePage(self, canvas: Canvas, document):
        canvas.setAuthor(self._author)
        canvas.setCreator("PyBeam QA")
        canvas.setTitle(self.report_name)
        canvas.setSubject("Radiotherapy QA")

        canvas.saveState()
        canvas.setFont("Helvetica-Bold", 20)
        canvas.drawCentredString(A4[0]/2.0, 26.0 * cm , self.report_name)
        canvas.restoreState()

class WinstonLutzReport(BaseReport):
    """
    Class for generating Winston-Lutz reports
    """
    def __init__(
        self, filename: str,
        report_name: str = "Winston-Lutz Analysis Report",
        author: str = "N/A",
        institution: str = "N/A",
        treatment_unit_name: str = None,
        analysis_summary: dict = None,
        patient_info: dict = None,
        summary_plot: io.BytesIO = None,
        report_status: str = "N/A",
        tolerance: float = 1.00,
        comments: str | None = None
        ):
        super().__init__(filename, report_name)

        self._author = author
        self._institution = institution
        self._treatment_unit_name = treatment_unit_name
        self._analysis_summary = analysis_summary
        self._patient_info = patient_info
        self._summary_plot = summary_plot
        self._report_status = report_status
        self._tolerance = tolerance
        self._comments = comments

        self.default_style = styles["Normal"]

    def userDetails(self, doc_contents: list):
        data = [[Paragraph("<b>Physicist</b>"), f": {self._author}"],
                [Paragraph("<b>Institution</b>"), f": {self._institution}"],
                [Paragraph("<b>Treatment Unit</b>"), f": {self._treatment_unit_name}"],
                [Paragraph("<b>Analysis Date</b>"), f": {datetime.today().strftime('%d %B %Y')}"],
                [Paragraph("<b>Test Tolerance</b>"), f": {self._tolerance} mm"],
                [Paragraph("<b>Test Outcome</b>"), f": {self._report_status}"]]
        
        if self._patient_info is not None:
            data.append(["",""])
            data.append([Paragraph("<b>Patient Name</b>"), f": {self._patient_info['patient_name']}"])
            data.append([Paragraph("<b>Patient ID</b>"), f": {self._patient_info['patient_id']}"])
        
        doc_contents.append(Table(data, colWidths=[3.5*cm, 5.0*cm], hAlign="LEFT"))

    def analysisDetails(self, doc_contents: list):
        doc_contents.append(Spacer(1, 16)) # add spacing of 8 pts
        doc_contents.append(Paragraph("<b><u><font size=11 color=\"darkblue\">Analysis Details:</font></u></b>"))
        doc_contents.append(Spacer(1, 16)) # add spacing of 16 pts

        data = [[param, value] for param, value in self._analysis_summary.items()]
        data.insert(0, [Paragraph("<b>Parameter</b>"), Paragraph("<b>Value</b>")])

        table = Table(data, colWidths=[8.0*cm, 3.5*cm], hAlign="LEFT",
                      style=[('GRID', (0,0), (-1,-1), 0.5, colors.grey),
                             ('BACKGROUND', (0,0), (-1,0), colors.lightgrey),
                             ('LINEABOVE', (0,0), (-1,0), 1, colors.black),
                             ('LINEABOVE', (0,1), (-1,1), 1, colors.black)])
        
        doc_contents.append(table)

    def plotSummary(self, doc_contents: list):
        doc_contents.append(PageBreak())
        doc_contents.append(Paragraph("<b><u><font size=11 color=\"darkblue\">Summary plot:</font></u></b>"))
        doc_contents.append(Spacer(1, 16)) # add spacing of 8 pts
        doc_contents.append(Image(self._summary_plot, width=16*cm, height=16*cm))

    def signature(self, doc_contents: list):

        data = [[Paragraph("<b>Done by</b>"), ":", self._author],
                [Paragraph("<b>Signature</b>"), ":", ""]]

        table = Table(data, colWidths=[3.0*cm, 0.5*cm, 4*cm], hAlign="LEFT",
                      style=[('LINEBELOW', (-1,-1), (-1,-1), 1, colors.black)])
        doc_contents.append(TopPadder(table))

    def saveReport(self):
        document =  SimpleDocTemplate(self._filename)
        doc_contents = [Spacer(1, 2.0*cm)]

        # add document body and then build the PDF
        self.userDetails(doc_contents)
        self.analysisDetails(doc_contents)

        if self._summary_plot is not None:
            self.plotSummary(doc_contents)
        
        self.signature(doc_contents)

        document.build(doc_contents, onFirstPage=self.titlePage)