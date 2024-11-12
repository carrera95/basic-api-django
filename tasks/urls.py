from django.urls import path
from . import views

urlpatterns = [
    path("tasks/", views.TaskList.as_view(), name="task-list"),
    path("tasks/create/", views.TaskCreate.as_view(), name="task-create"),
    path("tasks/<int:pk>/", views.TaskDetail.as_view(), name="task-detail"),
    path("categories/", views.CategoryList.as_view(), name="category-list"),
    path("categories/create/", views.CategoryCreate.as_view(), name="category-create"),
]