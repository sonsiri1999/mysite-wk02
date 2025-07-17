# quiz/views.py
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt # นำเข้า decorator นี้เพื่อยกเว้น CSRF

# View สำหรับ GET request ที่ /quiz/question/
def question_detail(request):
    data = {
        "id": 1,
        "text": "ประเทศไทยมีกี่จังหวัด",
        "choices": [50, 68, 72, 77]
    }
    return JsonResponse(data)

# View สำหรับ POST request ที่ /quiz/question/create/
@csrf_exempt # ใช้ decorator นี้เพื่อยกเว้นการตรวจสอบ CSRF สำหรับ API endpoint นี้
@require_http_methods(["POST"]) # กำหนดให้ View นี้รับเฉพาะ POST request เท่านั้น
def create_question(request):

    response_data = {
        "id": 9,
        "text": "ภาษาโปรแกรมใดได้รับความนิยมสูงสุดในวิทยาการข้อมูล",
        "choices": ["C", "C++", "C#", "Python", "R", "Julia"]
    }

    return JsonResponse(response_data, status= 'Success')
