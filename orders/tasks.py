from celery.app import task

from cart.models import Cart_bd
from svyatoslav_shop.celery import app


@app.task
def order_created():

    #order = Cart_bd.objects.get(id=cart_id)
    #subject = 'Order nr. {}'.format(order.id)
    #message = 'Dear {},\n\nYou have successfully placed an order.\
    #              Your order id is {}.'.format(order.first_name,
     #                                       order.id)

    with open('send_sms.txt', 'w') as out:
        out.write("Hello")
