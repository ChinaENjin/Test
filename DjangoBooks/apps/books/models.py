from DjangoUeditor.models import UEditorField
from django.db import models
from django.utils import timezone
from DjangoBooks.settings import DB_FIELD_VALID_CHOICES

"""
timezone.now 为了保证所有地区时间一致
如果网站面向的是多个时区用户，只以当前时间为标准开发，便会在时间计算上产生错误。
最好USE_TZ = True 同时安装 pytz 模块(pip install pytz) 。
verbose_name_plural = "学校"
如果不指定Django会自动在模型名称后加一个’s’
"""


class Tag(models.Model):
    t_name = models.CharField(max_length=60, verbose_name='书名字')
    t_info = models.CharField(max_length=60, verbose_name='书分类')
    t_createtime = models.DateTimeField(default=timezone.now, db_index=True, verbose_name='创建时间')
    t_flag = models.IntegerField(default=0, verbose_name='控制字段', choices=DB_FIELD_VALID_CHOICES)

    def __str__(self):
        return self.t_name

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name
        db_table = 'tag'
        # ordering这是一个字符串的元组或列表,更具字段排序默认升序 '-' 降序
        ordering = ["-t_createtime"]


class Art(models.Model):
    a_title = models.CharField(max_length=100, verbose_name='书名')
    a_info = models.CharField(max_length=200, verbose_name='书分类')
    # a_content = models.TextField(max_length=500,verbose_name='书详情介绍')
    a_content = UEditorField(verbose_name="文章内容", width=1000, height=600,
                             imagePath="media/arts_ups/ueditor/",
                             filePath="media/arts_ups/ueditor/",
                             blank=True, toolbars="full", default='')
    a_img = models.ImageField(null=True, blank=True, upload_to='media/arts_ups/%Y/%m',
                              verbose_name='封面', max_length=150
                              )
    a_createtime = models.DateTimeField(default=timezone.now, db_index=True,
                                        verbose_name="添加时间")
    a_tag = models.ForeignKey(Tag, verbose_name="关联文章标签")
    a_price = models.IntegerField(default=0, verbose_name="单价")
    a_flag = models.IntegerField(default=0, verbose_name="控制字段", choices=DB_FIELD_VALID_CHOICES)
    operator = models.ForeignKey('auth.User', default=1, verbose_name='api操作者')

    # 和后台用户建立外键auth.User
    def __str__(self):
        return self.a_title

    class Meta:
        verbose_name = '小说'
        verbose_name_plural = verbose_name
        db_table = 'art'
        ordering = ['-a_createtime']


class Chapter(models.Model):
    art = models.ForeignKey(Art, verbose_name='小说')
    title = models.CharField(max_length=100, verbose_name='章节标题')
    content = models.TextField(verbose_name="小说章节内容")
    create_time = models.DateTimeField(default=timezone.now, db_index=True,
                                       verbose_name="添加时间")

    class Meta:
        db_table = "art_chapter"
        verbose_name = "小说章节"
        verbose_name_plural = verbose_name
