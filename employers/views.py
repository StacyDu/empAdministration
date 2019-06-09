from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import (
    CreateView,
    FormView,
    ListView,
)

from employers.forms import (
    TechnologiesForm,
    DevelopersForm,
)
from employers.models import (
    REFERENCE_CHOICES,
    Developers,
    Technologies,
)
from django.views import View

# View for the developers form


# @method_decorator(csrf_exempt, name='dispatch')
# class CreateDeveloperView(View):
#     def get(self, request):
#         options = dict(REFERENCE_CHOICES)
#         context = {
#             'options': options
#         }
#         return render_to_response("developers_form.html", context)
#
#     def post(self, request):
#         first_name = request.POST['first_name']
#         last_name = request.POST['last_name']
#         middle_name = request.POST['middle_name']
#         email = request.POST['email']
#         salary = request.POST['salary']
#         date_hired = request.POST['date_hired']
#         notes = request.POST['notes']
#         reference = request.POST['reference']
#         developer = Developers.objects.create(
#             first_name=first_name,
#             last_name = last_name,
#             middle_name = middle_name,
#             email = email,
#             salary = salary,
#             date_hired = date_hired,
#             notes = notes,
#             reference = reference,
#         )
#         return HttpResponse('DONE')

class DevelopersCreateView(FormView):

    template_name = 'generic_form.html'
    form_class = DevelopersForm
    model = Developers


    # def form_valid(self, form):
    #     technology_name = form.cleaned_data['technology_name']
    #     developer = Developers.objects.create(
    #         first_name='first_name',
    #         last_name='last_name',
    #         middle_name='middle_name',
    #         email='email',
    #         salary='salary',
    #         date_hired='date_hired',
    #         notes='notes',
    #         reference='reference',
    #     )
    #     return redirect('show-developers-view')


class HomeView(View):
    def get(self, request):
        return render_to_response('main.html')


# Historical data - to be deleted
# @method_decorator(csrf_exempt, name='dispatch')
# class TechnologyView(View):
#     def get(self, request):
#         return render_to_response('generic_form.html')
#
#     def post(self, request):
#         technology_name = request.POST['technology_name']
#         technology = Technologies.objects.create(
#             technology_name=technology_name
#         )
#         return redirect('show-technologies-view')


class TechnologiesCreateView(CreateView):

    template_name = 'generic_form.html'
    model = Technologies
    form_class = TechnologiesForm
    success_url = '/show_technologies'

    # def form_valid(self, form):
    #     technology_name = form.cleaned_data['technology_name']
    #     technology = Technologies.objects.create(
    #         technology_name=technology_name
    #     )
    #     return redirect('show-technologies-view')


class ShowTechnologyView(ListView):
    model = Technologies
    template_name = 'show_technologies.html'
