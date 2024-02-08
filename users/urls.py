from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from users.views import RegisterView, VerifyEmailView, UsersView, toggle_user_activity

app_name = 'users'

urlpatterns = [
    path('login/', LoginView.as_view(template_name="users/login.html"), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('register/', RegisterView.as_view(), name="register"),
    path('verify_email/<str:uid>/<str:token>/', VerifyEmailView.as_view(), name='verify_email'),
    path('users/', UsersView.as_view(), name='users_list'),
    path('toggle_user_activity/<int:user_id>/', toggle_user_activity, name='toggle_user_activity'),
]
