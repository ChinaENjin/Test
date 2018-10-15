import numpy

__author__ = "Administrator"
__date__ = "2018/10/9 20:25"
# -*- coding:utf-8 -*-
import datetime
# now = datetime.datetime.now().strftime('%Y-%m-%d').split('-')
# print(now)
# today = now[2]
# print(today)
# d = datetime.datetime.now()
# weekday = d.weekday()+1
# dt = datetime.datetime(int(now[0]), int(now[1]), int(now[2]))
# print('是第'+ dt.strftime('%j') + '天')
# print('是本月第%s天'%today)
# print('是本月第%s周'%weekday)

# list = [1,3,5,7,9]
# list.remove(numpy.max(list))
# print(list)

from collections import OrderedDict


# dic = OrderedDict()   # 声明有序字典
# dic.clear()   # 清空有序字典
# dic['233'] = 233   # 加入键值对
# print(dir(OrderedDict))
# print(dic)

def num():
    return [lambda x: i * x for i in range(4)]

# print(num())
print([m(2) for m in num()])
