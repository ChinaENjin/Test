from django.shortcuts import HttpResponseRedirect, render

from books import models
from message.models import Comment
from message import forms

def detail_handler(request):
    art_id = request.GET.get('id',0)
    if art_id == 0:
        return HttpResponseRedirect("/books/index")
    # 获取小说详情
    art_queryset = models.Art.objects.get(id= art_id)
    name = art_queryset.a_title
    print(name)
    # 获取小说对应的章节
    art_capters = models.Chapter.objects.filter(title= name )
    # for art_capter in art_capters:

    # 获取评论表单
    comment_form = forms.CommentForm()
    comment_list = Comment.objects.filter(art= art_id)
    context = dict(
        art= art_queryset,
        art_capters = art_capters,
        form = comment_form,
        comment_list = comment_list,
        comment_count = comment_list.count(),
    )
    return render(request, 'detail_handler.html',context = context)
