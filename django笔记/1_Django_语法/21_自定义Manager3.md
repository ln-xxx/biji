#### 重写create()

```

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models.manager import Manager



class CustomManager(Manager):
    # 重写方法Student.objects.create()
    # 实现Student.objects.create(sname='lisi',clazz='B208Python',course=('HTML5','UI','Java','Python'))
    def create(self, **kwargs):
        clsname=kwargs.get('clazz')
        clazz = self.__get_cls(clsname)
        kwargs['clazz']=clazz

        course=kwargs.pop('course')

        stu = Manager.create(self,**kwargs)
        stu.save()

        stu.course.add(*self.__get_course(*course))
        stu.save()

        return stu


    def __get_cls(self, clsname):
        try:
            cls = Clazz.objects.get(cname=clsname)
        except Clazz.DoesNotExist:
            cls = Clazz.objects.create(cname=clsname)
            cls.save()
        return cls


    def __get_course(self,*course):
        row_course=[]
        for cour in course:
            try:
                r_cour = Course.objects.get(course_name=cour)
            except Course.DoesNotExist:
                r_cour = Course.objects.create(course_name=cour)
                r_cour.save()
            row_course.append(r_cour)
        return row_course



class Clazz(models.Model):
    cname=models.CharField(max_length=30,unique=True)

    class Meta:
        db_table='t_clazz'

    def __unicode__(self):
        return u'Clazz:%s'%self.cname

class Course(models.Model):
    course_name=models.CharField(max_length=30,unique=True)

    class Meta:
        db_table='t_course'

    def __unicode__(self):
        return u'Course:%s'%self.course_name


# Create your models here.
class Student(models.Model):
    sname=models.CharField(max_length=30,unique=True)
    clazz=models.ForeignKey(Clazz)
    course=models.ManyToManyField(Course)


    objects=CustomManager()



    class Meta:
        db_table='t_student'

    def __unicode__(self):
        return u'Student:%s'%self.sname







```