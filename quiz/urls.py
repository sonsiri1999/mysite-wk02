# quiz/urls.py
from django.urls import path
from . import views # นำเข้า views จากไฟล์ views.py ในโฟลเดอร์เดียวกัน

urlpatterns = [
    # URL สำหรับ GET request ที่ /quiz/question/
    path('question/', views.question_detail, name='question_detail'),
    # URL สำหรับ POST request ที่ /quiz/question/create/
    path('question/create/', views.create_question, name='create_question'),
]
