from users import views
from django.urls import path

urlpatterns = [
    path('users/', views.users),
    path('users/<int:pk>/', views.user_detail),
]
