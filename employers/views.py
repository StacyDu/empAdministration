from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def show_number(request, number):
    answer = """
    <html><body><p>
    The answer is {}
    </p></body></html>
    """.format(number)
    return HttpResponse(answer)
