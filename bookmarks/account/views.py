from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .forms import UserRegistrationForm, UserEditForm, ProfileEditForm
from .models import Profile


@login_required
def dashboard(request):
    return render(request, 'registration/dashboard.html', {'session': dashboard})


# from django.contrib.auth import authenticate, login
# from django.http import HttpResponse
# from django.shortcuts import render
#
# from .forms import LoginForm
#
#
# # Create your views here.
#
# def user_login(request):
#     if request.method == "POST":
#         form = LoginForm(request.POST)
#         print(form)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(request, username=cd['username'], password=cd['password'])
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return HttpResponse('authenticate successfully')
#                 else:
#                     return HttpResponse('Disabled account')
#             else:
#                 return HttpResponse('Invalid user')
#
#     else:
#         form = LoginForm()
#     return render(request, 'account/login.html', {'form': form})
def success(request):
    return render(request, 'registration/success.html')


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            if form.cleaned_data['password'] == form.cleaned_data['password2']:
                print(form.cleaned_data['password'])
                print(form.cleaned_data['password2'])
                email = form.cleaned_data['email']
                hashed_password = make_password(form.cleaned_data['password'])
                new_user = User.objects.create(username=username, email=email, password=hashed_password)
                Profile.objects.create(user=new_user)
                print(hashed_password)
                firstname = form.cleaned_data['first_name']
                # new_user = form.save(commit=False)
                # password = form.cleaned_data['password']
                # new_user.set_password(password)
                # new_user.save()
                return render(request, 'registration/success.html', {'firstname': firstname})
    else:
        form = UserRegistrationForm()

    return render(request, 'registration/create_user.html', {'form': form})


@login_required()
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'profile updated successfully')
        else:
            messages.error(request, 'error in updating your profile')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

    return render(request, 'account/edit.html', {'user_form': user_form, 'profile_form': profile_form})
