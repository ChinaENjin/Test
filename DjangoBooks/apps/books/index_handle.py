from django.shortcuts import render, HttpResponseRedirect

from books import models
from DjangoBooks import utils
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index_handle(request):
    """
    p.count  # 总条数
    p.num_pages  # 总页数
    p.page_range   range(first_page,end_page)
    :param request:
    :return:
    """
    try:
        url = request.path  # 得到url路径 books/index
        t = int(request.GET.get('t', 0) ) # 得到tag id
        page = int(request.GET.get('page', 1))  # 得到页码数
        tags = models.Tag.objects.filter(t_flag=0)  # 得到分类信息Qset对象
        if t == 0:
            data = models.Art.objects.filter(a_flag=0)
        else:
            data = models.Art.objects.filter(a_flag=0, a_tag_id=t)
        p = Paginator(data, 10)
        # print(p.page_range,type(p.page_range))
        btnum = 5
        if btnum > p.num_pages:
            firstpage = 1
            lastpage = btnum
        else:
            if page ==  1:
                firstpage = 1
                lastpage = btnum
            else:
                firstpage = page -2
                lastpage = page + btnum -2
                if firstpage < 1:
                    firstpage = 1
                if lastpage > p.num_pages:
                    lastpage = p.num_pages
        try:
            data = p.page(page)
        except PageNotAnInteger: # 如果输入页码错误比如小数，就显示第一页
            data = p.page(1)
        except EmptyPage: # 如果超过了页码范围，就把最后的页码显示出来，
            data = p.page(p.num_pages)
        key = 'page:%d:t:%d' % (page, t)
        utils.store_rds_str(key,data)   #将所有的url对应的数据存入redis
        context = dict(
            data = data,
            url=url,
            t=t,
            p=p,
            tags=tags,
            page = page,  #用来获取这一页的页码反馈给前端
            pagerange=range(firstpage, lastpage + 1),
        )
    except Exception:
        return render(request,'404.html')
    return render(request, 'index_handler.html', context=context)

    # if t == 0:
    #     total = models.Art.objects.filter(a_flag=0).count()
    # else:
    #     total = models.Art.objects.filter(a_flag=0, a_tag_id=t).count()
    # context = dict(
    #     pagenum=1,
    #     total=0,
    #     prev=1,
    #     next=1,
    #     pagerange=range(1, 2),
    #     data=[],
    #     url=url,
    #     tags=tags,
    #     page=page,
    #     t=t,
    # )
    # shownum = 10  #每页展示的数量
    # if total > 0:
    #     import math
    #     pagenum = int(math.ceil(total/shownum))  #总页数
    #     if page < 1:
    #         url = url + "?page=1&t=%d" % t #用户第一次进来page = 0
    #         return HttpResponseRedirect(url)
    #     if page > pagenum:   #输入大于最大页数定位到最后一页
    #         url =url + '?page=%d&t=%d' % (pagenum,t)
    #         return HttpResponseRedirect(url)
    #     offset = (page -1) * shownum
    #     if t== 0:
    #         data = models.Art.objects.filter(a_flag = 0)[offset:offset + shownum]
    #     else:
    #         data =  models.Art.objects.filter(a_flag = 0, a_tag_id=t)[offset:offset + shownum]
    #     key = 'page:%d:t:%d' % (page, t)
    #     utils.store_rds_str(key,data)   #将所有的url对应的数据存入redis
    #
    #     btnum = 5
    #     if btnum > pagenum:
    #         firstpage = 1
    #         lastpage = btnum
    #     else:
    #         if page ==  1:
    #             firstpage = 1
    #             lastpage = btnum
    #         else:
    #             firstpage = page -2
    #             lastpage = page + btnum -2
    #             if firstpage < 1:
    #                 firstpage = 1
    #             if lastpage > pagenum:
    #                 lastpage = pagenum
    # prev = page - 1
    # next = page + 1
    # if prev < 1:
    #     prev = 1
    # if next > pagenum:
    #     next = pagenum
    #
    # context = dict(
    #     pagenum=pagenum,
    #     total=total,
    #     prev=prev,
    #     next=next,
    #     pagerange=range(firstpage, lastpage + 1),
    #     data=data,
    #     url=url,
    #     tags=tags,
    #     page=page,
    #     t=t,
    #
    # )

    # return  render(request,'index_handler.html',context = context)
