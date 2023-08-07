
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from qrcode.models import *

# Create your views here.

def home(request):
	return render(request, 'index.html')


@csrf_exempt
def check_num(request, num):
    if request.method == "POST":

        if Student.objects.filter(number = num).exists():
            std_obj = Student.objects.get(number = num)
            name = std_obj.name
            attemps = std_obj.attemps
            std_obj.attemps += 1
            std_obj.save()
        else:
        	name = "000"

        return JsonResponse({ 'result' : name, 'attemps' : attemps })