from ckeditor.fields import RichTextField
from django.contrib import admin

from .models import ScientificTeam, Scientists, Expressions, News, Provensiya, Dictionary, Sentences
from ckeditor.widgets import CKEditorWidget

admin.site.register(ScientificTeam)


@admin.register(Scientists)
class ScientistsAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'description')


@admin.register(Expressions)
class ExpressionsAdmin(admin.ModelAdmin):
    list_display = ('express',)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')


class SentencesInline(admin.TabularInline):
    model = Sentences
    extra = 1

class ProvensiyaAdmin(admin.ModelAdmin):
    list_display = ('id', 'provensiya')

class DictionaryAdmin(admin.ModelAdmin):
    formfield_overrides = {
        RichTextField: {'widget': CKEditorWidget()},
    }
    list_display = ('id', 'lexical', 'provensiya')
    search_fields = ('lexical', 'provensiya__provensiya')
    inlines = [SentencesInline]

admin.site.register(Provensiya, ProvensiyaAdmin)
admin.site.register(Dictionary, DictionaryAdmin)
