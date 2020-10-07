from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('create-poll', views.create_poll, name='create-poll'),
    path('display-polls', views.display_polls, name='display-polls'),
    path('single_poll', views.display_single_poll, name='single_poll'),
    path('vote_up', views.vote_up, name='vote_up'),
    path('user_polls', views.user_polls, name='user_polls'),
    path('poll_results', views.poll_results, name='poll_results'),
    path('username-validate', views.username_validate, name='username-validate'),
    path('delete-poll', views.delete_poll, name='delete-poll')
]
