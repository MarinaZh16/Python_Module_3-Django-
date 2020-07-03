from django.contrib.auth import login, authenticate, logout as logout_
from django.shortcuts import redirect, render
from users.forms import UserForm, EmailConfirmForm
from users.models import User
from django.views.generic.edit import FormView, UpdateView
from django.views.generic import TemplateView
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect


class RegisterView(FormView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy('profile')
    template_name = 'users/user_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.set_password(form.cleaned_data['password'])
        self.object.save()
        login(self.request, self.object)
        return super(RegisterView, self).form_valid(form)


def logout(request):
    logout_(request)
    return redirect('/')


class UserUpdate(UpdateView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy('profile')


class ProfilePage(TemplateView):
    template_name = "registration/profile.html"

    def get(self, request, *args, **kwargs):
        confirm_form = None
        if not self.request.user.email_confirmed:
            confirm_form = EmailConfirmForm()
        return render(request, self.template_name, {'confirm_form': confirm_form})

    def post(self, request, *args, **kwargs):
        if self.request.POST.get('action') == 'confirm':
            form = EmailConfirmForm(self.request.POST)
            if form.is_valid():
                if form.cleaned_data.get('token') == self.request.user.token:
                    self.request.user.email_confirmed = True
                    self.request.user.save()
            else:
                return render(self.request, self.template_name, {'confirm_form': form})
        return HttpResponseRedirect(reverse('profile'))
