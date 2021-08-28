from django.urls import path
from django.urls.resolvers import URLPattern

from . import views

urlpatterns=[
    path('', views.youtubers, name="youtubers"),
    path('<int:id>', views.youtubers_detail, name="youtubers_detail"),
    path('search', views.search, name="search"),

]

