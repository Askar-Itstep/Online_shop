from django import forms
from django.contrib import admin

# Register your models here.
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
  list_display = ['name', 'slug']
  prepopulated_fields = {'slug': ('name',)}


###-------------------------------------
class ChangeCategoryForm(forms.Form):
    _selected_action = forms.CharField(widget=forms.MultipleHiddenInput)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), label=u'Основная категория')

def move_to_category(modeladmin, request, queryset):
    # queryset.update(category='p')
    form = None

    if 'apply' in request.POST:
        form = ChangeCategoryForm(request.POST)

        if form.is_valid():
            category = form.cleaned_data['category']

            count = 0
            for item in queryset:
                item.category = category
                item.save()
                count += 1

            modeladmin.message_user(request, "Категория %s применена к %d товарам." % (category, count))
            return HttpResponseRedirect(request.get_full_path())

    if not form:
        form = ChangeCategoryForm(initial={'_selected_action': request.POST.getlist(admin.ACTION_CHECKBOX_NAME)})

    return render(request, 'shop/product/move_to_category.html',
                  {'items': queryset, 'form': form, 'title': u'Изменение категории'})

move_to_category.short_description = "Сhange the category"

##-------------------------------------------------
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
  list_filter = ['available', 'created', 'update']
  list_display = ['name', 'slug', 'price', 'image', 'description', 'available', 'created', 'update']
  list_editable = ['slug', 'available', 'image', 'price', 'description']
  prepopulated_fields = {'slug': ('name',)}



