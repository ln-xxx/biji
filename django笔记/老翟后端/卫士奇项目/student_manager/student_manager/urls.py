"""student_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from first import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # 通过视图函数index添加表数据
    # path('', views.index),
    # 首页
    path('', views.first_page, name='index'),
    # 添加页面
    path('add/', views.add, name='add'),
    # 删除
    path('del/<int:sid>/', views.delete, name='del'),
    # 修改页面
    path('update/<int:sid>/', views.update, name='update'),
    # 查看页面
    path('detail/<int:sid>/', views.detail, name='detail'),
]

