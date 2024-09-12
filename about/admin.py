from ckeditor.fields import RichTextField
from django.contrib import admin

from .models import ScientificTeam, Scientists, Expressions, News, Provensiya, Dictionary, Contact, Slider, \
    Text, UsefulSites
from ckeditor.widgets import CKEditorWidget

@admin.register(ScientificTeam)
class ScientificTeamAdmin(admin.ModelAdmin):
    list_display = (
        'fullname', 'workplace', 'position', 'academic_level',
        'phone', 'email', 'admission_day', 'image_preview'
    )
    search_fields = (
        'fullname', 'workplace', 'position', 'academic_level',
        'phone', 'email'
    )
    list_filter = ('workplace', 'position', 'academic_level')
    readonly_fields = ('admission_day',)  # Optional: make 'admission_day' read-only if desired
    ordering = ['fullname']

    def image_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" style="width: 100px; height: auto;" />'
        return 'No Image'
    image_preview.allow_tags = True
    image_preview.short_description = 'Image Preview'

@admin.register(UsefulSites)
class UsefulSitesAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'link')
    search_fields = ('title',)
    list_filter = ('title',)


@admin.register(Scientists)
class ScientistsAdmin(admin.ModelAdmin):
    list_display = ('fullname', 'description')


@admin.register(Expressions)
class ExpressionsAdmin(admin.ModelAdmin):
    list_display = ('express',)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')



class TextAdmin(admin.ModelAdmin):
    list_display = ('id', 'provensiya', 'text')  # Fields to display in the list view
    search_fields = ('text',)  # Fields to be searchable in the admin interface
    list_filter = ('provensiya',)

class ProvensiyaAdmin(admin.ModelAdmin):
    list_display = ('id', 'provensiya')


class DictionaryAdmin(admin.ModelAdmin):
    formfield_overrides = {
        RichTextField: {'widget': CKEditorWidget()},
    }
    list_display = ('id', 'lexical', 'provensiya')
    search_fields = ('lexical', 'provensiya__provensiya')


class ContactAdmin(admin.ModelAdmin):
    list_display = ('phone', 'email', 'instagram', 'telegram', 'facebook', 'latitude', 'longitude')
    search_fields = ('phone', 'email', 'instagram', 'telegram', 'facebook')
    list_filter = ('latitude', 'longitude')
    ordering = ('phone',)


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
