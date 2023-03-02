import pandas as pd

from django.shortcuts import render
from django.views.generic import FormView
from django.http import JsonResponse

from .models import Product
from .forms import ArticleForm

class ArticleFormView(FormView):
    template_name = 'parser/article.html'
    form_class = ArticleForm
    success_url = '/'

    def form_valid(self, form):
        code = form.cleaned_data['code']
        if code:
            Product.objects.create(code=code)
        elif 'file' in self.request.FILES:
            file = self.request.FILES['file']
            df = pd.read_excel(file)
            codes = df.iloc[:,0].to_list()
            for code in codes:
                Product.objects.create(code=code)
        return super().form_valid(form)


