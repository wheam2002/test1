from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .form import RegisterForm
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt 


#首頁
@csrf_exempt
def get_my_name(request):
    try:
        if request.method == 'GET':
            name = 'My name is John Cena !'
    except:
        name = 'Error'        
        
    return JsonResponse({'name':name})
     