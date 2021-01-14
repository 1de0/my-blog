from django import forms
from .models import Post
from ckeditor.fields import CKEditorWidget

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'text',)
        text = forms.CharField(widget=CKEditorWidget(attrs={
            'class': 'content'
        }))
        widgets = {
            'title': forms.TextInput(attrs={
                'placeholder': '제목',
                'class': 'form-title'
                }),
            'author': forms.TextInput(attrs={
                'placeholder': '작성자',
                'class': 'form-author'
                })
        }