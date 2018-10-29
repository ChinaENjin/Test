from DjangoUeditor.models import UEditorField
from django.db import models
from django.utils import timezone
# Create your models here.
from books.models import Art
from DjangoBooks.settings import DB_FIELD_VALID_CHOICES


class Comment(models.Model):
    name = models.CharField(max_length=50, verbose_name="评论者")
    title = models.CharField(max_length=200, verbose_name="评论标题")
    text = models.TextField(verbose_name="评论内容")
    created_time = models.DateTimeField(default=timezone.now, db_index=True, verbose_name="创建时间")
    art = models.ForeignKey(Art, verbose_name="关联的小说")
    flag = models.IntegerField(default=0, verbose_name="控制字段", choices=DB_FIELD_VALID_CHOICES)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "comments"
        verbose_name = "用户评论"
        verbose_name_plural = verbose_name
        ordering = ["-created_time"]

class UserMessage(models.Model):
    name = models.CharField(max_length=20, verbose_name="用户名")
    email = models.EmailField(verbose_name="邮箱")
    address = models.CharField(max_length=100, verbose_name="地址")
    # message = models.TextField(verbose_name="留言内容")
    message = UEditorField(verbose_name="留言内容", width=1000, height=600,
                           imagePath="msg_ups/ueditor/",
                           filePath="msg_ups/ueditor/",
                           blank=True, toolbars="full", default='')
    create_time = models.DateTimeField(default=timezone.now, verbose_name="创建时间")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "user_message"
        verbose_name = "用户留言"
        verbose_name_plural = verbose_name
        ordering = ["-create_time"]

