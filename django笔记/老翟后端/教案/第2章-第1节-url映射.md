#URL分发器

*思考:为什么我们输入127.0.0.1:8000能够给我们返回给我们特定的页面,而不会返回其他的页面呢?*

> django底层给我们做了一个映射, 访问一个url, 会把这个url的页面返回给我们.

*思考: 如果不想要这个页面, 想要看个别的页面怎么办呢?*

> 需要用到url与视图函数的映射

*思考: 那么什么是视图函数呢?*

> 举个栗子: 
>
> 访问豆瓣网站->电影->全部正在热映
>
> 在豆瓣的服务器上, 将这个url和这个页面进行了一个映射.
>
> 而这个网页又是一个动态的页面, 动态的页面指: 网页上所有的数据都不是写死的, 无论是电影名字,图片还是得分, 都是从数据库读取的, 这些工作需要很多代码完成, 这些代码可以放在一个函数中完成, 这个函数就叫做视图函数. 从开发者的角度想, 豆瓣访问这个url的时候, 实际上是访问了豆瓣服务器上的某个视图函数, 然后执行视图函数上的代码, 通过代码将数据读取出来. 这就是url与视图函数的映射.

**需求:**

*访问127.0.0.1:700端口, 返回一个其他的页面*

##1.	视图的基本用法：

* 视图一般都写在`app`的`views.py`中。不是必须的, 只是规范.
* 视图的第一个参数永远都是`request`（一个HttpRequest）对象。这是一个强制性的条件.

> django接收到客户端或者浏览器发送过来的请求之后, 会创建一个`httprequest`对象, 然后将这个对象作为视图函数的第一个参数传递进来. 

这个对象存储了请求过来的所有信息，包括携带的参数以及一些头部信息等。在视图中，一般是完成逻辑相关的操作。比如这个请求是添加一篇博客，那么可以通过request来接收到这些数据，然后存储到数据库中，最后再把执行的结果返回给浏览器。

* 视图函数的返回结果必须是`HttpResponseBase`对象或者子类的对象。

  创建一个新项目, 示例代码如下：

```python
from django.http import HttpResponse   # 快捷键 ctrl + b 能看到所有HttpResponseBase的子类
def book_list(request):
    return HttpResponse("书籍列表！")
```

## 2.	URL映射：

视图写完后，要与URL进行映射，也即用户在浏览器中输入什么`url`的时候可以请求到这个视图函数。在用户输入了某个`url`，请求到我们的网站的时候，`django`会从项目的`urls.py`文件中寻找对应的视图。在`urls.py`文件中有一个`urlpatterns`变量，以后`django`就会从这个变量中读取所有的匹配规则。

```python
from django.contrib import admin
from django.urls import path
from book import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('book/',views.book_list)
]
```

*练习1: 自己动手书写视图函数movie(电影, 并与url进行映射)*

*练习2: 自己动手书写视图函数music(音乐, 并与url进行映射)*

*思考: 在网站中,会有多少个视图函数呢? 如果所有的视图函数都写到这个urls.py中进行url映射,不方便项目的管理, 怎么办呢?*

> 针对每个模块专门创建一个python包进行管理, 注意是个包文件,不是文件夹
>
> book包-->(views.py专门进行书籍类的视图函数的管理, models.py, forms.py...)
>
> movie包-->(views.py专门进行电影类的视图函数的管理, models.py, forms.py..)

**思考:为什么在django项目会在urls.py中寻找所有的映射呢? 怎么不去其他地方找呢?**

> 1. settings.py中配置了ROOT_URLCONF 为urls.py.  所以django会去urls.py中寻找     
> 2. 在ulrs.py中所有的映射都会放在urlpatterns变量中存储
> 3. 所有的映射不是随便写的, 而是使用path函数或者re_path函数进行包装的

## 3. url的模块化

*思考: 如果所有的url映射关系都写到urls.py中?这里要写多少个url映射呢?方便项目的管理吗?*

> 在我们的项目中，不可能只有一个`app`，如果把所有的`app`的`views`中的视图都放在`urls.py`中进行映射，肯定会让代码显得非常乱。
>
> 因此`django`给我们提供了一个方法，可以在`app`内部包含自己的`url`匹配规则，而在项目的`urls.py`中再统一包含这个`app`的`urls`。使用这个技术需要借助`include`函数。
>
> 就像我们将不同`app`的视图函数分别放置在不同的`app`中一样

*思考: 豆瓣中都有哪些app呢?*

> Settings.py --> INSTALL_APP这里都是app, 这些都是已经被安装的app

**创建app**

进入工程所在目录, 执行命令

`python manage.py startapp book`

在相应的app中书写相应模块的视图函数

*思考: 为什么创建项目用到命令django-admin, 创建app需要用python manage.py*?

**django推荐的项目规范:**

按照功能或者模块进行分层，分成一个个app。所有和某个模块相关的视图都写在对应的app的views.py中，并且模型和其他的也是类似。然后django已经提供了一个比较方便创建app的命令叫做`python manage.py startapp [app的名称]`。把所有的代码写在各自的app中。

**project和app的关系:**

`app`是`django`项目的组成部分。一个`app`代表项目中的一个模块，所有`URL`请求的响应都是由`app`来处理。比如豆瓣，里面有图书，电影，音乐，同城等许许多多的模块，如果站在`django`的角度来看，图书，电影这些模块就是`app`，图书，电影这些`app`共同组成豆瓣这个项目。因此这里要有一个概念，`django`项目由许多`app`组成，一个`app`可以被用到其他项目，`django`也能拥有不同的`app`。

创建项目, 创建app, 示例代码如下：

```python
# first_project/urls.py文件：

from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('book/',include("book.urls"))   # 将所有book开头的url都到book这个app中的urls.py中进行匹配
    								# 相对于项目所在的路径
]
```

在`urls.py`文件中把所有的和`book`这个`app`相关的`url`都移动到`app/urls.py`中了，然后在`first_project/urls.py`中，通过`include`函数包含`book.urls`，以后在请求`book`相关的url的时候都需要加一个`book`的前缀。

```python
# book/urls.py文件：

from django.urls import path
from . import views

urlpatterns = [
    path('list/',views.book_list),
    path('detail/<book_id>/',views.book_detail)
]
```

以后访问书的列表的`url`的时候，就通过`/book/list/`来访问，访问书籍详情页面的`url`的时候就通过`book/detail/<id>`来访问。













