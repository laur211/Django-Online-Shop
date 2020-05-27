from django import forms

product_quantity_choices=[(i,str(i)) for i in range (1,21)]

class CartQuantityForm(forms.Form):
    quantity=forms.TypedChoiceField(choices=product_quantity_choices,coerce=int)