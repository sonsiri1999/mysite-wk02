
from django.urls import path
from . import views

urlpatterns = [
    path('question/', views.question_detail, name='question_detail'),
    path('question/create/', views.create_question, name='create_question'), 
]