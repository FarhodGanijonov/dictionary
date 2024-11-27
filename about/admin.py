from django.contrib import admin

from .models import ScientificTeam, Scientists, News, Provensiya, Contact, Slider, \
    Text, Addition, UsefulSites, NewsCategory, AdminContact, Category, AuthorText, TextField

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

@admin.register(AuthorText)
class AuthorTextAdmin(admin.ModelAdmin):
    list_display = ('id', 'author')
    search_fields = ('author',)


class TextFieldInline(admin.TabularInline):
    model = TextField
    fields = ['text']
    extra = 1


@admin.register(Text)
class TextAdmin(admin.ModelAdmin):
    list_display = ('id', 'word', 'provensiya', 'author',)
    search_fields = ['word']
    list_filter = ('provensiya',)
    inlines = [TextFieldInline]


class ProvensiyaAdmin(admin.ModelAdmin):
    list_display = ('id', 'provensiya')

@admin.register(AdminContact)
class AdminContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone', 'email', 'location', 'telegram', 'instagram', 'youtube',)


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


@admin.register(Category)
class Category_soz_turkum(admin.ModelAdmin):
    list_display = ('id', 'type')
    search_fields = ('type',)


admin.site.register(Contact, ContactAdmin)
admin.site.register(Provensiya, ProvensiyaAdmin)
admin.site.register(Addition)
