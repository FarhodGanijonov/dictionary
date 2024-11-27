from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import News
from .serializers import NewsSerializer


@api_view(['GET'])
def similar_news(request, pk):
    news_item = News.objects.get(pk=pk)

    similar_news = News.objects.filter(category=news_item.category).exclude(pk=news_item.pk)[:5]
    similar_news_serializer = NewsSerializer(similar_news, many=True, context={'request': request})

    return Response({"similar_news": similar_news_serializer.data})
