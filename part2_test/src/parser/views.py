import pandas as pd

from rest_framework.views import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer, BrowsableAPIRenderer

from .models import Product

@api_view(http_method_names=['POST'])
def post_code(request):
    if 'file' in request.FILES:
        file = request.FILES['file']
        df = pd.read_excel(file)
        codes = df.iloc[:, 0].tolist()
        return Response({'codes': codes})
    elif 'code' in request.POST:
        code = request.POST['code']
        return Response({'code': code})
    return Response({'error': 'Invalid request'}, status=400)

