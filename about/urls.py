from django.urls import path

from .filters import similar_news
from .views import scientific_team_list, scientific_team_detail, scientists_list, news_list, \
    dictionary_list, provensiya_list, \
    news_detail, contact_list_create, contact_detail, slider_list, TextListView, WordRootAPIView, useful_sites_list, \
    newscategory_list, admin_contact_list, category_soz_turkum

urlpatterns = [
    path('scientific-team/', scientific_team_list),
    path('scientific-team/<int:pk>', scientific_team_detail),
    path('scientists/', scientists_list),
    path('news/', news_list),
    path('news/<int:pk>/', news_detail),
    path('news/<int:pk>/similar/', similar_news),
    path('provensiya/', provensiya_list),
    path('dictionary/', dictionary_list,),
    path('contacts/', contact_list_create),
    path('contacts/<int:pk>/', contact_detail),
    path('admin-contacts/', admin_contact_list),
    path('sliders/', slider_list),
    path('text/', TextListView.as_view()),
    path('api/word-root/', WordRootAPIView.as_view()),
    path('useful-sites/', useful_sites_list),
    path('news_category/', newscategory_list),
    path('category_soz_turkum/', category_soz_turkum),

]

