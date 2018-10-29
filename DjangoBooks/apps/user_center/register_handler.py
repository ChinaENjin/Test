from django.core.cache import cache
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import uuid

from DjangoBooks import settings
from user_center import forms
from DjangoBooks.utils import flash
from user_center import models


def create_pwd_md5(str_password):
    import hashlib
    h1 = hashlib.md5()
    h1.update(str_password.encode(encoding='utf-8'))
    return h1.hexdigest()


@csrf_exempt
def Register_handle(request):
    reg_form = forms.ArtsUserRegForm()
    method = request.method
    context = dict(form=reg_form)
    if method == "POST":
        reg_form = forms.ArtsUserRegForm(data=request.POST)
        if not reg_form.is_valid():  # 无效
            flash(request, 'error', f"用户注册是失败")
            context = dict(form=forms.ArtsUserRegForm(data=request.POST))
            return render(request, 'register_handler.html', context=context)
        username = reg_form.cleaned_data.get('username')
        password = create_pwd_md5(reg_form.cleaned_data.get('password'))
        email = reg_form.cleaned_data.get('email')
        user = models.ArtsUser(username=username, password=password, email=email)
        user.save()
        flash(request, 'success', f"恭喜{username}注册成功，需查看邮件激活登录")
        # 生成token  时间 + ip + 随机数
        # uuid
        token = str(uuid.uuid4())  # 产生一个随机数
        cache.set(token, user.id, timeout=2 * 60 * 60 * 24)  # token
        active_url = "http://%s:%s/user/active/?token=%s" % (settings.DJANGO_SERVICE[0],
                                                             settings.DJANGO_SERVICE[1],
                                                             token)  # 激活url 127.0.0.1:8000?token=随机数

        # 同步处理
        # viewhelper.send_mail_to(username, active_url, email, "注册邮箱激活")

        # TODO 异步处理
        from user_center import tasks
        # delay创建任务，并送入消息队列
        tasks.send_mail_celery.delay(username, active_url, email, '注册邮箱激活')  # 调用token异步发送邮箱

    context = dict(form=reg_form)
    return render(request, 'register_handler.html', context=context)
