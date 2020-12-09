# 第十天数据分析web 展示

**房源分析,网页版展示:**

**技术介绍:**

* django
* 数据源:表格/csv格式
* 数据分析 numpy +pandas 
* 图形展示 静态图/echars动态图

**找房神器项目要点:**

* **项目模块划分(链接模块,安居模块,我爱我家模块......)**
* **路由配置:urls.py(总路由器配置包含N个子模块路由配置)**
  * url 路径配置相互独立,互不影响
* **静态资源引入(html,css,js)**
* **控制层逻辑处理和页面跳转(views.py)**
* **数据分析框架和django结合**
* **百度echars引入页面**



**目标: 非常重要[自己手动完成]**



# 建项目划分模块

* 项目名:soufang04
* 模块名: lianjia   anju .....
* **IDE  Eclips     pycharm.....**

**注意1:虚拟环境选择:anacoda**

本地虚拟环境

**在settings.py里面**

```
"""
手动引入自己创建的模块  
"""

INSTALLED_APPS = [
    'lianjia.apps.LianjaiConfig',
    'anju.apps.AnjuConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

**路由配置:**

总路由配置文件urls.py 引入每个模块对应的urls.py配置文件~~

每个模块都复制跟目录urls.py 配置路由,通过include 指令整合到跟目录urls.py中

### 引入静态资源

静态资源分为3类,统称为模板:

* html

* js

* css 

  ***(1)每个模块App新建templates(html代码)和static(css/js/图片)保存**

* (2) setting .py中设置引入模板和静态文件

~~~python
'DIRS':[os.path.join(BASE_DIR,'templates')],
    
STATIC_URL ='/static/'


跳转模块的方法

<a href={%url 'lianjia:index'%}>

#把数据渲染到网页
return render(request,'sub.html',{}字典的格式)
~~~

* (3) view中跳转到页面render()
* (4),网页解决css和图片路径问题

## 引入百度echars

* 引入百度echars.js
* 页面准备显示数据的div
* 复制画图代码

**需要展示后台传输的数据**

~~~python
return render(request,'sub.html',{}字典的格式)


#网页中渲染 替换option中2个data信息

data: [{%for x in xlist%}
       '{{x}}',
      {%endfor%}]



~~~

## 引入数据分析框架

**实现案例,统计每个地区的房源数量**

* 导入numpy pandas matplotlib库
* 数据分析代码
* 获得list
  * dataframe 的tolist()方法

**动态图展示:可使用pyechars和django结合**

























