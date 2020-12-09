### Linux入门

**Linux服务器搭建工作需要掌握的核心点**

- **虚拟机的使用**
- **Linux安装（注意事项）**
- **服务器搭建（重点）**
  - 网络配置（本地虚拟机）
  - SSH连接远程服务器（putty、xshell6）
  - FTP文件传输（FlashFXP、winscp）
  - 安装python（Linux自带python2.7.5）
  - 虚拟环境管理（virtualenv）
  - django安装
  - web服务器（Nginx + uwsgi）  django项目发布
  - 数据库mysql
  - DNS解析（域名）
  - Nginx多项目配置
- **虚拟机安装**
  - 虚拟机安装[重要]：https://blog.csdn.net/qq_39038465/article/details/81478847



### Linux目录结构

- bin:	存放二进制可执行文件
- boot:     存放用于系统引导时使用的各种文件
- dev:       用于存放设备文件
- etc:        存放系统配置文件
- home:   存放所有用户文件的根目录
- lib          存放跟文件系统中的程序运行所需要的共享库及内核模块
- mnt       系统管理员安装 临时文件系统的安装点
- opt         额外安装 的可选应用程序包所放置的位置
- proc       虚拟文件系统，存放当前内存的映射
- root        超级用户目录
- sbin        存放二进制可执行文件，只有root才可以访问
- tmp        用于存放临时文件
- usr          用于存放系统应用程序
- var          用于存放运行时需要改变数据的文件





## Linux命令

### IP地址和主机名相关的命令

##### 查看IP：ifconfig 

##### 重启网卡：service network restart

##### 查看网卡状态：service network status

##### 修改IP地址：vim /etc/sysconfig/network-scripts/ifcfg-ens33

```python
YPE="Ether net"             # 网络类型，以太网
BOOTPROTO="static"			# 改为静态IP
IPADDR="192.168.8.88"		# IP地址
NETMASK="255.255.255.0"		# 子网掩码
GATEWAY="192.168.8.1"		# 网关
DNS1="192.168.8.1"			# 首选DNS
ONBOOT="yes"				# 是否可以上网（默认为ON）
```

##### 查看主机名：hostname

##### 修改主机名：vim /etc/hostname



#### CentOS7更换清华yum镜像

清华：https://mirror.tuna.tsinghua.edu.cn/help/centos/



### VIM常用命令

```python
    dd        删除光标所在的那一行
	u         撤销上一步操作
	ndd		  删除光标所在位置起的多行   n为数字
	yy		  复制光标当前所在的那一行
	nyy		  复制多行 n为数字
	p 		  将已复制的内容粘贴到光标所在的位置的下一行
	大P		 将已复制的内容粘贴到光标所在的位置的上一行
	np		  粘贴多行到光标的下一行  n为数字
	ctrl+r    重复上一次操作
	$		  跳到一行的尾部
	0		  跳到一行的头部
	gg		  移动到这个文件的第一行
	G         跳到这个文件的最后一行
	nG		  跳到n行
	set nu	  显示行号
	H		  光标移动到屏幕的最上方那一行的第一个字符
	M		  光标移动到屏幕的中央那一行的第一个字符
	L		  光标移动到屏幕的最下面那一行的第一个字符
```

#### CentOS7下安装python3

```python
# 1、安装pyhton3.7 的依赖包

    yum -y groupinstall "Development tools"

    yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel libffi-devel

# 2、下载python3.7的“源码”：
    wget https://www.python.org/ftp/python/3.7.0/Python-3.7.0.tar.xz

# 3、解压并编译安装：
    tar -xJvf Python-3.7.0.tar.xz
    
# 4、用cd命令进入解压出来的Python文件夹
    cd Python-3.7.0

# 5、用./方法执行configure,并指定安装到usr目录下
    ./configure --prefix=/usr/local/python3  --enable-shared

# 6、开始编译安装
    make && make install

# 7、配置环境变量， 创建软链接
    ln -s /usr/local/python3/bin/python3 /usr/bin/python3  # 创建python3的软链接
    
    ln -s /usr/local/python3/bin/pip3 /usr/bin/pip3  # 创建pip的软链接
	
# 8、将编译目录下的libpython3.7m.so.1.0文件复制到
	cp /root/Python3.7.0/libpython3.7m.so.1.0 /usr/lib64/libpython3.7m.so.1.0
```

#### CentOS7下安装MySQL

```python
# 1、下载mysql的repo源
    wget http://repo.mysql.com/mysql-community-release-el7-5.noarch.rpm

# 2、安装mysql-community-release-el7-5.noarch.rpm包
    rpm -ivh mysql-community-release-el7-5.noarch.rpm

# 3、安装mysql
    yum install mysql-server

# 4、授权用户可以使用mysql
    chown -R root:root /var/lib/mysql

# 5、重启服务
    service mysqld restart

# 6、接下来登录重置密码：    
    mysql -u root        # 进入mysql
    
        # 下面为mysql命令        
        use mysql;            
        update user set password=password('root') where user='root';            
        grant all privileges on *.* to 'root'@'%' identified by 'root';  #设置远程登陆密码
        flush privileges;      #刷新当前配置    注：如果不管用，重启虚拟机ctrl+c,退出myql
			
# 7、开放3306端口：
    # 设置 iptables service
	yum -y install iptables-services

    # 如果要修改防火墙配置，如增加防火墙端口3306
	vi /etc/sysconfig/iptables 

    # 增加规则
	-A INPUT -p tcp -m state --state NEW -m tcp --dport 3306 -j ACCEPT   #保存退出后

# 8、配置防火墙: 服务器运行不需要这个步骤
    systemctl restart iptables.service     # 重启防火墙使配置生效
    systemctl enable iptables.service      # 设置防火墙开机启动
```

#### 连接MySQL数据库，并新建一个库以备的django使用

- ##### 使用navicat连接数据库

  ![navicat-1](D:\学习资料\北网学习\课堂笔记\03-数据分析第三阶段\三阶段图片\LInux服务器部署\navicat-1.png)

- ##### 打开navicat以后，点击右上角的连接，弹出以下窗口，按下图中的内容填写

  ![数据库连接](D:\学习资料\北网学习\课堂笔记\03-数据分析第三阶段\三阶段图片\LInux服务器部署\数据库连接.png)

- ##### 新建数据库，以便的django连接

  ![新建数据库](D:\学习资料\北网学习\课堂笔记\03-数据分析第三阶段\三阶段图片\LInux服务器部署\新建数据库.png)

  > #### 数据库已经建好，下面就是django配置数据库

#### django配置MySQL数据库

```python
# 1、在settings文件中，把数据库配置地方更改为以下内容：
DATABASES = {
	'default': {
        'ENGINE': 'django.db.backends.mysql',  # 默认数据库为MySQL
        'NAME': 'library',  # 数据库名为library
        'USER': 'root',  # 连接数据库的用户 "root"
        'PASSWORD': '123456',  # 用户密码  "123456"
        'HOST': 'www.donghaiming.cn',  # 主机的IP或者域名都可以
        'PORT': 3306,  # 数据库端口，默认为3306
	}
}
```

#### django项目目录下的__init__.py文件中，导入pymysql

```python
import pymysql
pymysql.install_as_MySQLdb()
```



### CentOS7安装虚拟环境

```python
# 安装虚拟环境
pip3 install virtualenv

# 创建软链接
ln -s /usr/local/python3/bin/virtualenv /usr/bin/virtualenv
```

#### 创建目录

```python
# 创建报错虚拟环境目录  名字是任意的
mkdir  -p /data/env   
# 个人网站发布文件夹 .名字都是任意的!
mkdir  -p /data/wwwroot
```

#### 创建、进入虚拟环境

```python
# 进入env目录
cd  /data/env
# 创建虚拟环境
virtualenv --python=/usr/bin/python3 py3_django2
# 激活虚拟环境
cd  /data/env/py3_django2/bin
source  activate  #  退出:  deactivate
# 安装django、uwsgi等.
pip install django
pip install uwsgi  # django项目发布相关
# 退出虚拟环境
cd  /data/env/py3_django2/bin
deactivate 
```

#### 为uwsgi创建软链接

```python
# 给uwsgi建立软链接，方便使用
ln -s /usr/local/python3/bin/uwsgi /usr/bin/uwsgi
```

#### 创建xml文件，保存名字与项目名同名，后缀为.xml

```xml
<?xml version="1.0" encoding="UTF-8"?>
<uwsgi>    
   <socket>127.0.0.1:8000</socket> <!-- 内部端口，自定义 --> 
   <chdir>/data/wwwroot/library/</chdir> <!-- 项目路径 -->            
   <module>library.wsgi</module>  <!-- wsgi.py所在目录名--> 
   <processes>4</processes> <!-- 进程数 -->     
   <daemonize>uwsgi.log</daemonize> <!-- 日志文件 -->
</uwsgi>
```

#### 本地项目上传到CentOS7服务器上

```python
# 1、在windows系统下，用cmd进入项目的目录，生成项目包依赖列表（如果依赖包少的话，这一步忽略）
pip freeze > requirements.txt
# 2、settings文件设置
ALLOWED_HOSTS = ['*']  # 允许所有IP访问
```

#### CentOS7下安装相关依赖包

```python
# CentOS7下安装相关依赖包（如果依赖包少的话，这一步忽略）
pip install -r requirements.txt
```

#### 迁移静态文件

```python
# 一、指定收集静态文件的目录，修改settings文件中静态文件路径	
    STATIC_ROOT = '/data/wwwroot/library/static'    

# 二、收集所有静态文件到STATIC_ROOT指定的目录
	python3 manage.py collectstatic
```

#### 安装Nginx

```python
# 1、用wget下载Nginx
wget http://nginx.org/download/nginx-1.13.7.tar.gz
    
# 2、下载完成后，解压
tar -zxvf nginx-1.13.7.tar.gz

# 3、进入到nginx-1.13.7目录下，并执行以下命令
cd nginx-1.13.7
./configure
make && make install

# 4、nginx一般默认安装好的路径为/usr/local/nginx 在/usr/local/nginx/conf/中先备份一下nginx.conf文件，以防意外。
cd /usr/local/nginx/conf/
cp nginx.conf nginx.conf.bak

# 5、然后打开nginx.conf，把原来的内容删除，直接加入以下内容：
events {
    worker_connections  1024;
}
http {
    include       mime.types;
    default_type  application/octet-stream;
    sendfile        on;
    server {
        listen 80;
        server_name  www.donghaiming.cn; #改为自己的域名，没域名修改为127.0.0.1:80
        charset utf-8;
        location / {
           include uwsgi_params;
           uwsgi_pass 127.0.0.1:8000;  #端口要和uwsgi里配置的一样
           uwsgi_param UWSGI_SCRIPT library.wsgi;  #wsgi.py所在的目录名+.wsgi
           uwsgi_param UWSGI_CHDIR /data/wwwroot/library/; #项目路径
           
        }
        location /static/ {
        alias /data/wwwroot/library/static/; #静态资源路径
        }
    }
}

""" 
6、 
要留意备注的地方，要和UWSGI配置文件mysite.xml，还有项目路径对应上。 
进入/usr/local/nginx/sbin/目录
执行./nginx -t命令先检查配置文件是否有错，没有错就执行以下命令：
"""
cd /usr/local/nginx/sbin/
./nginx

# 没有提示，证明成功
# 测试
127.0.0.1：80  

```

#### 启动项目

```python
# 进入djnago项目
cd /data/wwwroot/library/

# uwsgi 解析项目中的配置文件
uwsgi -x library.xml

#以上步骤都没有出错的话。
cd /usr/local/nginx/sbin/

# 重启nginx
./nginx -s reload

# 服务器内部测试是否发布成功
curl 1270.0.0.0:80  #就可以看到网站!
    
# 关闭防火墙,否则远程不能访问!服务器运行不需要这个步骤
    systemctl stop firewalld.service
```





####     

