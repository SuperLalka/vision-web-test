from django.http import HttpResponse
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.shortcuts import redirect, render

from page_blocks.forms import (
    AuthorizationForm,
    RegistrationForm,
)
from page_blocks.models import (
    Block,
    User
)


def index(request):
    return render(request, 'index.html', context={
        'blocks': Block.objects.filter(is_active=True).order_by('sorting'),
        'auth_form': AuthorizationForm(),
        'reg_form': RegistrationForm(),
    })


def authentication(request):
    if request.method != 'POST':
        return redirect('page_blocks:index')

    form = AuthorizationForm(request.POST)
    if not form.is_valid():
        return HttpResponse('The entered data is incorrect')

    user = authenticate(request, **form.cleaned_data)
    if user is None:
        return HttpResponse('User is not found')
    auth_login(request, user)

    return redirect('page_blocks:index')


def logout(request):
    auth_logout(request)
    return redirect('page_blocks:index')


def registration(request):
    form = RegistrationForm(request.POST)
    if not form.is_valid():
        return HttpResponse('The entered data is incorrect')

    form.cleaned_data.pop('password_check')
    User.objects.create_user(**form.cleaned_data)
    return redirect('page_blocks:index')
