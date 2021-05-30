from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, ArchiveIndexView, TemplateView, ListView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.db.models import Q
from django.contrib.auth.decorators import login_required

from .models import Bb, Rubric
from .forms import BbForm, SignUpForm

class BbIndexView(ArchiveIndexView):
    model = Bb
    date_field = "published"
    date_list_period = "year"
    template_name = "bboard/index.html"
    context_object_name = "bbs"
    allow_empty = True

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context

def by_rubric(request, rubric_id):
    bbs=Bb.objects.filter(rubric=rubric_id)
    rubrics=Rubric.objects.all()
    current_rubric=Rubric.objects.get(pk=rubric_id)
    context={"bbs":bbs, "rubrics": rubrics, "current_rubric": current_rubric}
    return render(request, 'bboard/by_rubric.html', context)


class BbCreateView(CreateView):
    template_name='bboard/bb_create.html'
    form_class=BbForm
    model = Bb
    success_url=reverse_lazy('main')

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context
    
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.request = self.request
        return form
    
    def get_initial(self):
        if self.request.user.username!="":
            initial = super(BbCreateView, self).get_initial()
            initial['author'] = self.request.user.username
            initial['phone'] = self.request.user.phone
            return initial
    
class BbDetailView(DetailView):
    model = Bb

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['username'] = self.request.user.username
        context['rubrics'] = Rubric.objects.all()
        return context

class BbEditView(UpdateView):
    model = Bb
    success_url = '/'
    template_name = 'bboard/bb_update.html'
    form_class = BbForm

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context

class BbDeleteView(DeleteView):
    model = Bb
    success_url = '/'
    template_name = 'bboard/bb_delete.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context

class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context

def profile(request):
    bbs = Bb.objects.filter(author=request.user.username)
    context = {'bbs':bbs}
    return render(request, "bboard/profile.html", context)

class SearchResultsView(ListView):
    model = Bb
    template_name = 'bboard/search_results.html'
    
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['rubrics'] = Rubric.objects.all()
        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list=Bb.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )
        return object_list