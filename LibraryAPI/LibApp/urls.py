from django.conf.urls import url
from LibApp import views


from django.conf import settings

urlpatterns=[
    url(r'^genre$',views.genreApi),
    url(r'^genre/([0-9]+)$',views.genreApi),

     url(r'^book$',views.bookApi),
    url(r'^book/([0-9]+)$',views.bookApi),
] 