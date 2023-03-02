from django import forms


class ArticleForm(forms.Form):
    file = forms.FileField(label="Excel file",required=False)
    code = forms.IntegerField(required=False)