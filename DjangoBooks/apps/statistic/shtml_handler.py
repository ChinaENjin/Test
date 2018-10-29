from django.shortcuts import render

from DjangoBooks.utils import check_user_login


@check_user_login
def IndexHandler(request):
	return render(request, "static_handler.html")

