#### 重写all()_get_queryset()

```

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models.manager import Manager

class CustomManager(Manager):
    #重写Student.objects.all()
    # def all(self):
    #     return Manager.all(self).filter(isdelete=False)


    def get_queryset(self):
        return Manager.get_queryset(self).filter(isdelete=False)

class DeletedManager(models.Manager):
    def get_queryset(self):
        return Manager.get_queryset(self).filter(isdelete=True)

# Create your models here.
class Student(models.Model):
    sname=models.CharField(max_length=30,unique=True)
    isdelete=models.BooleanField(default=False)

    objects=CustomManager()

    delStus=DeletedManager()

    class Meta:
        db_table='t_student'

    def __unicode__(self):
        return u'Student:%s'%self.sname


```