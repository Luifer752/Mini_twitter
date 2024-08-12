from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Users
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm


class UsersListView(ListView):
    model = Users
    template_name = 'users/users_list.html'
    context_object_name = 'users'


class UserDetailView(DetailView):
    model = Users
    template_name = 'users/user_details.html'
    context_object_name = 'user'


@login_required
def edit_profile(request, user_id):
    user_profile = get_object_or_404(Users, user__id=user_id)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('users:user_details', pk=user_id)
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'users/edit_profile.html', {'form': form})







