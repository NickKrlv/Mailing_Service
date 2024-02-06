import random
import string
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import CreateView, UpdateView
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.urls import reverse_lazy, reverse
from users.forms import UserSignupForm, UserProfileForm
from users.models import User

User = get_user_model()


class RegisterView(CreateView):
    model = User
    form_class = UserSignupForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/register.html'

    def form_valid(self, form):
        new_user = form.save()
        token = ''.join(random.choices(string.ascii_letters + string.digits, k=50))
        new_user.email_token = token
        new_user.save()
        current_site = get_current_site(self.request)
        mail_subject = 'Подтвердите ваш аккаунт'
        message = (
            f'Поздравляем, Вы зарегистрировались на нашем портале!\n'
            f'Для завершения регистрации и подтверждения вашей электронной почты, '
            f'пожалуйста, кликните по следующей ссылке:\n'
            f'http://{current_site.domain}{reverse("users:verify_email", kwargs={"uid": new_user.pk, "token": token})}'
        )
        send_mail(
            subject=mail_subject,
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[new_user.email]
        )
        return super().form_valid(form)


class VerifyEmailView(View):
    def get(self, request, uid, token):
        user = get_object_or_404(User, pk=uid, email_token=token)
        user.is_active = True
        user.save()
        return render(request, 'users/registration_success.html')


class ProfileView(LoginRequiredMixin, View):
    model = User
    form_class = UserProfileForm
    template_name = 'users/profile.html'

    def get(self, request):
        return render(request, self.template_name, {'user': request.user})


class ProfileEditView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')
    template_name = 'users/profile_edit.html'

    def get_object(self, queryset=None):
        if self.request.user.is_authenticated:
            return self.request.user
        return None

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('users:profile')


class UsersView(LoginRequiredMixin, PermissionRequiredMixin, View):
    model = User
    permission_required = 'users.view_user'
    template_name = 'users/users_list.html'

    def get(self, request):
        users = User.objects.all()
        return render(request, self.template_name, {'users': users})


@permission_required('users.set_active')
def toggle_user_activity(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    user.is_active = not user.is_active
    user.save()
    return redirect('users:users_list')
