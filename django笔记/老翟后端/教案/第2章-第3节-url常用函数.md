## include

在项目变大以后，经常不会把所有的`url`匹配规则都放在项目的`urls.py`文件中，而是每个`app`都有自己的`urls.py`文件，在这个文件中存储的都是当前这个`app`的所有`url`匹配规则。然后再统一注册到项目的`urls.py`文件中。`include`函数有多种用法，这里讲下两种常用的用法。

1. `include(pattern,namespace=None)`：直接把其他`app`的`urls`包含进来。示例代码如下：

   ```python
    from django.contrib import admin
    from django.urls import path,include
   
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('book/',include("book.urls"))
    ]
   ```

   当然也可以传递`namespace`参数来指定一个实例命名空间，但是在使用实例命名空间之前，必须先指定一个应用命名空间。示例代码如下：

   ```python
   # 主urls.py文件：
   from django.urls import path,include
   urlpatterns = [
       path('movie/',include('movie.urls',namespace='movie'))
   ]
   ```

   然后在`movie/urls.py`中指定应用命名空间。实例代码如下：

   ```python
   from django.urls import path
   from . import views
   
   # 应用命名空间
   app_name = 'movie'
   
   urlpatterns = [
       path('',views.movie,name='index'),
       path('list/',views.movie_list,name='list'),
   ]
   ```


## reverse

1. 之前我们都是通过url来访问视图函数。有时候我们知道这个视图函数，但是想反转回他的url。这时候就可以通过`reverse`来实现。示例代码如下：

    ```python
    reverse("list")
    > /book/list/
    ```

    如果有应用命名空间或者有实例命名空间，那么应该在反转的时候加上命名空间。示例代码如下：

    ```python
    reverse('book:list')
    > /book/list/
    ```

    如果这个url中需要传递参数，那么可以通过`kwargs`来传递参数。示例代码如下：

    ```python
    reverse("book:detail",kwargs={"book_id":1})
    > /book/detail/1
    ```

    因为`django`中的`reverse`反转`url`的时候不区分`GET`请求和`POST`请求，因此不能在反转的时候添加查询字符串的参数。如果想要添加查询字符串的参数，只能手动的添加。示例代码如下：

    ```python
    login_url = reverse('login') + "?next=/"
    ```

     

##path函数：

`path`函数的定义为：`path(route,view,name=None,kwargs=None)`。以下对这几个参数进行讲解。

1. `route`参数：`url`的匹配规则。这个参数中可以指定`url`中需要传递的参数，比如在访问文章详情页的时候，可以传递一个`id`。传递参数是通过`<>`尖括号来进行指定的。并且在传递参数的时候，可以指定这个参数的数据类型，比如文章的`id`都是`int`类型，那么可以这样写`<int:id>`，以后匹配的时候，就只会匹配到`id`为`int`类型的`url`，而不会匹配其他的`url`，并且在视图函数中获取这个参数的时候，就已经被转换成一个`int`类型了。其中还有几种常用的类型：

   - str：非空的字符串类型。默认的转换器。但是不能包含斜杠。
   - int：匹配任意的零或者正数的整形。到视图函数中就是一个int类型。
   - slug：由英文中的横杠`-`，或者下划线`_`连接英文字符或者数字而成的字符串。
   - uuid：匹配`uuid`字符串。
   - path：匹配非空的英文字符串，可以包含斜杠。

2. `view`参数：可以为一个视图函数或者是`类视图.as_view()`或者是`django.urls.include()`函数的返回值。

3. `name`参数：这个参数是给这个`url`取个名字的，这在项目比较大，`url`比较多的时候用处很大。

4. `kwargs`参数：有时候想给视图函数传递一些额外的参数，就可以通过`kwargs`参数进行传递。这个参数接收一个字典。传到视图函数中的时候，会作为一个关键字参数传过去。比如以下的`url`规则：

   ```
    from django.urls import path
    from . import views
   
    urlpatterns = [
        path('blog/<int:year>/', views.year_archive, {'foo': 'bar'}),
    ]
   ```

   那么以后在访问`blog/1991/`这个url的时候，会将`foo=bar`作为关键字参数传给`year_archive`函数。

##re_path函数：

有时候我们在写url匹配的时候，想要写使用正则表达式来实现一些复杂的需求，那么这时候我们可以使用`re_path`来实现。`re_path`的参数和`path`参数一模一样，只不过第一个参数也就是`route`参数可以为一个正则表达式。
一些使用`re_path`的示例代码如下：

```python
    from django.urls import path, re_path

    from . import views

    urlpatterns = [
        path('articles/2003/', views.special_case_2003),
        re_path(r'articles/(?P<year>[0-9]{4})/', views.year_archive),
        re_path(r'articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/', views.month_archive),
        re_path(r'articles/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<slug>[\w-_]+)/', views.article_detail),
    ]
```

以上例子中我们可以看到，所有的`route`字符串前面都加了一个`r`，表示这个字符串是一个原生字符串。在写正则表达式中是推荐使用原生字符串的，这样可以避免在`python`这一层面进行转义。而且，使用正则表达式捕获参数的时候，是用一个圆括号进行包裹，然后这个参数的名字是通过尖括号`<year>`进行包裹，之后才是写正则表达式的语法。



 