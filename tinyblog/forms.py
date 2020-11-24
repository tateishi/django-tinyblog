from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'entry')
        widgets = {
            'title': forms.TextInput(attrs=dict(placeholder='タイトル')),
            'entry': forms.Textarea(attrs=dict(rows=8)),
        }
