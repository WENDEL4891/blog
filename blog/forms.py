from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['topic', 'title', 'text']
        labels = {
            'title': 'Título',
            'text': '',
            'topic': 'Assunto'
        }