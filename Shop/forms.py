from django import forms
from Shop.models import Product, Comment


class SearchForm(forms.ModelForm):
    myCategory = forms.CharField(label='myCategory', max_length=100)

    class Meta:
        model = Product
        fields = ['title']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'image', 'category']
        widgets = {
            'creator': forms.HiddenInput(),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
        widgets = {
            'user' : forms.HiddenInput(),
            'product':forms.HiddenInput(),
        }