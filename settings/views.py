from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic import (
    ListView
)
from user.forms import UserRegisterForm, UserUpdateForm
from django.contrib.auth.decorators import login_required
from user.models import Role


# All users list
class UserListView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'index.html'
    context_object_name = 'users'
    ordering = ['first_name']
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Settings'
        return context


# Add new user
@login_required()
def create(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'User registration by admin is successfully!')
            role = Role(user_id=User.objects.latest('id').id, role=request.POST.get('role'))
            role.save()
            return redirect('setting-index')
    return render(request, 'user/add.html', {'title': 'New User'})


# Delete user
@login_required()
def delete_user(request, user_id):
    try:
        u = User.objects.get(id=user_id)
        u.delete()
        messages.success(request, 'User delete successfully!')
        return redirect('setting-index')
    except User.DoesNotExist:
        messages.error(request, 'User does not exist!')
        return redirect('setting-index')
    except Exception as e:
        messages.error(request, 'Failed to user delete!')
        return redirect('setting-index')


# User update
@login_required()
def edit_user(request, user_id):
    users = User.objects.get(id=user_id)
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=users)
        if form.is_valid():
            form.save()

            messages.success(request, 'User updated by admin is successfully!')
            return redirect('setting-index')
    return render(request, 'user/edit.html', {'title': 'Edit User', 'users': users})
