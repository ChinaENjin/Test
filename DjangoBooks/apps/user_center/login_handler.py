from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from user_center import forms
from DjangoBooks.utils import flash
from user_center import models


def create_pwd_md5(str_password):
    import hashlib
    h1 = hashlib.md5()
    h1.update(str_password.encode(encoding="utf-8"))
    return h1.hexdigest()


@csrf_exempt
def Login_handler(request):
    login_form = forms.ArtsUserLoginForm()
    if request.method == "POST":
        login_form = forms.ArtsUserLoginForm(data=request.POST)
        if not login_form.is_valid():
            flash(request, 'error', f"用户登录校验失败")
            context = dict(form=forms.ArtsUserLoginForm())
            return render(request, 'login_handler.html', context=context)
        username = login_form.cleaned_data.get('username')
        password = create_pwd_md5(login_form.cleaned_data.get('password'))
        user = models.ArtsUser.objects.filter(username=username, password=password, isActive=True)
        user_first = user.first()
        if user_first:
            request.session['muser'] = user_first
            return HttpResponseRedirect('/books/index')

        else:
            flash(request, 'error', f"用户{username}登录失败")

    context = dict(form=login_form)
    return render(request, 'login_handler.html', context=context)


def LogoutHandler(request):
    del request.session['muser']
    return HttpResponseRedirect('/user/login')
