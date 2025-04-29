from django.shortcuts import render

# Create your views here.

from django.http import JsonResponse

from django.http import HttpResponse

def student_list_text(request):
    students = [
        {"name": "أحمد", "age": 21, "major": "هندسة برمجيات"},
        {"name": "سارة", "age": 22, "major": "علوم حاسوب"},
        {"name": "محمد", "age": 20, "major": "ذكاء اصطناعي"},
        {"name": "ليلى", "age": 23, "major": "هندسة شبكات"},
        {"name": "خالد", "age": 24, "major": "أمن معلومات"},
    ]

    # نص منسق - كل طالب بسطر
    result = ""
    for student in students:
        result += f"{student['name']} - {student['age']} سنة - {student['major']}\n"

    return HttpResponse(result, content_type="text/plain; charset=utf-8")

