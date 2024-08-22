from rest_framework import serializers
from .models import ScientificTeam, Scientists, Expressions, News, Provensiya, Dictionary


class ScientificTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScientificTeam
        fields = ['fullname', 'position', 'academic_level', 'phone', 'email', 'admission_day']


class ScientistsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scientists
        fields = ['fullname', 'description']


class ExpressionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expressions
        fields = ['express']


class NewsSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = News
        fields = ['id', 'title', 'description', 'image']

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image and request:
            return request.build_absolute_uri(obj.image.url)
        return None


class ProvensiyaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provensiya
        fields = ['id', 'provensiya']


class DictionarySerializer(serializers.ModelSerializer):
    provensiya = ProvensiyaSerializer()

    class Meta:
        model = Dictionary
        fields = ['id', 'grammatical', 'lexical', 'comment', 'sentences', 'provensiya']

