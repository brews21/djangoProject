from django.shortcuts import render
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, DeleteView, UpdateView
from django.http import HttpResponse
from . import models
from django.urls import reverse_lazy

# Create your views here.
class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['inject_me'] = 'basic injection'
        return context


class SchoolListView(ListView):
    context_object_name = 'school' # List View will return schools_list by default
    model = models.School


class SchoolDetailView(DetailView):
    context_object_name = 'school_detail' # Detail View will return schools by default
    model = models.School
    template_name = 'basic_app/school_detail.html'


class SchoolCreateView(CreateView):
    fields = ('name','principle','location')
    model = models.School


class SchoolUpdateView(UpdateView):
    fields = ('name','principle')
    model = models.School


class SchoolDeleteView(DeleteView):
    model = models.School
    success_url = reverse_lazy("basic_app:list")
