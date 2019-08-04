from django.conf.urls import url 
from . import views

urlpatterns = [
    url(r'^wall$', views.index),
    url(r'^post_message$', views.post_message),
    url(r'^post_comment$', views.post_comment),
    url(r'^delete_message$', views.delete_message),
    url(r'^wall/messages/(?P<id>\d+)/like$', views.like_mess),
    url(r'^wall/messages/(?P<id>\d+)/unlike$', views.unlike_mess),
]