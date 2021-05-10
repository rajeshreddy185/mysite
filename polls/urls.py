from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('question/', views.question, name='question'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/votes/', views.votes, name='votes'),
    path('<int:question_id>/results/', views.results, name='results'),
]