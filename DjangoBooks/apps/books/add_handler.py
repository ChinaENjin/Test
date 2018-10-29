# from django.shortcuts import HttpResponse
#
# from books.tasks import add
# # from user_center.tasks import say_hello
#
#
# def AddHandler(request):
#     x = int(request.GET.get('x',0))
#     y = int(request.GET.get('y',0))
#     add.delay(x,y)
#     say_hello.delay('wujiwu')
#     return HttpResponse('add delay ok')