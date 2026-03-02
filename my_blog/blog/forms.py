from django import forms 
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article 
        fields = ['title' , 'content' , 'pub_date']
        widgets = {
            'pub_date': forms.DateInput(attrs={'type':'date'}),
        }