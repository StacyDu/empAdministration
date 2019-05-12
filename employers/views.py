from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from employers.models import REFERENCE_CHOICES

# Create your views here.


@csrf_exempt
def hello(request):
    if request.method == 'GET':
        options = dict(REFERENCE_CHOICES)
        context = {
            'options': options
        }
        return render_to_response("main.html", context)
    else:
        context = {
            'request': request.method
        }
        return render_to_response("main.html", context)
