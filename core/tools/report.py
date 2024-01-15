from reportlab.platypus import (SimpleDocTemplate, Paragraph, PageBreak, Spacer, Table,
                                Image, TopPadder, Flowable)
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4, LETTER
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT

from datetime import datetime

import io
from pathlib import Path
from pdfrw import PdfReader, PdfDict
from pdfrw.buildxobj import pagexobj

from core.tools.toreportlab import makerl

assets_dir = Path(str(Path(__file__).parent) + "/report_assets").resolve()
assets_dir = str(assets_dir)

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
    
    def add_metadata(self, canvas: Canvas, document):
        canvas.setAuthor(self._author)
        canvas.setCreator("PyBeam QA")
        canvas.setTitle(self.report_name)
        canvas.setSubject("Radiotherapy QA")

        canvas.saveState()
        canvas.setFont("Helvetica-Bold", 20)
        canvas.drawCentredString(A4[0]/2.0, 26.0 * cm , self.report_name)
        canvas.restoreState()

    def add_page_number(self, canvas: Canvas, document):
        page_num = canvas.getPageNumber()
        text = f"Page {page_num}"

        canvas.drawCentredString(20.0*cm, 2.0*cm, text)

    def add_signature(self, doc_contents: list):

        data = [[Paragraph("<b>Performed by</b>"), ":", self._author],
                [Paragraph("<b>Signature</b>"), ":", ""]]

        table = Table(data, colWidths=[3.0*cm, 0.5*cm, 4*cm], hAlign="LEFT",
                      style=[('LINEBELOW', (-1,-1), (-1,-1), 1, colors.black),
                             ('LEFTPADDING', (-1,-1), (-1,-1), 0)])
        doc_contents.append(TopPadder(table))

    def add_comments(self, doc_contents: list):
        if self._comments:
            doc_contents.append(Spacer(1, 16))
            data = [[Paragraph("<b>Comments:</b>"), self._comments]]

            table = Table(data, colWidths=[3.0*cm, 0.5*cm, 4*cm], hAlign="LEFT",
                          style=[('VALIGN', (0,0), (0,0), 'TOP'),
                                 ('LEFTPADDING', (-1,-1), (-1,-1), 0)])
            doc_contents.append(table)

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
        
        doc_contents.append(Table(data, colWidths=[3.5*cm, 5.0*cm], hAlign="LEFT",
                                  style=[('LEFTPADDING', (-1,-1), (-1,-1), 0)]))

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

    def save_report(self):
        document =  SimpleDocTemplate(self._filename)
        doc_contents = [Spacer(1, 2.0*cm)]

        # add document body and then build the PDF
        self.set_user_details(doc_contents)
        self.set_analysis_details(doc_contents)

        if self._summary_plot is not None:
            self.set_plot_summary(doc_contents)
        
        self.add_signature(doc_contents)

        document.build(doc_contents, onFirstPage=self.add_metadata)

class PicketFenceReport(BaseReport):
    """
    Class for generating Picket fence reports
    """
    def __init__(
        self, filename: str,
        report_name: str = "Picket Fence Analysis Report",
        author: str = "N/A",
        institution: str = "N/A",
        treatment_unit_name: str | None = None,
        mlc_type: str = "N/A",
        analysis_summary: list | None = None,
        summary_plot: io.BytesIO | None = None,
        report_status: str = "N/A",
        max_error: float | None = None,
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
        
        doc_contents.append(Table(data, colWidths=[3.5*cm, 5.0*cm], hAlign="LEFT",
                                  style=[('LEFTPADDING', (-1,-1), (-1,-1), 0)]))

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

    def save_report(self):
        document =  SimpleDocTemplate(self._filename)
        doc_contents = [Spacer(1, 2.0*cm)]

        # add document body and then build the PDF
        self.set_user_details(doc_contents)
        self.set_analysis_details(doc_contents)

        if self._summary_plot is not None:
            self.set_plot_summary(doc_contents)
        
        self.add_signature(doc_contents)

        document.build(doc_contents, onFirstPage=self.add_metadata)

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
        treatment_unit_name: str | None = None,
        analysis_summary: dict | None = None,
        summary_plots: list[io.BytesIO] | None = None,
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
        
        doc_contents.append(Table(data, colWidths=[3.5*cm, 5.0*cm], hAlign="LEFT",
                                  style=[('LEFTPADDING', (-1,-1), (-1,-1), 0)]))

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

    def save_report(self):
        document =  SimpleDocTemplate(self._filename)
        doc_contents = [Spacer(1, 2.0*cm)]

        # add document body and then build the PDF
        self.set_user_details(doc_contents)
        self.set_analysis_details(doc_contents)

        if self._summary_plots is not None:
            self.set_plot_summary(doc_contents)
        
        self.add_signature(doc_contents)

        document.build(doc_contents, onFirstPage=self.add_metadata)
       
class StarshotReport(BaseReport):
    """
    Class for generating Starshot reports
    """
    def __init__(
        self, filename: str,
        report_name: str = "Starshot Analysis Report",
        author: str = "N/A",
        institution: str = "N/A",
        treatment_unit_name: str | None = None,
        analysis_summary: list | None = None,
        summary_plots: list[io.BytesIO] | None = None,
        report_status: str = "N/A",
        wobble_diameter: float | None = None,
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

    def save_report(self):
        document =  SimpleDocTemplate(self._filename)
        doc_contents = [Spacer(1, 2.0*cm)]

        # add document body and then build the PDF
        self.set_user_details(doc_contents)
        self.set_analysis_details(doc_contents)

        if self._summary_plots is not None:
            self.set_plot_summary(doc_contents)
        
        self.add_signature(doc_contents)

        document.build(doc_contents, onFirstPage=self.add_metadata)

class PlanarImagingReport(BaseReport):
    """
    Class for generating Planar Imaging reports
    """
    def __init__(
        self, filename: str,
        report_name: str = "Planar Imaging Analysis Report",
        author: str = "N/A",
        institution: str = "N/A",
        treatment_unit_name: str | None = None,
        analysis_summary: list | None = None,
        summary_plots: list[io.BytesIO] | None = None,
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
        
        doc_contents.append(Table(data, colWidths=[3.5*cm, 5.0*cm], hAlign="LEFT",
                                  style=[('LEFTPADDING', (-1,-1), (-1,-1), 0)]))

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

        document.build(doc_contents, onFirstPage=self.add_metadata)

class BaseCalibrationReport(BaseReport):
    """
    General class for generating TRS398 calibration reports
    """
    def __init__(
        self, filename: str,
        report_name: str = "Base Calibration Report",
        calibration_info: dict | None = None,
        ):
        super().__init__(filename, report_name)

        self._calibration_info = calibration_info
        self._author = self._calibration_info["user"] # We need this for self._author in title_page()
        self._comments = self._calibration_info["comments"]

    def set_user_details(self, doc_contents: list):
        data = [[Paragraph("<b>Physicist</b>"), f': {self._calibration_info["user"]}'],
                [Paragraph("<b>Institution</b>"), f': {self._calibration_info["institution"]}'],
                [Paragraph("<b>Treatment unit</b>"), f': {self._calibration_info["linac_name"]}'],
                [Paragraph("<b>Analysis date</b>"), f': {self._calibration_info["date"]}'],
                [Paragraph("<b>Test tolerance</b>"), f': {self._calibration_info["tolerance"]}%']]
        
        doc_contents.append(Table(data, colWidths=[3.5*cm, 5.0*cm], hAlign="LEFT"))

    def set_instrumentation_details(self, doc_contents: list):
        doc_contents.append(Spacer(1, 16)) # Add spacing of 16 pts
        doc_contents.append(Paragraph("<b><u><font size=11 color=\"darkblue\">Instrumentation:</font></u></b>"))
        doc_contents.append(Spacer(1, 12)) # Add spacing of 16 pts

        ion_chamber_info = self._calibration_info["ion_chamber"]
        elect_meter_info = self._calibration_info["electrometer"]

        #TODO Add operating voltage info

        data = [[Paragraph("<b>Ion. Chamber Model</b>"), f': {ion_chamber_info["model_name"]}'],
                [Paragraph("<b>Chamber Serial No.</b>"), f': {ion_chamber_info["serial_no"]}'],
                [Paragraph("<b>Calibration Laboratory</b>"), f': {ion_chamber_info["calibration_lab"]}'],
                [Paragraph("<b>Calibration Date</b>"), f': {ion_chamber_info["calibration_date"]}'],
                [Paragraph("<b>Calibration Coefficient</b>"), f': {ion_chamber_info["calibration_coeff"]} cGy/nC'],
                ["", ""],
                [Paragraph("<b>Electrometer Model</b>"), f': {elect_meter_info["model_name"]}'],
                [Paragraph("<b>Electrometer Serial No.</b>"), f': {elect_meter_info["serial_no"]}'],
                [Paragraph("<b>Calibration Laboratory</b>"), f': {elect_meter_info["calibration_lab"]}'],
                [Paragraph("<b>Calibration Date</b>"), f': {elect_meter_info["calibration_date"]}']]
        
        doc_contents.append(Table(data, colWidths=[4.5*cm, 5.0*cm], hAlign="LEFT"))

class PhotonCalibrationReport(BaseCalibrationReport):
    """
    Class for generating TRS398 Photon output calibration reports
    """
    def __init__(
        self, filename: str,
        report_name: str = "Photon Output Calibration Report",
        calibration_info: dict | None = None,
        comments: str | None = None
        ):
        super().__init__(filename, report_name, calibration_info)

    def set_measurement_details(self, doc_contents: list):
        doc_contents.append(Spacer(1, 16)) # add spacing of 16 pts
        doc_contents.append(Paragraph("<b><u><font size=11 color=\"darkblue\">Measurement Conditions:</font></u></b>"))
        doc_contents.append(Spacer(1, 16)) # add spacing of 16 pts
        #TODO Allow report to accept custom units of measurement

        worksheet = self._calibration_info["worksheets"][0]
        data = [[Paragraph("<b>Setup Type (SSD or SAD)</b>"), 
                 f': {"SSD" if self._calibration_info["setup_type"] == -2 else "SAD"}'],
                [Paragraph("<b>Reference Distance</b>"), f': {worksheet["reference_distance"]} cm'],
                [Paragraph("<b>Field Size</b>"), f': {worksheet["reference_field_size"].replace(" ", "")} cm²'],
                [Paragraph("<b>Number of MUs</b>"), f': {worksheet["corresponding_linac_mu"]}'],
                [Paragraph("<b>Temperature</b>"), f': {worksheet["user_temperature"]} °C'],
                [Paragraph("<b>Pressure</b>"), f': {worksheet["user_pressure"]} kPa'],
                [Paragraph("<b>Relative Humidity</b>"), f': {worksheet["user_humidity"]}%']]
        
        doc_contents.append(Table(data, colWidths=[5.5*cm, 3.5*cm], hAlign="LEFT"))

        data = [["", Paragraph("<para align='centre'><b>Nominal Accelerating Potential (MV)</b> \
                               </para>")],
                [Paragraph("<b>Parameter</b>")],
                ["Reference depth (g/cm²)"]
            ]
        
        num_worksheets = len(self._calibration_info["worksheets"])
        
        data[0].extend([""]*(num_worksheets-1))
        #data[7].extend([""]*num_worksheets)
        
        for worksheet in self._calibration_info["worksheets"]:
            data[1].append(worksheet["beam_energy"] + (" FFF" if worksheet["is_fff"] 
                                   else ""))
            """
            data[2].append("SSD" if self._calibration_info["setup_type"] == -2 else "SAD")
            data[3].append(worksheet["reference_distance"])
            """
            data[2].append(worksheet["reference_depth"])
            """
            data[5].append(worksheet["reference_field_size"].replace(" ", ""))
            data[6].append(worksheet["corresponding_linac_mu"])

            data[8].append(worksheet["user_temperature"])
            data[9].append(worksheet["user_pressure"])
            data[10].append(worksheet["user_humidity"])
            """
        col_widths = [5.5*cm]
        col_widths.extend([10.0*cm / num_worksheets]*num_worksheets)
        
        table = Table(data, colWidths=col_widths, hAlign='CENTRE',
                      style=[('BACKGROUND', (0,0), (-1,1), colors.lightgrey),
                             ('SPAN', (1,0), (-1,0)),
                             ('BOX', (0,0), (-1, -1), 1, colors.black),
                             ('LINEABOVE', (1,1), (-1,1), 0.5, colors.black),
                             ('LINEBEFORE', (1,0), (1, -1), 1, colors.black)])
        
        doc_contents.append(Spacer(1, 16))
        doc_contents.append(table)

    def set_correction_details(self, doc_contents: list):
        doc_contents.append(PageBreak())
        doc_contents.append(Spacer(1, 16)) # add spacing of 16 pts
        doc_contents.append(Paragraph("<b><u><font size=11 color=\"darkblue\">Beam Quality & " \
                                      "Correction Factors:</font></u></b>"))
        doc_contents.append(Spacer(1, 16)) # add spacing of 16 pts
        #TODO Allow report to accept custom units of measurement
        data = [["", Paragraph("<para align='centre'><b>Nominal Accelerating Potential (MV)</b> \
                               </para>")],
                [Paragraph("<b>Parameter</b>")],
                [PdfImage(assets_dir + "/tpr2010.pdf")],
                [PdfImage(assets_dir + "/kQQo.pdf")],
                [PdfImage(assets_dir + "/kElec.pdf")],
                [PdfImage(assets_dir + "/kTP.pdf")],
                [PdfImage(assets_dir + "/kPol.pdf")],
                [PdfImage(assets_dir + "/kS.pdf")],
                [""],
                ["Average dosimeter rdg. (nC)"],
                ["Corrected dosimeter rdg. (nC)"]]
        
        num_worksheets = len(self._calibration_info["worksheets"])
        data[0].extend([""]*(num_worksheets-1))
        data[8].extend([""]*num_worksheets)
        
        for worksheet in self._calibration_info["worksheets"]:
            data[1].append(worksheet["beam_energy"] + (" FFF" if worksheet["is_fff"] 
                                   else ""))
            
            cal_summary = worksheet["cal_summary"]
            data[2].append(worksheet["tpr_2010"])
            data[3].append(cal_summary["kQQo"])
            data[4].append(cal_summary["kElec"])
            data[5].append(cal_summary["kTP"])
            data[6].append(cal_summary["kPol"])
            data[7].append(cal_summary["kS"])

            data[9].append(worksheet["raw_dosimeter_reading_v1"])
            data[10].append(cal_summary["corr_dos_reading"])

        col_widths = [5.5*cm]
        col_widths.extend([10.0*cm / num_worksheets]*num_worksheets)
        table = Table(data, colWidths=col_widths, hAlign='CENTRE',
                      style=[('BACKGROUND', (0,0), (-1,1), colors.lightgrey),
                             ('SPAN', (1,0), (-1,0)),
                             ('BOX', (0,0), (-1,-1), 1, colors.black),
                             ('LINEABOVE', (1,1), (-1,1), 0.5, colors.black),
                             ('LINEBEFORE', (1,0), (1,-1), 1, colors.black)])
        
        doc_contents.append(table)

    def set_outcome_details(self, doc_contents: list):
        doc_contents.append(Spacer(1, 16)) # add spacing of 16 pts
        doc_contents.append(Paragraph("<b><u><font size=11 color=\"darkblue\">Absorbed Dose To Water:</font></u></b>"))
        doc_contents.append(Spacer(1, 16)) # add spacing of 16 pts

        data = [["", Paragraph("<para align='centre'><b>Nominal Accelerating Potential (MV)</b> \
                               </para>")],
                [Paragraph("<b>Parameter</b>")],
                [PdfImage(assets_dir + "/depth_zmax.pdf")],
                [],
                [PdfImage(assets_dir + "/dw_zref.pdf")],
                [PdfImage(assets_dir + "/dw_zmax.pdf")],
                [""],
                ["Outcome (PASS / FAIL)"]]
        
        num_worksheets = len(self._calibration_info["worksheets"])
        data[0].extend([""]*(num_worksheets-1))
        data[6].extend([""]*num_worksheets)

        beam_q_file, key = (("/pdd_zref.pdf", "pdd_zref") if self._calibration_info["setup_type"] == -2 
                            else ("/tmr_zref.pdf", "tmr_zref"))
        
        data[3].insert(0,PdfImage(assets_dir + beam_q_file))
        
        for worksheet in self._calibration_info["worksheets"]:
            data[1].append(worksheet["beam_energy"] + (" FFF" if worksheet["is_fff"] 
                                   else ""))
            
            cal_summary = worksheet["cal_summary"]
            data[2].append(worksheet["depth_dmax"])
            data[3].append(worksheet[key])
            data[4].append(cal_summary["dw_zref"])
            data[5].append(cal_summary["dw_zmax"])
            data[7].append(cal_summary["test_outcome"])

        col_widths = [5.5*cm]
        col_widths.extend([10.0*cm / num_worksheets]*num_worksheets)
        table = Table(data, colWidths=col_widths, hAlign='CENTRE',
                      style=[('BACKGROUND', (0,0), (-1,1), colors.lightgrey),
                             ('SPAN', (1,0), (-1,0)),
                             ('BOX', (0,0), (-1,-1), 1, colors.black),
                             ('LINEABOVE', (1,1), (-1,1), 0.5, colors.black),
                             ('LINEBEFORE', (1,0), (1,-1), 1, colors.black)])
        
        doc_contents.append(table)

    def add_signature(self, doc_contents: list):

        data = [[Paragraph("<b>Performed by</b>"), ":", self._calibration_info["user"]],
                [Paragraph("<b>Signature</b>"), ":", ""]]

        table = Table(data, colWidths=[3.0*cm, 0.5*cm, 4*cm], hAlign="LEFT",
                      style=[('LINEBELOW', (-1,-1), (-1,-1), 1, colors.black)])
        doc_contents.append(TopPadder(table))

    def save_report(self):
        document =  SimpleDocTemplate(self._filename, pagesize=A4, pageCompression=1)
        doc_contents = [Spacer(1, 2.0*cm)]

        # add document body and then build the PDF
        self.set_user_details(doc_contents)
        self.set_instrumentation_details(doc_contents)
        self.set_measurement_details(doc_contents)
        self.set_correction_details(doc_contents)
        self.set_outcome_details(doc_contents)
        
        self.add_comments(doc_contents)
        self.add_signature(doc_contents)

        document.build(doc_contents, onFirstPage=self.add_metadata)

class ElectronCalibrationReport(BaseCalibrationReport):
    """
    Class for generating TRS398 Electron output calibration reports
    """
    def __init__(
        self, filename: str,
        report_name: str = "Electron Output Calibration Report",
        calibration_info: dict | None = None,
        comments: str | None = None
        ):
        super().__init__(filename, report_name, calibration_info)

    def set_measurement_details(self, doc_contents: list):
        doc_contents.append(Spacer(1, 16)) # add spacing of 16 pts
        doc_contents.append(Paragraph("<b><u><font size=11 color=\"darkblue\">Measurement Conditions:</font></u></b>"))
        doc_contents.append(Spacer(1, 16)) # add spacing of 16 pts
        #TODO Allow report to accept custom units of measurement

        worksheet = self._calibration_info["worksheets"][0]
        data = [[Paragraph("<b>Setup Type (SSD or SAD)</b>"), "SSD"],
                [Paragraph("<b>Reference Distance</b>"), f': {worksheet["reference_distance"]} cm'],
                [Paragraph("<b>Field Size</b>"), f': {worksheet["reference_field_size"].replace(" ", "")} cm²'],
                [Paragraph("<b>Number of MUs</b>"), f': {worksheet["corresponding_linac_mu"]}'],
                [Paragraph("<b>Temperature</b>"), f': {worksheet["user_temperature"]} °C'],
                [Paragraph("<b>Pressure</b>"), f': {worksheet["user_pressure"]} kPa'],
                [Paragraph("<b>Relative Humidity</b>"), f': {worksheet["user_humidity"]}%']]
        
        doc_contents.append(Table(data, colWidths=[5.5*cm, 3.5*cm], hAlign="LEFT"))

        data = [["", Paragraph("<para align='centre'><b>Nominal Energy (MeV)</b> \
                               </para>")],
                [Paragraph("<b>Parameter</b>")],
                [PdfImage(assets_dir + "/meas_depth_zref.pdf")]
            ]
        
        num_worksheets = len(self._calibration_info["worksheets"])
        
        data[0].extend([""]*(num_worksheets-1))
        #data[7].extend([""]*num_worksheets)
        
        for worksheet in self._calibration_info["worksheets"]:
            data[1].append(worksheet["beam_energy"] + (" FFF" if worksheet["is_fff"] 
                                   else ""))
            """
            data[2].append("SSD" if self._calibration_info["setup_type"] == -2 else "SAD")
            data[3].append(worksheet["reference_distance"])
            """
            data[2].append(worksheet["reference_depth"])
            """
            data[5].append(worksheet["reference_field_size"].replace(" ", ""))
            data[6].append(worksheet["corresponding_linac_mu"])

            data[8].append(worksheet["user_temperature"])
            data[9].append(worksheet["user_pressure"])
            data[10].append(worksheet["user_humidity"])
            """
        col_widths = [5.5*cm]
        col_widths.extend([10.0*cm / num_worksheets]*num_worksheets)
        
        table = Table(data, colWidths=col_widths, hAlign='CENTRE',
                      style=[('BACKGROUND', (0,0), (-1,1), colors.lightgrey),
                             ('SPAN', (1,0), (-1,0)),
                             ('BOX', (0,0), (-1, -1), 1, colors.black),
                             ('LINEABOVE', (1,1), (-1,1), 0.5, colors.black),
                             ('LINEBEFORE', (1,0), (1, -1), 1, colors.black)])
        
        doc_contents.append(Spacer(1, 16))
        doc_contents.append(table)

    def set_correction_details(self, doc_contents: list):
        doc_contents.append(PageBreak())
        doc_contents.append(Spacer(1, 16)) # add spacing of 16 pts
        doc_contents.append(Paragraph("<b><u><font size=11 color=\"darkblue\">Beam Quality & " \
                                      "Correction Factors:</font></u></b>"))
        doc_contents.append(Spacer(1, 16)) # add spacing of 16 pts
        #TODO Allow report to accept custom units of measurement
        data = [["", Paragraph("<para align='centre'><b>Nominal Accelerating Potential (MV)</b> \
                               </para>")],
                [Paragraph("<b>Parameter</b>")],
                [PdfImage(assets_dir + "/r50.pdf")],
                [PdfImage(assets_dir + "/kQQo.pdf")],
                [PdfImage(assets_dir + "/kElec.pdf")],
                [PdfImage(assets_dir + "/kTP.pdf")],
                [PdfImage(assets_dir + "/kPol.pdf")],
                [PdfImage(assets_dir + "/kS.pdf")],
                [""],
                ["Average dosimeter rdg. (nC)"],
                ["Corrected dosimeter rdg. (nC)"]]
        
        num_worksheets = len(self._calibration_info["worksheets"])
        data[0].extend([""]*(num_worksheets-1))
        data[8].extend([""]*num_worksheets)
        
        for worksheet in self._calibration_info["worksheets"]:
            data[1].append(worksheet["beam_energy"] + (" FFF" if worksheet["is_fff"] 
                                   else ""))
            
            cal_summary = worksheet["cal_summary"]
            data[2].append(worksheet["tpr_2010"])
            data[3].append(cal_summary["kQQo"])
            data[4].append(cal_summary["kElec"])
            data[5].append(cal_summary["kTP"])
            data[6].append(cal_summary["kPol"])
            data[7].append(cal_summary["kS"])

            data[9].append(worksheet["raw_dosimeter_reading_v1"])
            data[10].append(cal_summary["corr_dos_reading"])

        col_widths = [5.5*cm]
        col_widths.extend([10.0*cm / num_worksheets]*num_worksheets)
        table = Table(data, colWidths=col_widths, hAlign='CENTRE',
                      style=[('BACKGROUND', (0,0), (-1,1), colors.lightgrey),
                             ('SPAN', (1,0), (-1,0)),
                             ('BOX', (0,0), (-1,-1), 1, colors.black),
                             ('LINEABOVE', (1,1), (-1,1), 0.5, colors.black),
                             ('LINEBEFORE', (1,0), (1,-1), 1, colors.black)])
        
        doc_contents.append(table)

    def set_outcome_details(self, doc_contents: list):
        doc_contents.append(Spacer(1, 16)) # add spacing of 16 pts
        doc_contents.append(Paragraph("<b><u><font size=11 color=\"darkblue\">Absorbed Dose To Water:</font></u></b>"))
        doc_contents.append(Spacer(1, 16)) # add spacing of 16 pts

        data = [["", Paragraph("<para align='centre'><b>Nominal Accelerating Potential (MV)</b> \
                               </para>")],
                [Paragraph("<b>Parameter</b>")],
                [PdfImage(assets_dir + "/depth_zmax.pdf")],
                [],
                [PdfImage(assets_dir + "/dw_zref.pdf")],
                [PdfImage(assets_dir + "/dw_zmax.pdf")],
                [""],
                ["Outcome (PASS / FAIL)"]]
        
        num_worksheets = len(self._calibration_info["worksheets"])
        data[0].extend([""]*(num_worksheets-1))
        data[6].extend([""]*num_worksheets)

        beam_q_file, key = (("/pdd_zref.pdf", "pdd_zref") if self._calibration_info["setup_type"] == -2 
                            else ("/tmr_zref.pdf", "tmr_zref"))
        
        data[3].insert(0,PdfImage(assets_dir + beam_q_file))
        
        for worksheet in self._calibration_info["worksheets"]:
            data[1].append(worksheet["beam_energy"] + (" FFF" if worksheet["is_fff"] 
                                   else ""))
            
            cal_summary = worksheet["cal_summary"]
            data[2].append(worksheet["depth_dmax"])
            data[3].append(worksheet[key])
            data[4].append(cal_summary["dw_zref"])
            data[5].append(cal_summary["dw_zmax"])
            data[7].append(cal_summary["test_outcome"])

        col_widths = [5.5*cm]
        col_widths.extend([10.0*cm / num_worksheets]*num_worksheets)
        table = Table(data, colWidths=col_widths, hAlign='CENTRE',
                      style=[('BACKGROUND', (0,0), (-1,1), colors.lightgrey),
                             ('SPAN', (1,0), (-1,0)),
                             ('BOX', (0,0), (-1,-1), 1, colors.black),
                             ('LINEABOVE', (1,1), (-1,1), 0.5, colors.black),
                             ('LINEBEFORE', (1,0), (1,-1), 1, colors.black)])
        
        doc_contents.append(table)

    def add_signature(self, doc_contents: list):

        data = [[Paragraph("<b>Performed by</b>"), ":", self._calibration_info["user"]],
                [Paragraph("<b>Signature</b>"), ":", ""]]

        table = Table(data, colWidths=[3.0*cm, 0.5*cm, 4*cm], hAlign="LEFT",
                      style=[('LINEBELOW', (-1,-1), (-1,-1), 1, colors.black)])
        doc_contents.append(TopPadder(table))

    def save_report(self):
        document =  SimpleDocTemplate(self._filename, pagesize=A4, pageCompression=1)
        doc_contents = [Spacer(1, 2.0*cm)]

        # add document body and then build the PDF
        self.set_user_details(doc_contents)
        self.set_instrumentation_details(doc_contents)
        self.set_measurement_details(doc_contents)
        self.set_correction_details(doc_contents)
        self.set_outcome_details(doc_contents)
        
        self.add_signature(doc_contents)

        document.build(doc_contents, onFirstPage=self.add_metadata)

class PdfImage(Flowable):
    def __init__(self, image: str | io.BytesIO, width=None, height=None):
        self.img_width = width
        self.img_height = height

        if isinstance(image, io.BytesIO):
            image.seek(0)

        self.img_data = self.form_xo_reader(image)

    def form_xo_reader(self, imgdata):
        page, = PdfReader(imgdata).pages

        if self.img_width is None or self.img_height is None:
            self.img_width = float(page['/MediaBox'][2])
            self.img_height = float(page['/MediaBox'][3])

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