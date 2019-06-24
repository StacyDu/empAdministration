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
    DevelopersTechnologies)
from django.views import View


class DeveloperCreateView(FormView):

    template_name = 'generic_form.html'
    form_class = DevelopersForm
    model = Developers
    success_url = '/show_developers'

    def form_valid(self, form):
        developer = form.save(commit=False)
        developer.save()
        for technology in form.cleaned_data.get('technology'):
            developertechnology = DevelopersTechnologies.objects.create(developer=developer, technology_name=technology)
            developertechnology.save()
        return redirect('show-developers-view')


class ShowDevelopersView(ListView):
    model = Developers
    template_name = 'generic_list.html'


class HomeView(View):
    def get(self, request):
        return render_to_response('main.html')


class TechnologyCreateView(CreateView):

    template_name = 'generic_form.html'
    model = Technologies
    form_class = TechnologiesForm
    success_url = '/show_technologies'


class ShowTechnologiesView(ListView):
    model = Technologies
    template_name = 'generic_list.html'
