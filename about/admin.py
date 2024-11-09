from django.contrib import admin
from .models import ScientificTeam, Scientists, News, Provensiya, Dictionary, Sentences, Contact, Slider, \
    Text, Addition, UsefulSites, NewsCategory

admin.site.register(ScientificTeam)


@admin.register(Scientists)
class ScientistsAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'description')


@admin.register(NewsCategory)
class NewsCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'category')


class SentencesInline(admin.TabularInline):
    model = Sentences
    extra = 1


class TextAdmin(admin.ModelAdmin):
    list_display = ('id', 'provensiya', 'text')
    search_fields = ['text']
    list_filter = ('provensiya',)


class ProvensiyaAdmin(admin.ModelAdmin):
    list_display = ('id', 'provensiya')


class DictionaryAdmin(admin.ModelAdmin):
    list_display = ('id', 'lexical', 'provensiya')
    search_fields = ('lexical', 'provensiya__provensiya')
    inlines = [SentencesInline]


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'comment', 'latitude', 'longitude')
    search_fields = ('name', 'phone',)
    list_filter = ('latitude', 'longitude')
    ordering = ('phone',)


@admin.register(UsefulSites)
class UsefulSitesAdmin(admin.ModelAdmin):
    list_display = ['title', 'link']


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')
    search_fields = ('title',)
    list_filter = ('title',)


# admin.site.register(NewsCategory, NewsCategoryAdmin)
admin.site.register(Text, TextAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Provensiya, ProvensiyaAdmin)
admin.site.register(Dictionary, DictionaryAdmin)
admin.site.register(Addition)
