from django.core import serializers
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm
import simplejson

@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)  # -благодаря этому отпадает необходим. в JS-коде (ajax..)
    if form.is_valid():
        cart_data = form.cleaned_data       # read data out form
        cart.add(product=product,
                 quantity=cart_data['quantity'],
                 # override_quantity=cart_data['override']
                 )

        #url.py: path('', views.cart_detail, name='cart_detail'),+стр. 30 (def cart_detail())

    return redirect('cart:cart_detail')


@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    # -без этого нет чекбокса update
    for item in cart:
        # -кажд. элем. корз. получает форму "изм. кол-ва"
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'],
                                                                   'override': True})
    # #---------- -отправить в сессию Cart (корявввые методы)-------------------------------
    ## 1
    # # data = serializers.serialize('json', cart)
    # data = simplejson.dumps(cart) #, default=lambda x: x.__dict__)
    # request.session['Cart'] = data  #

    ## 2-
    # import jsonpickle
    # frozen = jsonpickle.encode(cart)
    # request.session['Cart'] = frozen

    return render(request, 'cart/detail.html', {'cart': cart})