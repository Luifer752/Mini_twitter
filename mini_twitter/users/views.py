from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import UpdateView
from .models import Users
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import UserProfileForm


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = Users
    # form_class = UserProfileForm
    fields = ["bio", "profile_picture"]
    template_name = "users/edit_profile.html"
    success_url = '/posts/'

    def get_object(self, queryset=None):
        # return self.request.user #get current logged user
        return Users.objects.get(user=self.request.user)

    def form_valid(self, form):
        print("Sending form data...", form.cleaned_data)
        messages.success(self.request, 'Profile successfully updated!')
        return super().form_valid(form)

# class UsersListView(ListView):
#     model = Users
#     template_name = 'users/users_list.html'
#     context_object_name = 'users'
#
#
# class UserDetailView(DetailView):
#     model = Users
#     template_name = 'users/user_details.html'
#     context_object_name = 'user'
#
#     # def get_object(self):
#     #     user_id = self.kwargs.get("user_id")
#     #     return get_object_or_404(Users, user__id=user_id)
#
#     # def get_queryset(self):
#     #     queryset = Users.objects.select_related('user').all()
#     #     queryset = queryset.annotate(
#     #         username=F('user__username'),
#     #         email=F('user__email')
#     #     )
#     #     return queryset
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['users'] = Users.objects.select_related('user').get(pk=self.kwargs['user_id'])
#         return context


# @login_required
# def edit_profile(request, user_id):
#     user_profile = get_object_or_404(CustomUser, user__id=user_id)
#
#     if request.method == 'POST':
#         form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
#         if form.is_valid():
#             form.save()
#             update_session_auth_hash(request, user_profile.user)
#             return redirect('custom_auth:user_details', user_id=user_id)
#     else:
#         form = UserProfileForm(instance=user_profile)
#
#     return render(request, 'users/edit_profile.html', {'form': form})







