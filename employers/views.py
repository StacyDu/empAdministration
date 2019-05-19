from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from employers.models import (
    REFERENCE_CHOICES,
    Developers,
    Technologies,
)
from django.views import View

# View for the developers form


@method_decorator(csrf_exempt, name='dispatch')
class CreateDeveloperView(View):
    def get(self, request):
        options = dict(REFERENCE_CHOICES)
        context = {
            'options': options
        }
        return render_to_response("developers_form.html", context)

    def post(self, request):
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        middle_name = request.POST['middle_name']
        email = request.POST['email']
        salary = request.POST['salary']
        date_hired = request.POST['date_hired']
        notes = request.POST['notes']
        reference = request.POST['reference']
        developer = Developers.objects.create(
            first_name=first_name,
            last_name = last_name,
            middle_name = middle_name,
            email = email,
            salary = salary,
            date_hired = date_hired,
            notes = notes,
            reference = reference,
        )
        return HttpResponse('DONE')


class HomeView(View):
    def get(self, request):
        return render_to_response('main.html')


@method_decorator(csrf_exempt, name='dispatch')
class TechnologyView(View):
    def get(self, request):
        return render_to_response('add_technology.html')

    def post(self, request):
        technology_name = request.POST['technology_name']
        technology = Technologies.objects.create(
            technology_name=technology_name
        )
        return redirect('show-technologies-view')


class ShowTechnologyView(View):
    def get(self, request):
        technologies = Technologies.objects.all()
        return render_to_response('show_technologies.html', {'technologies': technologies})
