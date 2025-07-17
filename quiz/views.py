from django.shortcuts import render
# quiz/views.py
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods # นำเข้า decorator นี้
import json # นำเข้าไลบรารี json
from django.views.decorators.csrf import csrf_exempt

def question_detail(request):
    data = {
        "id": 1,
        "text": "ประเทศไทยมีกี่จังหวัด",
        "choices": [50, 68, 72, 77]
    }
    return JsonResponse(data)
@csrf_exempt
@require_http_methods(["POST"]) 
def create_question(request):
    
    response_data = {
        "id": 9,
        "text": "ภาษาโปรแกรมใดได้รับความนิยมสูงสุดในวิทยาการข้อมูล",
        "choices": ["C", "C++", "C#", "Python", "R", "Julia"]
    }
    return JsonResponse(response_data, status=201) # 201 Created status