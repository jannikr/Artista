from django import forms

from Shop.models import Product


class SearchForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['title']