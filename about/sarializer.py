import re
from html import unescape

from django.utils.html import strip_tags
from rest_framework import serializers
from .models import ScientificTeam, Scientists, News, Provensiya, Dictionary, Sentences, Contact, Slider, \
    Text, UsefulSites, NewsCategory, AdminContact


class ScientificTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScientificTeam
        fields = ['id', 'fullname', 'workplace', 'position', 'academic_level', 'phone', 'email', 'image',
                  'admission_day']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        request = self.context.get('request')
        if instance.image and request:
            representation['image'] = request.build_absolute_uri(instance.image.url)
        return representation


class ScientistsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scientists
        fields = ['fullname', 'description']


class NewsCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsCategory
        fields = ['id', 'name']


class NewsSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()
    category = NewsCategorySerializer()

    class Meta:
        model = News
        fields = ['id', 'title', 'description', 'image', 'category']

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image and request:
            return request.build_absolute_uri(obj.image.url)
        return None


class SentencesSerializer(serializers.ModelSerializer):
    sentence = serializers.SerializerMethodField()

    class Meta:
        model = Sentences
        fields = ['id', 'sentence']

    def get_sentence(self, obj):
        # 1. HTML kodlangan maxsus belgilarni dekodlash
        cleaned_sentence = unescape(obj.sentence)

        # 2. HTML teglarini olib tashlash
        cleaned_sentence = strip_tags(cleaned_sentence)

        # 3. Yangi qatorlar va ortiqcha bo'sh joylarni tozalash
        cleaned_sentence = re.sub(r'\s+', ' ', cleaned_sentence).strip()

        return cleaned_sentence


class ProvensiyaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provensiya
        fields = ['id', 'provensiya']


class DictionarySerializer(serializers.ModelSerializer):
    provensiya = ProvensiyaSerializer()
    senten = SentencesSerializer(many=True, read_only=True)

    class Meta:
        model = Dictionary
        fields = ['id', 'grammatical', 'lexical', 'comment', 'provensiya', 'senten']

    def to_representation(self, instance):
        representation = super().to_representation(instance)

        representation['grammatical'] = self.clean_html(representation['grammatical'])
        representation['comment'] = self.clean_html(representation['comment'])

        return representation

    def clean_html(self, value):
        cleaned_value = unescape(value)

        cleaned_value = strip_tags(cleaned_value)

        cleaned_value = re.sub(r'\s+', ' ', cleaned_value).strip()

        return cleaned_value


class AdminContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminContact
        fields = ['phone', 'email', 'location']


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'name', 'phone', 'comment', 'latitude', 'longitude']


class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = ['id', 'title', 'image']


class TextSerializer(serializers.ModelSerializer):
    provensiya = ProvensiyaSerializer()

    class Meta:
        model = Text
        fields = ['id', 'text', 'provensiya']


class WordInputSerializer(serializers.Serializer):
    word = serializers.CharField(max_length=100)


class WordResultSerializer(serializers.Serializer):
    soz_ildizi = serializers.CharField(max_length=200)
    qoshimcha = serializers.CharField(max_length=200, required=False, allow_blank=True)
    soz_turkumi = serializers.CharField(max_length=200, required=False, allow_blank=True)


class UsefulSitesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsefulSites
        fields = ['id', 'title', 'image', 'link']
