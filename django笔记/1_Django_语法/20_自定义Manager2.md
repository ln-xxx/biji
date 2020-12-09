#### 重写删除
#### 单个对象删除
- Student.objects.first().delete()
- Student.delete()   #重写的是这个的父类delete()方法


#### 批量删除

- Student.objects.filter().delete()
- Student.objects.filter().all()  #重写_clone()方法
- Student.objects.all()  #重写get_queryset()方法   查询所有记录


```
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models import QuerySet
from django.db.models.manager import Manager



class CustomManager(Manager):

    #查询出需要删除的记录
    def get_queryset(self):
        row_queryset = Manager.get_queryset(self).filter(isdelete=False)
        return row_queryset

    #重写父类filter方法
    def filter(self, *args, **kwargs):
        #调用父类的filter方法
        dellist = Manager.filter(self, *args, **kwargs)

        #声明闭包方法进行逻辑删除
        def delete1(delqueryset):
            for delq in delqueryset:
                delq.isdelete=True
                delq.save()

        import new
        dellist.delete = new.instancemethod(delete1,dellist,QuerySet)

        return dellist




# Create your models here.
class Student(models.Model):
    sname=models.CharField(max_length=30,unique=True)
    isdelete=models.BooleanField(default=False)


    objects=CustomManager()
    # 重写Student.delete()
    #实现单条记录的逻辑删除
    # def delete(self, using=None, keep_parents=False):
    #     self.isdelete=True
    #     self.save()



    class Meta:
        db_table='t_student'

    def __unicode__(self):
        return u'Student:%s'%self.sname


 


```



#### 闭包：
        在一个外函数中定义了一个内函数，内函数里运用了外函数的临时变量，并且外函数的返回值是内函数的引用。这样就构成了一个闭包。


