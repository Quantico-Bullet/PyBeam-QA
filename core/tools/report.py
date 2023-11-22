from reportlab.platypus import (SimpleDocTemplate, Paragraph, PageBreak, Spacer, Table,
                                Image, TopPadder, Flowable)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT

from datetime import datetime

import io
from pdfrw import PdfReader, PdfDict
from pdfrw.buildxobj import pagexobj

from core.tools.toreportlab import makerl

styles = getSampleStyleSheet()

class BaseReport:
    """
    Base class for generating reports in PyBeam QA
    """

    default_style = styles["Normal"]

    def __init__(self, filename: str, report_name: str):
        self._filename = filename
        self.report_name = report_name

    def set_report_name(self, report_name: str):
        self.report_name = report_name
    
    def title_page(self, canvas: Canvas, document):
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

    def set_user_details(self, doc_contents: list):
        data = [[Paragraph("<b>Physicist</b>"), f": {self._author}"],
                [Paragraph("<b>Institution</b>"), f": {self._institution}"],
                [Paragraph("<b>Treatment unit</b>"), f": {self._treatment_unit_name}"],
                [Paragraph("<b>Analysis date</b>"), f": {datetime.today().strftime('%d %B %Y')}"],
                [Paragraph("<b>Test tolerance</b>"), f": {self._tolerance} mm"],
                [Paragraph("<b>Test outcome</b>"), f": {self._report_status}"]]
        
        if self._patient_info is not None:
            data.append(["",""])
            data.append([Paragraph("<b>Patient name</b>"), f": {self._patient_info['patient_name']}"])
            data.append([Paragraph("<b>Patient ID</b>"), f": {self._patient_info['patient_id']}"])
        
        doc_contents.append(Table(data, colWidths=[3.5*cm, 5.0*cm], hAlign="LEFT"))

    def set_analysis_details(self, doc_contents: list):
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

    def set_plot_summary(self, doc_contents: list):
        doc_contents.append(PageBreak())
        doc_contents.append(Paragraph("<b><u><font size=11 color=\"darkblue\">Summary plot:</font></u></b>"))
        doc_contents.append(Spacer(1, 16)) # add spacing of 8 pts
        doc_contents.append(PdfImage(self._summary_plot, width=16*cm, height=16*cm))

    def add_signature(self, doc_contents: list):

        data = [[Paragraph("<b>Performed by</b>"), ":", self._author],
                [Paragraph("<b>Signature</b>"), ":", ""]]

        table = Table(data, colWidths=[3.0*cm, 0.5*cm, 4*cm], hAlign="LEFT",
                      style=[('LINEBELOW', (-1,-1), (-1,-1), 1, colors.black)])
        doc_contents.append(TopPadder(table))

    def save_report(self):
        document =  SimpleDocTemplate(self._filename)
        doc_contents = [Spacer(1, 2.0*cm)]

        # add document body and then build the PDF
        self.set_user_details(doc_contents)
        self.set_analysis_details(doc_contents)

        if self._summary_plot is not None:
            self.set_plot_summary(doc_contents)
        
        self.add_signature(doc_contents)

        document.build(doc_contents, onFirstPage=self.title_page)

class PicketFenceReport(BaseReport):
    """
    Class for generating Picket fence reports
    """
    def __init__(
        self, filename: str,
        report_name: str = "Picket Fence Analysis Report",
        author: str = "N/A",
        institution: str = "N/A",
        treatment_unit_name: str = None,
        mlc_type: str = "N/A",
        analysis_summary: list = None,
        summary_plot: io.BytesIO = None,
        report_status: str = "N/A",
        max_error: float = None,
        tolerance: float = 0.5,
        comments: str | None = None
        ):
        super().__init__(filename, report_name)

        self._author = author
        self._institution = institution
        self._treatment_unit_name = treatment_unit_name
        self._mlc_type = mlc_type
        self._analysis_summary = analysis_summary
        self._summary_plot = summary_plot
        self._report_status = report_status
        self._max_error = max_error
        self._tolerance = tolerance
        self._comments = comments

    def set_user_details(self, doc_contents: list):
        data = [[Paragraph("<b>Physicist</b>"), f": {self._author}"],
                [Paragraph("<b>Institution</b>"), f": {self._institution}"],
                [Paragraph("<b>Treatment unit</b>"), f": {self._treatment_unit_name}"],
                [Paragraph("<b>MLC type</b>"), f": {self._mlc_type}"],
                [Paragraph("<b>Analysis date</b>"), f": {datetime.today().strftime('%d %B %Y')}"],
                [Paragraph("<b>Test tolerance</b>"), f": {self._tolerance:2.2f} mm"]]
        
        if self._max_error is not None:
            data.append([Paragraph("<b>Test outcome</b>"),
                         f": {self._report_status} (Max. error = {self._max_error:2.3f} mm)"])
            
        else:
            data.append([Paragraph("<b>Test outcome</b>"), f": {self._report_status}"])
        
        doc_contents.append(Table(data, colWidths=[3.5*cm, 5.0*cm], hAlign="LEFT"))

    def set_analysis_details(self, doc_contents: list):
        doc_contents.append(Spacer(1, 16)) # add spacing of 8 pts
        doc_contents.append(Paragraph("<b><u><font size=11 color=\"darkblue\">Analysis Details:</font></u></b>"))
        doc_contents.append(Spacer(1, 16)) # add spacing of 16 pts

        data = self._analysis_summary
        data.insert(0, [Paragraph("<b>Parameter</b>"), Paragraph("<b>Value</b>"), Paragraph("<b>Comment(s)</b>")])

        table = Table(data, colWidths=[6.0*cm, 3.0*cm, 6.5*cm], hAlign="LEFT",
                      style=[('GRID', (0,0), (-1,-1), 0.5, colors.grey),
                             ('BACKGROUND', (0,0), (-1,0), colors.lightgrey),
                             ('LINEABOVE', (0,0), (-1,0), 1, colors.black),
                             ('LINEABOVE', (0,1), (-1,1), 1, colors.black)])
        
        doc_contents.append(table)

    def set_plot_summary(self, doc_contents: list):
        doc_contents.append(PageBreak())
        doc_contents.append(Paragraph("<b><u><font size=11 color=\"darkblue\">Summary plot:</font></u></b>"))
        doc_contents.append(Spacer(1, 16)) # add spacing of 8 pts

        image = PdfImage(self._summary_plot, width=8.0*cm, height=8.0*cm)
        image.hAlign = "CENTRE"
        doc_contents.append(image)

    def add_signature(self, doc_contents: list):

        data = [[Paragraph("<b>Performed by</b>"), ":", self._author],
                [Paragraph("<b>Signature</b>"), ":", ""]]

        table = Table(data, colWidths=[3.0*cm, 0.5*cm, 4*cm], hAlign="LEFT",
                      style=[('LINEBELOW', (-1,-1), (-1,-1), 1, colors.black)])
        doc_contents.append(TopPadder(table))

    def save_report(self):
        document =  SimpleDocTemplate(self._filename)
        doc_contents = [Spacer(1, 2.0*cm)]

        # add document body and then build the PDF
        self.set_user_details(doc_contents)
        self.set_analysis_details(doc_contents)

        if self._summary_plot is not None:
            self.set_plot_summary(doc_contents)
        
        self.add_signature(doc_contents)

        document.build(doc_contents, onFirstPage=self.title_page)

class FieldAnalysisReport(BaseReport):
    """
    Class for generating Field Analysis reports
    """
    def __init__(
        self, filename: str,
        report_name: str = "Field Analysis Report",
        author: str = "N/A",
        institution: str = "N/A",
        protocol: str = "N/A",
        treatment_unit_name: str = None,
        analysis_summary: dict = None,
        summary_plots: list[io.BytesIO] = None,
        comments: str | None = None
        ):
        super().__init__(filename, report_name)

        self._author = author
        self._institution = institution
        self._treatment_unit_name = treatment_unit_name
        self._protocol = protocol
        self._analysis_summary = analysis_summary
        self._summary_plots = summary_plots
        self._comments = comments

    def set_user_details(self, doc_contents: list):
        data = [
            [Paragraph("<b>Physicist</b>"), f": {self._author}"],
            [Paragraph("<b>Institution</b>"), f": {self._institution}"],
            [Paragraph("<b>Treatment unit</b>"), f": {self._treatment_unit_name}"],
            [Paragraph("<b>Analysis date</b>"), f": {datetime.today().strftime('%d %B %Y')}"],
            [],
            [Paragraph("<b>Analysis protocol</b>"), f": {self._protocol}"]
        ]
        
        doc_contents.append(Table(data, colWidths=[3.5*cm, 5.0*cm], hAlign="LEFT"))

    def set_analysis_details(self, doc_contents: list):
        results = self._analysis_summary

        for title in results.keys():
            doc_contents.append(Spacer(1, 16)) # add spacing of 8 pts
            doc_contents.append(Paragraph(f"<b><u><font size=11 color=\"darkblue\">{title}</font></u></b>"))
            doc_contents.append(Spacer(1, 16)) # add spacing of 16 pts

            data = []
            data.insert(0, [Paragraph("<b>Parameter</b>"),
                            Paragraph("<b>Value</b>")]
                            )
            
            for item in results[title]:
                data.append(item)

            table = Table(data, colWidths=[8.0*cm, 5.0*cm], hAlign="LEFT",
                      style=[('GRID', (0,0), (-1,-1), 0.5, colors.grey),
                             ('BACKGROUND', (0,0), (-1,0), colors.lightgrey),
                             ('LINEABOVE', (0,0), (-1,0), 1, colors.black),
                             ('LINEABOVE', (0,1), (-1,1), 1, colors.black)])
        
            doc_contents.append(table)

    def set_plot_summary(self, doc_contents: list):
        #doc_contents.append(PageBreak())
        doc_contents.append(Spacer(1, 16))
        doc_contents.append(Paragraph("<b><u><font size=11 color=\"darkblue\">Summary plots:</font></u></b>"))
        doc_contents.append(Spacer(1, 16)) # add spacing of 16 pts

        data = [[PdfImage(self._summary_plots[0], width=9.0*cm, height=9.0*cm), 
                 PdfImage(self._summary_plots[1], width=9.0*cm, height=9.0*cm)]]

        doc_contents.append(Table(data, colWidths=[9.0*cm, 9.0*cm], hAlign="CENTER"))

    def add_signature(self, doc_contents: list):

        data = [[Paragraph("<b>Performed by</b>"), ":", self._author],
                [Paragraph("<b>Signature</b>"), ":", ""]]

        table = Table(data, colWidths=[3.0*cm, 0.5*cm, 4*cm], hAlign="LEFT",
                      style=[('LINEBELOW', (-1,-1), (-1,-1), 1, colors.black)])
        doc_contents.append(TopPadder(table))

    def save_report(self):
        document =  SimpleDocTemplate(self._filename)
        doc_contents = [Spacer(1, 2.0*cm)]

        # add document body and then build the PDF
        self.set_user_details(doc_contents)
        self.set_analysis_details(doc_contents)

        if self._summary_plots is not None:
            self.set_plot_summary(doc_contents)
        
        self.add_signature(doc_contents)

        document.build(doc_contents, onFirstPage=self.title_page)
       
class StarshotReport(BaseReport):
    """
    Class for generating Starshot reports
    """
    def __init__(
        self, filename: str,
        report_name: str = "Starshot Analysis Report",
        author: str = "N/A",
        institution: str = "N/A",
        treatment_unit_name: str = None,
        analysis_summary: list = None,
        summary_plots: list[io.BytesIO] = None,
        report_status: str = "N/A",
        wobble_diameter: float = None,
        tolerance: float = 1.0,
        comments: str | None = None
        ):
        super().__init__(filename, report_name)

        self._author = author
        self._institution = institution
        self._treatment_unit_name = treatment_unit_name
        self._analysis_summary = analysis_summary
        self._summary_plots = summary_plots
        self._report_status = report_status
        self._wobble_diameter = wobble_diameter
        self._tolerance = tolerance
        self._comments = comments

    def set_user_details(self, doc_contents: list):
        data = [[Paragraph("<b>Physicist</b>"), f": {self._author}"],
                [Paragraph("<b>Institution</b>"), f": {self._institution}"],
                [Paragraph("<b>Treatment unit</b>"), f": {self._treatment_unit_name}"],
                [Paragraph("<b>Analysis date</b>"), f": {datetime.today().strftime('%d %B %Y')}"],
                [Paragraph("<b>Test tolerance</b>"), f": {self._tolerance:2.2f} mm"],
                [Paragraph("<b>Test outcome</b>"),
                         f": {self._report_status} (wobble diameter  = {self._wobble_diameter:2.3f} mm)"]]
        
        doc_contents.append(Table(data, colWidths=[3.5*cm, 5.0*cm], hAlign="LEFT"))

    def set_analysis_details(self, doc_contents: list):
        doc_contents.append(Spacer(1, 16)) # add spacing of 16 pts
        doc_contents.append(Paragraph("<b><u><font size=11 color=\"darkblue\">Analysis Details:</font></u></b>"))
        doc_contents.append(Spacer(1, 16)) # add spacing of 16 pts

        data = self._analysis_summary
        data.insert(0, [Paragraph("<b>Parameter</b>"), Paragraph("<b>Value</b>"), Paragraph("<b>Comment(s)</b>")])

        table = Table(data, colWidths=[6.0*cm, 3.0*cm, 6.5*cm], hAlign="LEFT",
                      style=[('GRID', (0,0), (-1,-1), 0.5, colors.grey),
                             ('BACKGROUND', (0,0), (-1,0), colors.lightgrey),
                             ('LINEABOVE', (0,0), (-1,0), 1, colors.black),
                             ('LINEABOVE', (0,1), (-1,1), 1, colors.black)])
        
        doc_contents.append(table)

    def set_plot_summary(self, doc_contents: list):
        #doc_contents.append(PageBreak())
        doc_contents.append(Spacer(1, 16))
        doc_contents.append(Paragraph("<b><u><font size=11 color=\"darkblue\">Summary plots:</font></u></b>"))
        doc_contents.append(Spacer(1, 16)) # add spacing of 16 pts

        data = [[PdfImage(self._summary_plots[0], width=7.5*cm, height=7.5*cm), 
                 PdfImage(self._summary_plots[1], width=7.5*cm, height=7.5*cm)]]

        doc_contents.append(Table(data, colWidths=[8.0*cm, 8.0*cm], hAlign="CENTER"))

    def add_signature(self, doc_contents: list):

        data = [[Paragraph("<b>Performed by</b>"), ":", self._author],
                [Paragraph("<b>Signature</b>"), ":", ""]]

        table = Table(data, colWidths=[3.0*cm, 0.5*cm, 4*cm], hAlign="LEFT",
                      style=[('LINEBELOW', (-1,-1), (-1,-1), 1, colors.black)])
        doc_contents.append(TopPadder(table))

    def save_report(self):
        document =  SimpleDocTemplate(self._filename)
        doc_contents = [Spacer(1, 2.0*cm)]

        # add document body and then build the PDF
        self.set_user_details(doc_contents)
        self.set_analysis_details(doc_contents)

        if self._summary_plots is not None:
            self.set_plot_summary(doc_contents)
        
        self.add_signature(doc_contents)

        document.build(doc_contents, onFirstPage=self.title_page)

class PlanarImagingReport(BaseReport):
    """
    Class for generating Planar Imaging reports
    """
    def __init__(
        self, filename: str,
        report_name: str = "Planar Imaging Analysis Report",
        author: str = "N/A",
        institution: str = "N/A",
        treatment_unit_name: str = None,
        analysis_summary: list = None,
        summary_plots: list[io.BytesIO] = None,
        comments: str | None = None
        ):
        super().__init__(filename, report_name)

        self._author = author
        self._institution = institution
        self._treatment_unit_name = treatment_unit_name
        self._analysis_summary = analysis_summary
        self._summary_plots = summary_plots
        self._comments = comments

    def set_user_details(self, doc_contents: list):
        data = [[Paragraph("<b>Physicist</b>"), f": {self._author}"],
                [Paragraph("<b>Institution</b>"), f": {self._institution}"],
                [Paragraph("<b>Treatment unit</b>"), f": {self._treatment_unit_name}"],
                [Paragraph("<b>Analysis date</b>"), f": {datetime.today().strftime('%d %B %Y')}"],
                [Paragraph("<b>Test tolerance</b>"), f": {self._tolerance:2.2f} mm"],
                [Paragraph("<b>Test outcome</b>"),
                         f": {self._report_status} (wobble diameter  = {self._wobble_diameter:2.3f} mm)"]]
        
        doc_contents.append(Table(data, colWidths=[3.5*cm, 5.0*cm], hAlign="LEFT"))

    def set_analysis_details(self, doc_contents: list):
        doc_contents.append(Spacer(1, 16)) # add spacing of 16 pts
        doc_contents.append(Paragraph("<b><u><font size=11 color=\"darkblue\">Analysis Details:</font></u></b>"))
        doc_contents.append(Spacer(1, 16)) # add spacing of 16 pts

        data = self._analysis_summary
        data.insert(0, [Paragraph("<b>Parameter</b>"), Paragraph("<b>Value</b>"), Paragraph("<b>Comment(s)</b>")])

        table = Table(data, colWidths=[6.0*cm, 3.0*cm, 6.5*cm], hAlign="LEFT",
                      style=[('GRID', (0,0), (-1,-1), 0.5, colors.grey),
                             ('BACKGROUND', (0,0), (-1,0), colors.lightgrey),
                             ('LINEABOVE', (0,0), (-1,0), 1, colors.black),
                             ('LINEABOVE', (0,1), (-1,1), 1, colors.black)])
        
        doc_contents.append(table)

    def set_plot_summary(self, doc_contents: list):
        #doc_contents.append(PageBreak())
        doc_contents.append(Spacer(1, 16))
        doc_contents.append(Paragraph("<b><u><font size=11 color=\"darkblue\">Summary plots:</font></u></b>"))
        doc_contents.append(Spacer(1, 16)) # add spacing of 16 pts

        data = [[PdfImage(self._summary_plots[0], width=7.5*cm, height=7.5*cm), 
                 PdfImage(self._summary_plots[1], width=7.5*cm, height=7.5*cm)]]

        doc_contents.append(Table(data, colWidths=[8.0*cm, 8.0*cm], hAlign="CENTER"))

    def add_signature(self, doc_contents: list):

        data = [[Paragraph("<b>Performed by</b>"), ":", self._author],
                [Paragraph("<b>Signature</b>"), ":", ""]]

        table = Table(data, colWidths=[3.0*cm, 0.5*cm, 4*cm], hAlign="LEFT",
                      style=[('LINEBELOW', (-1,-1), (-1,-1), 1, colors.black)])
        doc_contents.append(TopPadder(table))

    def save_report(self):
        document =  SimpleDocTemplate(self._filename)
        doc_contents = [Spacer(1, 2.0*cm)]

        # add document body and then build the PDF
        self.set_user_details(doc_contents)
        self.set_analysis_details(doc_contents)

        if self._summary_plots is not None:
            self.set_plot_summary(doc_contents)
        
        self.add_signature(doc_contents)

        document.build(doc_contents, onFirstPage=self.title_page)

class PhotonCalibrationReport(BaseReport):
    """
    Class for generating TRS398 Photon output calibration reports
    """
    def __init__(
        self, filename: str,
        report_name: str = "Photon Output Calibration Report",
        author: str = "N/A",
        institution: str = "N/A",
        treatment_unit_name: str = None,
        calibration_info: dict = None,
        comments: str | None = None
        ):
        super().__init__(filename, report_name)

        self._author = author
        self._institution = institution
        self._treatment_unit_name = treatment_unit_name
        self._calibration_info = calibration_info
        self._comments = comments
        self._tolerance = 1.0

    def set_user_details(self, doc_contents: list):
        data = [[Paragraph("<b>Physicist</b>"), f": {self._author}"],
                [Paragraph("<b>Institution</b>"), f": {self._institution}"],
                [Paragraph("<b>Treatment unit</b>"), f": {self._treatment_unit_name}"],
                [Paragraph("<b>Analysis date</b>"), f": {datetime.today().strftime('%d %B %Y')}"],
                [Paragraph("<b>Test tolerance</b>"), f": {self._tolerance:2.1f} %"],
                [Paragraph("<b>Test outcome</b>"), f": {self._report_status}"]]
        
        doc_contents.append(Table(data, colWidths=[3.5*cm, 5.0*cm], hAlign="LEFT"))

    def set_analysis_details(self, doc_contents: list):
        doc_contents.append(Spacer(1, 16)) # add spacing of 16 pts
        doc_contents.append(Paragraph("<b><u><font size=11 color=\"darkblue\">Analysis Details:</font></u></b>"))
        doc_contents.append(Spacer(1, 16)) # add spacing of 16 pts

        data = self._analysis_summary
        data.insert(0, [Paragraph("<b>Parameter</b>"), Paragraph("<b>Value</b>"), Paragraph("<b>Comment(s)</b>")])

        table = Table(data, colWidths=[6.0*cm, 3.0*cm, 6.5*cm], hAlign="LEFT",
                      style=[('GRID', (0,0), (-1,-1), 0.5, colors.grey),
                             ('BACKGROUND', (0,0), (-1,0), colors.lightgrey),
                             ('LINEABOVE', (0,0), (-1,0), 1, colors.black),
                             ('LINEABOVE', (0,1), (-1,1), 1, colors.black)])
        
        doc_contents.append(table)

    def set_plot_summary(self, doc_contents: list):
        #doc_contents.append(PageBreak())
        doc_contents.append(Spacer(1, 16))
        doc_contents.append(Paragraph("<b><u><font size=11 color=\"darkblue\">Summary plots:</font></u></b>"))
        doc_contents.append(Spacer(1, 16)) # add spacing of 16 pts

        data = [[PdfImage(self._summary_plots[0], width=7.5*cm, height=7.5*cm), 
                 PdfImage(self._summary_plots[1], width=7.5*cm, height=7.5*cm)]]

        doc_contents.append(Table(data, colWidths=[8.0*cm, 8.0*cm], hAlign="CENTER"))

    def add_signature(self, doc_contents: list):

        data = [[Paragraph("<b>Performed by</b>"), ":", self._author],
                [Paragraph("<b>Signature</b>"), ":", ""]]

        table = Table(data, colWidths=[3.0*cm, 0.5*cm, 4*cm], hAlign="LEFT",
                      style=[('LINEBELOW', (-1,-1), (-1,-1), 1, colors.black)])
        doc_contents.append(TopPadder(table))

    def save_report(self):
        document =  SimpleDocTemplate(self._filename)
        doc_contents = [Spacer(1, 2.0*cm)]

        # add document body and then build the PDF
        self.set_user_details(doc_contents)
        self.set_analysis_details(doc_contents)

        if self._summary_plots is not None:
            self.set_plot_summary(doc_contents)
        
        self.add_signature(doc_contents)

        document.build(doc_contents, onFirstPage=self.title_page)

class PdfImage(Flowable):
    def __init__(self, img_data: io.BytesIO, width=200, height=200):
        self.img_width = width
        self.img_height = height
        img_data.seek(0)

        self.img_data = self.form_xo_reader(img_data)

    def form_xo_reader(self, imgdata):
        page, = PdfReader(imgdata).pages
        return pagexobj(page)

    def wrap(self, width, height):
        return self.img_width, self.img_height

    def drawOn(self, canv, x, y, _sW=0):
        if _sW > 0 and hasattr(self, 'hAlign'):
            a = self.hAlign
            if a in ('CENTER', 'CENTRE', TA_CENTER):
                x += 0.5*_sW
            elif a in ('RIGHT', TA_RIGHT):
                x += _sW
            elif a not in ('LEFT', TA_LEFT):
                raise ValueError("Bad hAlign value " + str(a))
        canv.saveState()
        img = self.img_data
        if isinstance(img, PdfDict):
            xscale = self.img_width / img.BBox[2]
            yscale = self.img_height / img.BBox[3]
            canv.translate(x, y)
            canv.scale(xscale, yscale)
            canv.doForm(makerl(canv, img))
        else:
            canv.drawImage(img, x, y, self.img_width, self.img_height)
        canv.restoreState()