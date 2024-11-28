from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .pagination import NewsPagination
from django.db.models import Q, Count
from .models import (ScientificTeam, Scientists, News, Provensiya, Contact, \
                     Slider, UsefulSites, NewsCategory, AdminContact, Category, AuthorText, Text, TextField, )
from .serializers import ScientificTeamSerializer, ScientistsSerializer, NewsSerializer, \
    ProvensiyaSerializer, ContactSerializer, SliderSerializer, TextSerializer, \
    UsefulSitesSerializer, NewsCategorySerializer, AdminContactSerializer, CategorySerializer, \
    AuthorTextSerializer, TextFieldSerializer


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


@api_view(['GET'])
def author_text(request):
    if request.method == 'GET':
        categories = AuthorText.objects.all()
        serializer = AuthorTextSerializer(categories, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def text_list_view(request):
    texts = Text.objects.all()
    serializer = TextSerializer(texts, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def category_soz_turkum(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


class TextSearchAPIView(APIView):
    def get(self, request):
        query = request.GET.get("word", "").strip().lower()
        search_type = request.GET.get("type", "lemma").lower()

        if not query:
            return Response({"error": "So‘z kiritilmadi!"}, status=400)

        if search_type == "lemma":
            text_obj = Text.objects.filter(word__iexact=query).first()
            if not text_obj:
                return Response({"error": f"So‘z '{query}' topilmadi."}, status=404)

            text_fields = TextField.objects.filter(
                Q(text_model=text_obj) &
                Q(text__iregex=fr'\b{query}\b')
            )

            if not text_fields.exists():
                return Response({"message": f"So‘z '{query}' ishtirok etgan gaplar topilmadi."}, status=404)

            serializer = TextFieldSerializer(text_fields, many=True)
            return Response(serializer.data)

        elif search_type == "token":
            text_fields = TextField.objects.filter(
                Q(text__icontains=query)
            )

            if not text_fields.exists():
                return Response({"error": f"So‘z '{query}' ishtirok etgan gaplar topilmadi."}, status=404)

            serializer = TextFieldSerializer(text_fields, many=True)

            return Response(serializer.data)

        return Response({"message": "Noto‘g‘ri qidiruv turi."}, status=400)


class ProvensiyaWordStatsAPIView(APIView):
    def get(self, request):
        provensiya_data = (
            Text.objects.values("provensiya__provensiya")
            .annotate(word_count=Count("word"))
            .order_by("-word_count")
        )

        result = [
            {"provensiya": data["provensiya__provensiya"], "word_count": data["word_count"]}
            for data in provensiya_data
        ]

        return Response(result)
