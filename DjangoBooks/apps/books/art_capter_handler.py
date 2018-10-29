'''
小说章节
/art/capter?id=capter_id
'''
from django.shortcuts import render

from books import models
from books.detail_handler import detail_handler


def ArtCapterHandler(request):
    capter_id = int(request.GET.get("id", 0))
    if capter_id == 0:
        return detail_handler(request)
    art_capter = models.Chapter.objects.get(id=capter_id)
    art_capter.content = ['第' + i.strip() for i in art_capter.content.split('第') if i != '']

    context = dict(
        art_capter=art_capter
    )
    return render(request, "capter_handler.html", context=context)
