#### 配置模型类
```
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.contrib.auth.models import User
from django.utils import timezone


class BlogArticles(models.Model):
    title = models.CharField(max_length=300)
    author = models.ForeignKey(User,related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-publish',)


    def __unicode__(self):
        return self.title



```
#### 配置admin后台类
```

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import BlogArticles

class BlogArticlesAdmin(admin.ModelAdmin):
    #显示表格列表字段
    list_display = ('title','author','publish',)
    #条件查询字段
    list_filter = ('publish','author',)
    #搜索框中根据某些字段进行查询
    search_fields = ('title','body')
    # 在admin后台类中加入raw_id_fields（只适用于外键）后，会显示外键的详细信息
    raw_id_fields = ("author",)
    #以某个日期字段分层次查询
    date_hierarchy = 'publish'
    #排序字段
    ordering = ['publish','author']

admin.site.register(BlogArticles,BlogArticlesAdmin)

```
hierarchy:层级

#### 终端创建超级用户
```
python manage.py createsuperuser


```


#### 浏览器访问
```
http://127.0.0.1:8000/admin

```