from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch, mm
from reportlab.lib import colors
from reportlab.platypus import Table, TableStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import black, blue, red
import datetime

class TransactionReceipt:
    def __init__(self, transaction_id, date, customer_name, items, total_amount):
        self.transaction_id = transaction_id
        self.date = date
        self.customer_name = customer_name
        self.items = items
        self.total_amount = total_amount

    def generate_receipt(self, filename):
        doc = canvas.Canvas(filename, pagesize=A4)
        doc.setFillColor(blue)
        doc.setFontSize(20)
        doc.drawString(100, 750, "Transaction Receipt")

        styles = getSampleStyleSheet()
        styles.add(ParagraphStyle(name='Center', alignment=TA_CENTER, fontSize=12, leading=15))
        styles.add(ParagraphStyle(name='Left', alignment=TA_LEFT, fontSize=12, leading=15))

        ptext = '<font size=12>Transaction ID: {}</font>'.format(self.transaction_id)
        p = Paragraph(ptext, styles["Left"])
        p.wrapOn(doc, 500, 20)
        p.drawOn(doc, 100, 720)

        ptext = '<font size=12>Date: {}</font>'.format(self.date.strftime('%Y-%m-%d %H:%M:%S'))
        p = Paragraph(ptext, styles["Left"])
        p.wrapOn(doc, 500, 20)
        p.drawOn(doc, 100, 700)

        ptext = '<font size=12>Customer Name: {}</font>'.format(self.customer_name)
        p = Paragraph(ptext, styles["Left"])
        p.wrapOn(doc, 500, 20)
        p.drawOn(doc, 100, 680)

        data = [['Item', 'Quantity', 'Price', 'Total']]
        for item in self.items:
            data.append([item['name'], item['quantity'], '${:.2f}'.format(item['price']), '${:.2f}'.format(item['total'])])
        data.append(['', '', 'Total', '${:.2f}'.format(self.total_amount)])

        t = Table(data, colWidths=[100, 50, 50, 50])
        t.setStyle(TableStyle([
            ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
            ('FONTNAME', (0, 0), (-1, -1), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 12),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ]))
        w, h = t.wrapOn(doc, 500, 500)
        t.drawOn(doc, 50, 550)

        ptext = '<font size=12>Thank you for your purchase!</font>'
        p = Paragraph(ptext, styles["Center"])
        p.wrapOn(doc, 500, 20)
        p.drawOn(doc, 150, 500)

        doc.save()

# Example usage:
transaction_id = "TRX001"
date = datetime.datetime.now()
customer_name = "John Doe"
items = [
    {"name": "Apple iPhone", "quantity": 1, "price": 999.99, "total": 999.99},
    {"name": "Samsung TV", "quantity": 2, "price": 499.99, "total": 999.98},
    {"name": "Sony Headphones", "quantity": 3, "price": 99.99, "total": 299.97}
]
total_amount = sum(item["total"] for item in items)

receipt = TransactionReceipt(transaction_id, date, customer_name, items, total_amount)
receipt.generate_receipt("receipt.pdf")