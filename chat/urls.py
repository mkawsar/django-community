from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', ChatIndex.as_view(), name='chat-index'),
    path('conversation', broadcast),
    path('conversations/', conversations),
    re_path(r'^conversations/(?P<id>[-\w]+)/delivered$', delivered),
]
