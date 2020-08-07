from django.shortcuts import render, get_object_or_404

from cart.cart import Cart
from .models import Category, Product
from cart.forms import CartAddProductForm
from django.conf import settings

# Create your views here.
def product_list(request, category_slug=None):
  category = None
  categories = Category.objects.all()
  products = Product.objects.filter(available=True)
  if category_slug:
    category = get_object_or_404(Category, slug=category_slug)
    products = products.filter(category=category)

  cart = Cart(request)
  return render(request, 'product/list.html',
                          {'category': category,
                           'categories': categories,
                           'products': products,
                           'cart': cart
                           })


def product_detail(request, id, slug):
  product = get_object_or_404(Product, id=id,
                              slug=slug,
                              available=True)
  cart_product_form = CartAddProductForm( )

  cart = Cart(request)
  return render(request, 'product/detail.html',
                context={'product': product,
                         'cart_product_form':cart_product_form, #устанав. в форме select
                         'cart': cart
                         })
