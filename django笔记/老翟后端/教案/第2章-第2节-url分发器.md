# URL分发器

## 1. url中添加参数

*思考: 什么叫做参数?*

> 不固定的, 会发生变化的
>
> 有时候，`url`中包含了一些参数需要动态调整。

举个栗子:

比如简书某篇文章的详情页的url，是`https://www.jianshu.com/p/a5aab9c4978e`后面的`a5aab9c4978e`就是这篇文章的`id`，那么简书的文章详情页面的url就可以写成`https://www.jianshu.com/p/<id>`，其中id就是文章的id。那么如何在`django`中实现这种需求呢。这时候我们可以在`path`函数中，使用尖括号的形式来定义一个参数。比如我现在想要获取一本书籍的详细信息，那么应该在`url`中指定这个参数。

新建项目, 新建app,示例代码如下：

####1.1  方法一: 传递参数

```python
from django.contrib import admin
from django.urls import path
from book import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('book/',views.book_list),  # 注意这里的参数是整个函数, 而不是函数执行的结果
    path('book/<book_id>/',views.book_detail)  # 注意参数的名字和视图函数中参数的名字保持一致
]
```

而`views.py`中的代码如下：

```python
def book_detail(request,book_id):   # 参数的名字和url中参数的名字保持一致
    text = "您输入的书籍的id是：%s" % book_id
    return HttpResponse(text)
```

*思考: 如果创建完项目,没有进行任何的映射, 会默认在首页提供一个默认的页面,怎么没有了呢?*

>  此时访问: `127.0.0.1:8000`报错: 页面没有找到错误.404
>
> 如果创建完项目,没有进行任何的映射, 会默认在首页提供一个默认的页面, 一旦在urls.py中写了任何一个映射,django就会把这个默认的页面映射关闭掉

增加参数, 在`views.py`和`urls.py`中修改如下:

````python
def book_detail(request,book_id, category_id):   
    text = "您输入的书籍的id是：%s" % (book_id, category_id)
    return HttpResponse(text)
````

````python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('book/<book_id>/<categroy_id>',views.book_detail)
]
````

______

####1.2  方法二: 查询字符串

当然，也可以通过查询字符串的方式传递一个参数过去。

示例代码如下：

```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index)
    path('book/',views.book_list),
    path('book/detail/',views.book_detail)
]
```

在`views.py`中的代码如下：

```python
def book_detail(request):
    # 模板中input标签 name='id'
    book_id = request.GET.get("id")   
    text = "您输入的书籍id是：%s" % book_id
    return HttpResponse(text)
```

以后在访问的时候就是通过`/book/detail/?id=1`即可将参数传递过去。

#### 1.3   指定参数类型(指定url转换器)    

`<int:arg>z`指定参数类型为整形

````python
def publish_detail(request, publish_id):
    book_id = request.GET.get("id")   
    text = "您输入的出版社id是：%s" % book_id
    return HttpResponse(text)
````

````python
from django.urls import converters  # 导入模块 进入查看所有转换器

urlpatterns = [
    path('book/publish/<int:publish_id>',views.publish_detail)  # 指定转换器类型
]
````

> 查看django所有内置的转换器
>
> - str：非空的字符串类型。默认的转换器。但是不能包含斜杠。
> - int：匹配任意的零或者正数的整形。到视图函数中就是一个int类型。
> - slug：由英文中的横杠`-`，或者下划线`_`连接英文字符或者数字而成的字符串。
> - uuid：匹配`uuid`字符串。
> - path：匹配非空的英文字符串，可以包含斜杠。任意字符.
>
> 如果参数没有写任何的转换器, 那么默认的转换器就是str

#### 1.4  指定默认的参数

使用`path`或者是`re_path`的后，在`route`中都可以包含参数，而有时候想指定默认的参数，这时候可以通过以下方式来完成。示例代码如下：

```python
from django.urls import path

from . import views

urlpatterns = [
    path('blog/', views.page),
    path('blog/page<int:num>/', views.page),
]

# View (in blog/views.py)
def page(request, num=1):
    # Output the appropriate page of blog entries, according to num.
    ...
```

当在访问`blog/`的时候，因为没有传递`num`参数，所以会匹配到第一个url，这时候就执行`view.page`这个视图函数，而在`page`函数中，又有`num=1`这个默认参数。因此这时候就可以不用传递参数。而如果访问`blog/1`的时候，因为在传递参数的时候传递了`num`，因此会匹配到第二个`url`，这时候也会执行`views.page`，然后把传递进来的参数传给`page`函数中的`num`。

