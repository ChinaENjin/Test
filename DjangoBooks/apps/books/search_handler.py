from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.shortcuts import HttpResponseRedirect, render

from books.models import Art


def search_handler(request):
    key = request.GET.get('key', '')
    url = request.path
    if key == '':
        return HttpResponseRedirect('/books/index')
    else:
        page = request.GET.get('page', 1)
        page = int(page)
        art_sets = Art.objects.filter(Q(a_title__contains=str(key))
                                      | Q(a_content__contains=str(key))
                                      | Q(a_info__contains=str(key))
                                      ).distinct()
        p = Paginator(art_sets, 10)
        # print(p.page_range,type(p.page_range))
        btnum = 5
        if btnum > p.num_pages:
            firstpage = 1
            lastpage = p.num_pages
        else:
            if page == 1:
                firstpage = 1
                lastpage = btnum
            else:
                firstpage = page - 2
                lastpage = page + btnum - 2
                if firstpage < 1:
                    firstpage = 1
                if lastpage > p.num_pages:
                    lastpage = p.num_pages
        try:
            data = p.page(page)
        except PageNotAnInteger:  # 如果输入页码错误比如小数，就显示第一页
            data = p.page(1)
        except EmptyPage:  # 如果超过了页码范围，就把最后的页码显示出来，
            data = p.page(p.num_pages)

        context = dict(
            data=data,
            url=url,
            p=p,
            key = key,
            page=page,  # 用来获取这一页的页码反馈给前端
            pagerange=range(firstpage, lastpage + 1),
        )
    return render(request,'search_handler.html',context = context)


