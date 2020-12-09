# linux入门2

检测当前服务器的环境,查看已经安装了那些软件

~~~linux

#主机网址
ifconfig -all /ip addr
#查看python是否安装
python -V
#查看python的安装路径
which python
cd /usr/bin/
ls -al python*
#查看python安装了那些包
pip list
#是否安装了 virualenv
virualenv
#检查虚拟环境是否能用
virtualenv -- version
##虚拟目录和项目发布目录   个人习惯(/data/env+++wwwroot)
cd /data
#进入虚拟环境检测软件
pip list
#检测uwsgi是否可用
uwsgi
which uwsgi
cd /usr/bin
ls -al uwsgi*

#nginx是否安装
  
~~~







### 生产环境介绍

工作中项目发布真实服务器环境

* 域名(万网/阿里云)
* 云服务器(阿里云/腾讯云/华为云/)
* 域名解析到服务器(DNS解析)



## 阿里云解析过程

实现:输入www.gf521.cn自动打开我的网站

前提:

* 购买域名
* 购买阿里云服务器
* 进入阿里云后台进行DNS解析
* 解析之前需要完成备案



### DNS域名解析

配置完后需要

查看nginx和uwsgi或其他软件的运行状态

netstat - atunp



































