from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import ScientificTeam, Scientists, Expressions, News, Provensiya, Dictionary
from .sarializer import ScientificTeamSerializer, ScientistsSerializer, ExpressionsSerializer, NewsSerializer, \
    ProvensiyaSerializer, DictionarySerializer


@api_view(['GET'])
def scientific_team_list(request):
    teams = ScientificTeam.objects.all()
    serializer = ScientificTeamSerializer(teams, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def scientists_list(request):
    scientists = Scientists.objects.all()
    serializer = ScientistsSerializer(scientists, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def expressions_list(request):
    expressions = Expressions.objects.all()
    serializer = ExpressionsSerializer(expressions, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def news_list(request):
    news = News.objects.all()
    serializer = NewsSerializer(news, many=True, context={'request': request})
    return Response(serializer.data)


@api_view(['GET'])
def news_detail(request, pk):
    try:
        news_item = News.objects.get(pk=pk)
    except News.DoesNotExist:
        return Response({'error': 'Not found'}, status=404)

    serializer = NewsSerializer(news_item, context={'request': request})
    return Response(serializer.data)


@api_view(['GET'])
def provensiya_list(request):
    provensiyas = Provensiya.objects.all()
    serializer = ProvensiyaSerializer(provensiyas, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def dictionary_list(request):
    dictionaries = Dictionary.objects.all()
    serializer = DictionarySerializer(dictionaries, many=True)
    return Response(serializer.data)