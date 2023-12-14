from django import forms
from django_summernote.widgets import SummernoteWidget


from blog.models import Article


class EditArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['text_1']
        widgets = {
            'text_1': SummernoteWidget(),
        }


