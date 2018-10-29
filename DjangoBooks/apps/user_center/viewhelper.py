from django.core.mail import send_mail
from django.template import loader

from user_center.models import ArtsUser
from DjangoBooks import settings


def send_mail_to(username,  active_url, receive_mail, title="xxx"):

    subject = "欢迎使用书城平台-邮件激活"

    temp = loader.get_template('user_active.html')

    data = {
        "username": username,
        "active_url": active_url
    }

    html_message = temp.render(context=data)

    send_mail(subject, title, from_email=settings.EMAIL_HOST_USER, recipient_list=[receive_mail],
              html_message=html_message)


def get_user_by_id(id):
    try:
        user = ArtsUser.objects.get(pk=id)
        return user
    except:
        return None
