#### Django中的事务处理
- Django中的事务是自动提交模式

```
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Clazz(models.Model):
    cno = models.AutoField(primary_key=True)
    cname = models.CharField(max_length=30)

    class Meta:
        db_table='t_cls'

    def __unicode__(self):
        return u'Clazz:%s,%s'%(self.cno,self.cname)

class Stu(models.Model):
    sno = models.AutoField(primary_key=True)
    sname = models.CharField(max_length=30)
    score = models.PositiveIntegerField(max_length=3)
    created = models.DateField(auto_now_add=True)
    clazz = models.ForeignKey(Clazz,on_delete=models.CASCADE)

    from django.db.transaction import atomic

    @atomic
    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        try:
            self.clazz = Clazz.objects.get(cname=self.clazz.cname)
        except Clazz.DoesNotExist:
            self.clazz = Clazz.objects.create(cname=self.clazz.cname)
            
        #制造异常
        1/0

        models.Model.save(self, force_insert, force_update, using,update_fields)


    class Meta:
        db_table='t_stu'

    def __unicode__(self):
        return u'Stu:%s,%s'%(self.sname,self.score)








```

#### 测试结果
```
#两张表中都没有插入新数据

from student.models import *
stu = Stu(sname='xiaowang',score=88,clazz=Clazz(cname='Oracle'))
stu.save()

Traceback (most recent call last):
  File "<input>", line 1, in <module>
  File "C:\Python27\lib\site-packages\django\utils\decorators.py", line 185, in inner
    return func(*args, **kwargs)
  File "D:\pythoncodes\django_20180402\demo\demo3\student\models.py", line 34, in save
    1/0
ZeroDivisionError: integer division or modulo by zero


```