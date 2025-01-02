from django import forms
from .models import ProductComment

class ProductCommentForm(forms.ModelForm):
    class Meta:
        model = ProductComment
        fields = ['name', 'email', 'comment', 'rating']
        widgets = {
            'rating': forms.RadioSelect(choices=[(i, f"{i} Star{'s' if i > 1 else ''}") for i in range(1, 6)]),
        }
