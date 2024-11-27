
from rest_framework import serializers
from .models import ScientificTeam, Scientists, News, Provensiya, Contact, Slider, \
    Text, UsefulSites, NewsCategory, AdminContact, Category, AuthorText, TextField


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
        fields = ['id', 'title', 'description', 'image', 'category', ]

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image and request:
            return request.build_absolute_uri(obj.image.url)
        return None


class ProvensiyaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provensiya
        fields = ['id', 'provensiya']


class AdminContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminContact
        fields = ['phone', 'email', 'location', 'telegram', 'instagram', 'youtube', ]


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'name', 'phone', 'comment', 'latitude', 'longitude']


class SliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slider
        fields = ['id', 'title', 'image']


class AuthorTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorText
        fields = ['id', 'author']


class TextSerializer(serializers.ModelSerializer):
    provensiya = ProvensiyaSerializer()
    author = AuthorTextSerializer()

    class Meta:
        model = Text
        fields = ['id', 'word', 'text', 'provensiya', 'author']


class UsefulSitesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsefulSites
        fields = ['id', 'title', 'image', 'link']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'type']


class TextFieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextField
        fields = ['id', 'text']