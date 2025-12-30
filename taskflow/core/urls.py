from django.urls import path
from .views import TaskListCreateView, TaskDetailView , RegisterView

urlpatterns = [
    path('register/' ,RegisterView.as_view()),
    path('tasks/' ,TaskListCreateView.as_view()),
    path('tasks/<int:pk>/',TaskDetailView.as_view()),
]
   