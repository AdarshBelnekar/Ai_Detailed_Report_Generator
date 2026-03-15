from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def build_report(report_text):

    file_path = "output/DDR_Report.pdf"

    c = canvas.Canvas(file_path, pagesize=letter)

    y = 750

    for line in report_text.split("\n"):

        if y < 40:
            c.showPage()
            y = 750

        c.drawString(40, y, line)
        y -= 15

    c.save()

    return file_path