import pdfkit
from cart.models import Cart_bd
from svyatoslav_shop.celery import app


@app.task
def order_created():
    pdfkit.from_url('http://127.0.0.1:8000/', 'example.pdf')


