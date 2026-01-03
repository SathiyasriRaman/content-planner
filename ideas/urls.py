from django.urls import path
from .views import home, list_ideas, create_idea, update_idea, delete_idea

urlpatterns = [
    path('', home),
    path('ideas/', list_ideas),
    path('ideas/create/', create_idea),
    path('ideas/update/<int:pk>/', update_idea),
    path('ideas/delete/<int:pk>/', delete_idea),
]
