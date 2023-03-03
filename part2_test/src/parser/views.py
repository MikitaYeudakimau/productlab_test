import aiohttp
import asyncio
import pandas as pd
from pydantic import BaseModel

from django.core.exceptions import ObjectDoesNotExist

from rest_framework.views import Response
from rest_framework.decorators import api_view

from .models import Product


class ProductInfo(BaseModel):
    article: int
    brand: str
    title: str


async def get_product_data_from_code(article):
    async with aiohttp.ClientSession() as session:
        async with session.get(
                f"https://basket-05.wb.ru/vol{str(article)[:3]}/part{str(article)[:5]}/{str(article)}/info/ru/card.json") as response:
            data = await response.json()
            brand = data.get("selling").get("brand_name")
            title = data.get("imt_name")
            return ProductInfo(article=article, brand=brand, title=title).dict()


async def get_product_data_from_file(articles):
    tasks = []
    for article in articles:
        task = asyncio.create_task(get_product_data_from_code(article))
        tasks.append(task)
    result = await asyncio.gather(*tasks)
    return result


@api_view(http_method_names=['POST'])
def post_article(request):
    if 'file' in request.FILES:
        file = request.FILES['file']
        df = pd.read_excel(file)
        articles = df.iloc[:, 0].tolist()
        try:
            data = asyncio.run(get_product_data_from_file(articles))
            return Response({'data': data}, status=200)
        except:
            return Response({'error': 'Check articles'}, status=400)
    elif 'article' in request.POST:
        article = request.POST['article']
        try:
            product = Product.objects.get(article=article)
            product_info = ProductInfo(article=product.article,
                                       brand=product.brand,
                                       title=product.title)
            return Response({'data': product_info.dict()}, status=200)
        except ObjectDoesNotExist:
            try:
                data = asyncio.run(get_product_data_from_code(article))
                Product.objects.create(**data)
                return Response({'data': data}, status=200)
            except:
                return Response({'error': 'Check article'}, status=400)
    return Response({'error': 'Invalid request'}, status=400)
