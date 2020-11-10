import pdfkit

from svyatoslav_shop.celery import app

@app.task
def order_created(html_str, order_number):
    pdfkit.from_string(html_str, f'orders/pdf_files/order_№{order_number}.pdf')


