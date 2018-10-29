from celery import shared_task
from user_center.viewhelper import send_mail_to
'''
此文件是属于celery工作worker处理进程文件
'''

# @shared_task
# def say_hello(str):
#     sleep(2)
#     print("-----------------")
#     r = settings.R
#     r.set("celery_hello", 'hello, ' + str)
#     return  str


# @shared_task
# def send_mail_asy(email):
#     sleep(3)
#     print("send mail", email)
#     return "Hello"


@shared_task
def send_mail_celery(username,  active_url, receive_mail, title):
    #send_mail("Test", "Hello", settings.EMAIL_HOST_USER, [email])
    print('----------------发送邮件')
    send_mail_to(username,  active_url, receive_mail, title)  #调用viewhelper 发送邮件

