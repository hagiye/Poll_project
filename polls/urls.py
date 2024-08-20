from django.urls import path
from . import views

app_name = 'polls'  # Ensure you have this line to namespace your app

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('questions/<int:pk>/', views.DetailView.as_view(), name='detail'),  # Detail view for Question
    path('questions/<int:pk>/results/', views.ResultsView.as_view(), name='results'),  # Results view
    path('questions/<int:question_id>/vote/', views.vote, name='vote'),  # Vote view
]