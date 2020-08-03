from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

# будет вызвана в shop\view\prod._detail, cart\view
# Джанговский шаблон (а можно было писать тонну строк во фронте)

class CartAddProductForm(forms.Form):
  quantity = forms.TypedChoiceField( # -tag <Select>
            choices=PRODUCT_QUANTITY_CHOICES,
            coerce=int)
  # -для кнопк. <update> (без этого нет select) !??????
  override = forms.BooleanField(required=False, # CheckboxInput
                                initial=False,
                                widget=forms.HiddenInput)