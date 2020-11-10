import wkhtmltopdf as wkhtmltopdf
from celery.app import task

from cart.models import Cart_bd
from svyatoslav_shop.celery import app


@app.task
def order_created():
    pdf = wkhtmltopdf(url='http://127.0.0.1:8000/', output_file='example.pdf')
    pdf.render()

