from django.urls import path
from . import views

urlpatterns = [
    path('test-logs/', views.test_logs, name='test_logs'),
]