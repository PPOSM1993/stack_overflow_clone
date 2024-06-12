from django.urls import path
from . import views

app_name = 'stack_overflow'

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.HomeView, name='home'),
    path('about/', views.AboutView, name='about'),
    path('questions/', views.QuestionListView.as_view(), name="question-lists"),
    path('questions/create', views.QuestionCreateView.as_view(), name="question-create"),
    path('questions/<int:pk>/', views.QuestionDetailView.as_view(), name="question-detail"),
]


