from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .pagination import NewsPagination
from .utils import find_root_and_category

from .models import (ScientificTeam, Scientists, News, Provensiya, Dictionary, Contact, \
                     Slider, Text, UsefulSites, NewsCategory, AdminContact, Category)
from .sarializer import ScientificTeamSerializer, ScientistsSerializer, NewsSerializer, \
    ProvensiyaSerializer, DictionarySerializer, ContactSerializer, SliderSerializer, TextSerializer, \
    WordInputSerializer, UsefulSitesSerializer, NewsCategorySerializer, AdminContactSerializer, CategorySerializer


@api_view(['GET'])
def scientific_team_list(request):
    teams = ScientificTeam.objects.all()
    serializer = ScientificTeamSerializer(teams, many=True, context={'request': request})
    return Response(serializer.data)


@api_view(['GET'])
def scientific_team_detail(request, pk):
    try:
        team = ScientificTeam.objects.get(pk=pk)
    except ScientificTeam.DoesNotExist:
        return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = ScientificTeamSerializer(team, context={'request': request})
    return Response(serializer.data)


@api_view(['GET'])
def scientists_list(request):
    scientists = Scientists.objects.all()
    serializer = ScientistsSerializer(scientists, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def newscategory_list(request):
    categories = NewsCategory.objects.all()
    serializer = NewsCategorySerializer(categories, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def news_list(request):
    news = News.objects.all()
    paginator = NewsPagination()
    page = paginator.paginate_queryset(news, request)

    if page is not None:
        serializer = NewsSerializer(page, many=True, context={'request': request})
        return paginator.get_paginated_response(serializer.data)

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


@api_view(['GET'])
def admin_contact_list(request):
    if request.method == 'GET':
        contacts = AdminContact.objects.all()
        serializer = AdminContactSerializer(contacts, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def contact_list_create(request):
    if request.method == 'GET':
        contacts = Contact.objects.all()
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def contact_detail(request, pk):
    try:
        contact = Contact.objects.get(pk=pk)
    except Contact.DoesNotExist:
        return Response({'detail': 'Not found.'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ContactSerializer(contact)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ContactSerializer(contact, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        contact.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def slider_list(request):
    if request.method == 'GET':
        sliders = Slider.objects.all()
        serializer = SliderSerializer(sliders, many=True)
        for slider in serializer.data:
            slider['image'] = request.build_absolute_uri(slider['image'])
        return Response(serializer.data)


@api_view(['GET'])
def useful_sites_list(request):
    teams = UsefulSites.objects.all()
    serializer = UsefulSitesSerializer(teams, many=True, context={'request': request})
    return Response(serializer.data)


class TextListView(ListAPIView):
    queryset = Text.objects.all()
    serializer_class = TextSerializer


class WordRootAPIView(APIView):
    def post(self, request):
        serializer = WordInputSerializer(data=request.data)
        if serializer.is_valid():
            word = serializer.validated_data['word']
            root_word, suffix, category = find_root_and_category(word)

            result_data = {
                'soz_ildizi': root_word,
                'soz_turkumi': category if isinstance(category, str) else category.type if category else root_word
            }

            if suffix:  # Agar qo'shimcha mavjud bo'lsa, natijaga qo'shimchani qo'shamiz
                result_data['qo\'shimcha'] = suffix

            return Response(result_data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def category_soz_turkum(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

