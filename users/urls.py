from django.conf.urls import url
from django.urls import include, path

from users.views import CreateUserAPIView, authenticate_user, UserRetrieveUpdateAPIView
from . import views

urlpatterns = [
    #path('', views.UserListView.as_view()),
    url(r'^create/$', CreateUserAPIView.as_view()),
    url(r'obtain_token/$', authenticate_user),
    url(r'^update/$', UserRetrieveUpdateAPIView.as_view()),
]