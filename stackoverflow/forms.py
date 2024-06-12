from .models import Comment
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'content']

        widgets = {
            'name': forms.TextInput(
                attrs={
                    'placeholder': 'Nombre Categoría',
                    'class': 'form-control form-control-md',
                    'autofocus': True
                }
            ),
            'body': forms.Textarea(attrs={'class': 'form-control form-control-lg'}),
        }