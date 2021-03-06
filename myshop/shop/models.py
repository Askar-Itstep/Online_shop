from django.db import models
from django.urls import reverse

# Create your models here.
'''
  У нас будут различные продукты ,
  Продукты разделены по категориям
  Например: 
  Python 2st Book - Книги 
  HarryPotter - Диски
  Iphone - Телефоны 
  
  Итого в бд будут категория и продукт
'''


class Category(models.Model):

  name = models.CharField(max_length=200,
                          db_index=True)
  slug = models.SlugField(max_length=200, unique=True)


  class Meta:
    ordering = ('name',)
    verbose_name = 'category'
    verbose_name_plural = 'categories'

  def __str__(self):
    return self.name


  def get_absolute_url(self):
    return reverse('shop:product_list_by_category', args=[self.slug])

##############################################################################
class Product(models.Model):
  category = models.ForeignKey(Category, related_name='products',
                               on_delete=models.CASCADE)

  name = models.CharField(max_length=200, db_index=True)
  slug = models.SlugField(max_length=200, db_index=True)
  image = models.ImageField(upload_to='products/%Y/%m/%d',
                            blank=True)
  price = models.DecimalField(max_digits=10, decimal_places=2)
  description = models.TextField(blank=True)
  available = models.BooleanField(default=True)
  created = models.DateTimeField(auto_now_add=True)
  update = models.DateTimeField(auto_now=True)

  class Meta:
    ordering = ('name',)
    index_together = (('id', 'slug'), )

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('shop:product_detail', args=[self.id, self.slug])