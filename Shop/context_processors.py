from Shop.models import Order


def cartitems_processor(request):
    if Order.objects.all():
        cartItems = 0
        items = Order.objects.all()
        for item in items:
            cartItems = cartItems + item.get_cart_items
    return {'cartItems': cartItems}