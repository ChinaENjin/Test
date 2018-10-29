from django.db import models
from django.utils import timezone

from books.models import Art
from user_center.models import ArtsUser
from DjangoBooks.settings import PAY_CHOICES, DINNER_CHOICES

# Create your models here.
'''
订单数据模型
'''


class ProductOrder(models.Model):
    order_id = models.BigIntegerField(verbose_name='订单号', unique=True)
    pay_type = models.IntegerField(default=0, verbose_name='支付类型', choices=PAY_CHOICES)
    address = models.CharField(default='', max_length=200, verbose_name='订单配送地址')
    phone = models.BigIntegerField(default=0, verbose_name="联系方式")
    order_time = models.DateTimeField(default=timezone.now, db_index=True,
                                      verbose_name="下单时间")


'''
购物车条目
'''


class LineItem(models.Model):
    product = models.ForeignKey(Art, verbose_name='小说商品')
    user = models.ForeignKey(ArtsUser, verbose_name='购买用户')
    unit_price = models.DecimalField(default=0, max_digits=8, decimal_places=2, verbose_name="单价")
    quantity = models.IntegerField(default=0, verbose_name="购买数量")
    createtime = models.DateTimeField(default=timezone.now, verbose_name="创建时间")
    flag = models.IntegerField(default=0, verbose_name="购买状态", choices=DINNER_CHOICES)

    def __str__(self):
        return self.product.a_title

    class Meta:
        db_table = "line_item"
        verbose_name = "购物车条目"
        verbose_name_plural = verbose_name


'''
商品条目和订单关联表
1   1
3   1
4   1
'''


class OrderItemRelation(models.Model):
    line_item = models.ForeignKey(LineItem, verbose_name='关联条目')
    product_order = models.ForeignKey(ProductOrder, verbose_name='关联订单')
    create_time = models.DateTimeField(default=timezone.now, verbose_name='创建时间')

    class Meta:
        db_table = "order_item_relation"
        verbose_name = "商品条目和订单关联表"
        verbose_name_plural = verbose_name


'''
购物车
购物车是这些条目的容器。
购物车并不需要记录到数据库中，就好像超市并不关注顾客使用了哪些购物车而只关注他买了什么商品一样。
所以购物车不应该继承自models.Model，而仅仅应该是一个普通类
'''


class Cart(object):
    @classmethod
    def add_product(cls, product, user):
        the_item_products = LineItem.objects.filter(user=user.id, product=product)
        product_quality_dict = {}
        if len(product_quality_dict) > 0:
            the_product = the_item_products[0]
            this_quality = the_product.quantity + 1
            the_item_products.update(quantity=this_quality)
        else:
            l_item = LineItem(
                product=product,
                user=user,
                unit_price=product.a_price,
                quantity=1
            )
            l_item.save()
        return True

    @classmethod
    def get_products(cls, user):
        product_list = LineItem.objects.filter(user=user.id)
        total_price = 0
        for prod_item in product_list:
            total_price += prod_item.product.a_price * prod_item.quantity
        return (total_price, product_list)
