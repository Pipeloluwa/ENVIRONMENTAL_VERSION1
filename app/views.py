from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from datetime import datetime, timedelta


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

import random
# Create your views here.
# from views_routers.index import index
json_data= {}


def index(request):
    return render(request, 'model_dashboard.html')

def add_model(request):
    return render(request, 'model_add.html')

def view_model(request):
    global json_data
    if request.method == "POST":
        # print(request.body)
        json_data= json.loads(request.body)
        # print(json_data)
        return redirect ('view')
    
    print(json_data)
    return render(request, 'model_view.html', {'json_data': json_data})
    
