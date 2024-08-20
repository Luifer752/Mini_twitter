from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth import login, logout
from .forms import CustomUserCreateForm, LoginForm
from users.models import Users

class RegisterView(CreateView):

    form_class = CustomUserCreateForm
    success_url = '/posts/'
    template_name = 'registration.html'

    def form_valid(self, form):
        response  = super().form_valid(form)
        user = self.object
        Users.objects.create(user=user)
        login(self.request, self.object)    # self.object is the one created in registration form
        return response


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            print("User logged in and redirected")
            return redirect('posts:posts_list')
    else:
        form = LoginForm()
    return render(request, 'login.html', context={'form': form})


def logout_view(request):
    logout(request)
    return redirect('custom_auth:login')
