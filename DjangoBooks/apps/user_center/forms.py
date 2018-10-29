from django import forms
from django.forms import widgets
from user_center import models
from django.core.exceptions import ValidationError


class ArtsUserRegForm(forms.Form):
    username = forms.CharField(
        label="用户名",
        required=True,
        min_length=6,
        max_length=20,
        widget=widgets.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "请输入用户名，长度为6 ~ 20",
            }),
        error_messages={
            "required": "对不起，输入的用户名不能为空",
            "min_length": "不行, 长度小于6",
            "max_length": "sorry, 长度大于20",
        }
    )
    password = forms.CharField(
        label="密码",
        required=True,
        min_length=6,
        max_length=20,
        widget=widgets.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "请输入密码, 长度为6~20",
            }),
        error_messages={
            "required": "密码不能为空",
            "min_length": "不行, 长度小于6",
            "max_length": "sorry, 长度大于20",
        }
    )
    email = forms.EmailField(
        label="163邮箱",
        required=True,
        widget=widgets.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "请输入邮箱",
            }),
        error_messages={
            "required": "邮箱不能为空",
        }
    )


    def clean_username(self):
        # 对会员信息的用户名username进行校验
        # 此函数返回的结果会存到 cleaned_data
        username = self.cleaned_data.get("username", "")
        user_count = models.ArtsUser.objects.filter(username=username).count()
        if user_count:
            raise ValidationError("用户名已经存在！")
        return username

    # def clean_email(self):
    #     # 对会员信息的用户名username进行校验
    #     # 此函数返回的结果会存到 cleaned_data
    #     email = self.cleaned_data.get("email", "")
    #     user_count = models.ArtsUser.objects.filter(email=email).count()
    #     if user_count:
    #         raise ValidationError("邮箱已经存在！")
    #     return email

    def clean_phone(self):
        phone = self.cleaned_data.get('phone', "")
        user_count = models.ArtsUser.objects.first(phone = phone).count()
        if user_count:
            raise ValidationError('手机号以存在')
        return phone
# ---------------------登录表单验证
class ArtsUserLoginForm(forms.Form):
    username = forms.CharField(
        label="用户名",
        required=True,
        min_length=6,
        max_length=20,
        widget=widgets.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "请输入用户名，长度为6 ~ 20",
            }),
        error_messages={
            "required": "对不起，输入的用户名不能为空",
            "min_length": "不行, 长度小于6",
            "max_length": "sorry, 长度大于20",
        }
    )
    password = forms.CharField(
        label="密码",
        required=True,
        min_length=6,
        max_length=20,
        widget=widgets.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "请输入密码, 长度为6~20",
            }),
        error_messages={
            "required": "密码不能为空",
            "min_length": "不行, 长度小于6",
            "max_length": "sorry, 长度大于20",
        }
    )

