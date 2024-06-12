from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView, CreateView
from .models import *
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.urls import reverse, reverse_lazy

from .forms import CommentForm


# Create your views here.


def index(request):
    return render(request, 'index.html')


def HomeView(request):
    return render(request, 'home.html')

def AboutView(request):
    return render(request, 'about.html')

#CRUD Functions
class QuestionListView(ListView):
    model = Question
    context_object_name = 'questions'
    ordering = ['-date_created']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_input = self.request.GET.get('search-area') or ""
        if search_input:
            context['questions'] = context['questions'].filter(title__icontains = search_input)
            context['search_input'] = search_input
        return context

class QuestionDetailView(DetailView):
    model = Question

    def get_context_data(self, *args, **kwargs):
        context = super(QuestionDetailView, self).get_context_data()
        something = get_object_or_404(Question, id=self.kwargs['pk'])
        total_likes = something.total_likes()
        liked = False
        if something.likes.filter(id=self.request.user.id).exists():
            liked = True

        context['total_likes'] = total_likes
        context['liked'] = liked
        return context
    

class QuestionCreateView(LoginRequiredMixin, CreateView):
    model = Question
    fields = ['title', 'content']
    context_object_name =  'question'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)