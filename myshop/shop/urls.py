from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name='shop'


# в TemplateView теперь тоже видно корзину (контекстный процессор)


urlpatterns = [
  path('', views.product_list, name='product_list'),
  path('<slug:category_slug>/', views.product_list, name='product_list_by_category' ),
  path('<int:id>/<slug:slug>', views.product_detail, name='product_detail'),

  path('about',  TemplateView.as_view(template_name='about.html',
                                      extra_context={'header': 'About django_shop'}))
]