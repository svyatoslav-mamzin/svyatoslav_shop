
def html_creater(username, order, cart):

    html_list = ['<!DOCTYPE html><html lang="en">',
                 '<head><meta charset="UTF-8">',
                 f'<title> Заказ № {order.id} </title></head><body>',
                 f'<p> username {username}</p>',
                 f'<p> delivery_address {order.delivery_address}</p>',
                 ]
    for item in cart.get_items_cart():
        html_list.append(f'<p> {item.product.name} -- {item.quantity} шт -- {item.get_cost()} руб </p>')
    html_list.append(f"ИТОГО: {order.get_total_cost()} </body></html>")

    return " ".join(html_list)