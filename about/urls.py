from django.urls import path
from .views import scientific_team_list, scientists_list, expressions_list, news_list, dictionary_list, provensiya_list, \
    news_detail

urlpatterns = [
    path('scientific-team/', scientific_team_list),
    path('scientists/', scientists_list),
    path('expressions/', expressions_list),
    path('news/', news_list),
    path('news/<int:pk>/', news_detail),
    path('provensiya/', provensiya_list),
    path('dictionary/', dictionary_list,),
]
