from django.urls import path
from .views import CustomLoginView, RegisterView
from django.contrib.auth.views import LoginView, LogoutView


app_name='users'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='catalog:product_list'), name='logout'),
    # path('logout/', LogoutView.as_view(next_page='catalog:product_list'), name='logout'),
]
