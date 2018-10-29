from django.contrib import admin

# Register your models here.
import xadmin

from xadmin import views
from  user_center.models import  ArtsUser
from books import models
from message.models import Comment
class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True

class GlobalSettings(object):
    site_title = '小说电商平台后台管理系统'
    site_footer = '千锋武汉python-1803'
    menu_style = 'accordion'  # 菜单折叠
    global_search_models = [ArtsUser, models.Tag, models.Art,
                            models.Chapter, Comment]

    global_models_icon = {
        models.Art: "glyphicon glyphicon-book",
        models.Tag: "fa fa-cloud",
        models.Chapter: "glyphicon glyphicon-th-list",
        ArtsUser: "glyphicon glyphicon-user",
        Comment: "glyphicon glyphicon-list-alt",
        # UserMessage:  "glyphicon glyphicon-list-alt",
    }  # 设置models的全局图标

'''
标签自定义展示对象
'''
class TagAdmin(object):
    list_display = ['t_name', 't_info', 't_createtime', 't_flag']
    search_fields = ['t_name', 't_info', 't_createtime']
    list_filter = ['t_name', 't_info', 't_flag']
    list_editable = ['t_name', 't_info']


class ArtAdmin(object):
    list_display = ['a_title', 'a_info', 'a_content', 'a_img', 'a_price' ,'a_createtime', 'a_tag']
    search_fields = ['a_title', 'a_info', 'a_content', 'a_img', 'a_createtime']
    list_filter = ['a_title', 'a_info', 'a_createtime', 'a_flag']
    show_detail_fields = ['a_title']
    list_per_page = 5
    list_editable = ['a_title', 'a_info', 'a_price' ,'a_content']
    style_fields = {'a_content': 'ueditor'}

class CapterAdmin(object):
    list_display = ['art', 'title', 'content', 'create_time']
    search_fields = ['art', 'title', 'content', 'create_time']
    list_filter = ['art', 'title', 'content', 'create_time']
    list_per_page = 5


class CommentAdmin(object):
    list_display = ['name', 'title', 'text', 'created_time', 'art', 'flag']
    search_fields =  ['name', 'title', 'text', 'created_time', 'art']
    list_per_page = 5

# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
class ArtsUserAdmin(object):
    list_display = ('username', 'password', 'email','isActive')

xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.register(views.BaseAdminView, BaseSetting)

xadmin.site.register(ArtsUser,ArtsUserAdmin)
xadmin.site.register(models.Tag, TagAdmin)
xadmin.site.register(models.Art, ArtAdmin)
xadmin.site.register(models.Chapter, CapterAdmin)
xadmin.site.register(Comment, CommentAdmin)