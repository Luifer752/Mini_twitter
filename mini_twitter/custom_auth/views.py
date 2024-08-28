from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth import login, logout
from .forms import CustomUserCreateForm, LoginForm
from users.models import Users
from django.views.generic import ListView, DetailView
from .models import CustomUser


class RegisterView(CreateView):
    form_class = CustomUserCreateForm
    success_url = '/posts/'
    template_name = 'registration.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        user = self.object
        Users.objects.get_or_create(user=user)
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


class UsersListView(ListView):
    model = CustomUser
    template_name = 'users/users_list.html'
    context_object_name = 'users'


class UserDetailView(DetailView):
    model = CustomUser
    template_name = 'users/user_details.html'
    context_object_name = 'user'
    # pk_url_kwarg = 'user_id'  may be useful

    # def get_object(self):
    #     return get_object_or_404(CustomUser, pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.get_object()
        context['current_user'] = self.request.user
        return context
