from django.urls import path
from users.views import RegisterView, VerifyEmailView, UsersView, UserChangeActiveUpdateView
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'users'

urlpatterns = [
    path('login/', LoginView.as_view(template_name="users/login.html"), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('register/', RegisterView.as_view(), name="register"),
    path('verify_email/<str:uid>/<str:token>/', VerifyEmailView.as_view(), name='verify_email'),
    path('users/', UsersView.as_view(), name='users_list'),
    path('user_change_active/<int:pk>/', UserChangeActiveUpdateView.as_view(), name='user_change_active'),
]
