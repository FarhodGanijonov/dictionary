from ckeditor.fields import RichTextField
from django.contrib import admin
from .models import ScientificTeam, Scientists, News, Provensiya, Dictionary, Sentences, Contact, Slider, \
    Text, Category, Addition, UsefulSites
from ckeditor.widgets import CKEditorWidget

admin.site.register(ScientificTeam)


@admin.register(Scientists)
class ScientistsAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'description')


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')


class SentencesInline(admin.TabularInline):
    model = Sentences
    extra = 1


class TextAdmin(admin.ModelAdmin):
    list_display = ('id', 'provensiya', 'text')  # Ko'rinishda maydonlarni chiqarish
    search_fields = ['text']  # Admin interfeysda qidiriladigan maydonlar
    list_filter = ('provensiya',)


class ProvensiyaAdmin(admin.ModelAdmin):
    list_display = ('id', 'provensiya')


class DictionaryAdmin(admin.ModelAdmin):
    formfield_overrides = {
        RichTextField: {'widget': CKEditorWidget()},
    }
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
    list_display = ['title', 'link']  # Admin interfeysida qaysi ustunlarni ko'rsatishni belgilaymiz


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')  # Adjust fields as needed
    search_fields = ('title',)  # Allows searching by title
    list_filter = ('title',)  # Allows filtering by title


# Add filters on the sidebar for the list view

admin.site.register(Text, TextAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Provensiya, ProvensiyaAdmin)
admin.site.register(Dictionary, DictionaryAdmin)
admin.site.register(Category)
admin.site.register(Addition)
