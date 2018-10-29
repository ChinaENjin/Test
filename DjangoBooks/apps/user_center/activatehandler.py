from django.core.cache import cache
from django.http import HttpResponse

from user_center import models


def ActivateHandler(request):
    token = request.GET.get('token')
    user_id = cache.get(token)

    if user_id:
        cache.delete(token)
        user = models.ArtsUser.objects.get(pk=user_id)
        user.isActive = True
        user.save()
        return HttpResponse(f"用户{user.username} 激活成功")
    else:
        return HttpResponse("激活用户信息过期，请重新申请激活邮件")

