# linux入门

linux服务器搭建工作需要掌握的核心点

1. 虚拟机的使用
2. linux安装(注意)
3. 服务器的搭建(重点)
   1. 网络配置(本地虚拟机/阿里云服务器已经联网了)
   2. SSH连接远程(putty)
   3. FTP文件传输(Winscp)
   4. 升级python(linux默认自带的是2.7版本的python)
   5. 虚拟环境管理(virtualenv)
   6. django
   7. web服务器(nginx+uwsgi)做django项目发布
   8. 数据库Mysql
   9. DNS解析实现
   10. nginx多项目配置

###1.虚拟机认识



重要功能:

* 快照功能(保存系统当前状态,后期便于随时还原)
* 克隆(完全复制一份)
* 删除虚拟机



### 2.安装系统

**虚拟机安装[重要]：https://blog.csdn.net/qq_39038465/article/details/81478847**

北网周正杨老师:
https://blog.csdn.net/qq_39038465/article/details/81478847



* 必须为虚拟机打开网络
  * 桥接(虚拟机相当于一台电脑,有独立的IP)
  * NAT(电脑太多是使用)
* 硬盘分区
  * boot(系统引导分区,存储是启动相关的核心文件,一般是200到500m)
  * swap内存交换分区(充当内存使用,内存的2倍)
  * /根分区:剩余所有空间
* 记住自己的IP



## 查看自己的IP地址

~~~linux
ifconfig
ip addr
~~~



###3.连接服务器

SSH:是客户端和linux服务器传输的加密协议!特点:安全,数据压缩,(传输速度快)

CentOs:服务器默认安装了SSH

windows电脑需要安装SSH客户端就可以和服务器进行SSH加密通信

常用的SSH客户端 PUTTY

核心配置(配置IP+端口(22),窗口显示行列,字体大小)



### 4.使用FTP协议传文件

常用的FTP协议软件 winScp



在根目录上传一个文件""""



### 5.虚拟机联网

* 桥连接(每个虚拟的系统都相当于一个真实电脑,内网自动分一个IP)

* NAT方式:

  列如:

  192.168.(1==254).(2===254) 该网段可分给1-254台电脑,可组建很庞大的内网系统

* 自连接:只能主机和虚拟机通信

* 建议使用桥接模式



* 最快联网设置

  * 多太虚拟机都设置为桥接',启动时自动分配内网的IP地址

  * 打开虚拟机的联网功能

    * 安装时打开
    * 手动更改配置文件,打开

    ~~~linux
    #windows系统   ipconfig -all
    #打开网络配置文件 vi是编辑文件的命令
    vi /etc/sysconfig/network-scripts/ifcfg-ens33
    #固定IP 修改内容如下
    
    BOOTQPOTO = 'static' #手动分配IP
    
    #改完重启网络
    serviec network restart
    ~~~




DNS和网关信息可在window电脑:cmd_ipconfig中查看

VI编辑器使用

1. vi 文件名
2. 进入编辑模式
3. 改
4. ESC退出, :wq 保存退出   :q!不保存直接退出



### 检测网络是否能连接网络

主机和虚拟机之间相互ping

ping  ip地址





## 6.linux目录结构

**![img](file:///C:/Users/ADMINI~1/AppData/Local/Temp/msohtmlclip1/01/clip_image002.jpg)**

bin   存放二进制可执行文件(cd,ls,cat,mkdir等)

boot  存放用于系统引导时使用的各种文件

dev   用于存放设备文件

etc    存放系统配置文件(重要)

home  存放所有用户文件的根目录

lib    存放跟文件系统中的程序运行所需要的共享库及内核模块

mnt   系统管理员安装临时文件系统的安装点

opt    额外安装的可选应用程序包所放置的位置

proc   虚拟文件系统，存放当前内存的映射

root   超级用户目录

sbin   存放二进制可执行文件，只有root才能访问

tmp   用于存放各种临时文件

usr    用于存放系统应用程序，比较重要的目录/usr/local 本地管理员软件安装目录

var    用于存放运行时需要改变数据的文件



* 软件安装目录:／usr/local
* 系统配置： /etc
* 还可以操作: (home,root,opt较少)



## 7.下载软件

* 从yum 软件仓库中下载

yum软件源默认是国外的服务器,下载慢,建议替换成国内的,例如:清华

https://mirrors.tuna.tsinghua.edu.cn/help/centos/ 

* wget 网址下载

注意mini版本的,wget不可以用,需要重新安装

~~~linux
wget https://www.python.org/ftp/python/
~~~



* 直接FTP传到服务器

最快,下载好直接传过去

# 总结

1. **熟悉虚拟机操作(快照,克隆,打开,删除)**
2. **安装系统(网络,系统分区)**
3. **联网(桥接)**
4. **SSH远程协议**
5. **FTP协议**
6. **linux目录结构**
7. **下载软件**





**(第二天)**

## 软件安装

**问题:虚拟机经常连不上网?**

**问题描述:在班级内虚拟机连接正常,回到宿舍后发现连不上?**

**原因:局域网发生改变,IP地址也自动发生变化,因为桥接模式会自动从局域网中分一个IP地址,**

**步骤**

1. 确保联网方式是:桥接模式

2. 从虚拟机登录查看IP      查看命令 ifconfig/ip addr

3. 改网络配置文件

   ~~~linux
   #更改步骤
   vi /etc/sysconfig/network - scripts/ifcfg-ens33
   # i 进入编辑模式
   #改
   BOOTRPTO = 'dhcp' #ip地址改为动态分配
   #注释掉手动设置IP(网络服务器重启后会自动分配)
   
   
   
   #重启服务器
   servie network restart
   
   ~~~

4. 最后SSH(putty) 改IP重新登录



### 安装python

centos 默认安装python.2.7,

* 查看是否有python    python -v(大写)
* 查看详细的解析方式   which  python/ ls -al python*



接下来从网上找详细的流程,一定要先确认,是哪种方式安装?

* 修改python指令的软件的连接指向3.6
* 或者添加python3的指令,软件连接指向3.6

选第一中方式,详细步骤如下

~~~linux
# 1 下载包管理器:gcc
yum -y groupinstall "Development tools"
# 2 下载相关依赖
yum install openssl-devel bzip2-devel expat-devel gdbm-devel readline-devel sqlite-
devel
# 3. 上传pyton3.6.6.tgz 到安装目录 /usr/local
上传...,也可通过wget手动下载到/usr/local
# 4. 备份默认的python指令的连接!!!!
mv /usr/bin/python /usr/bin/python.bak
# 5. 解压 在安装目录加压
cd  /usr/local
tar -zxvf Python-3.6.6.tgz  #多了Python3.6.6 文件夹
# 6.进入 Python3.6.6,
cd Python-3.6.6
# 编译安装,指定安装路径 ./configure --prefix=安装目录
./configure --prefix=/usr/local/python3  #[管理工具和依赖包必须已经安装好]
# 7. 安装
cd Python-3.6.6
make 
# 安装把安装日志保存起来
make install  > my_install.log
# 把python3/lib 保存到配置文件中，保存在 /etc/ld.so.conf.d中,并执行ldconfig
echo "/usr/local/python3/lib" >> /etc/ld.so.conf
ldconfig  
# 8 .建连接
ln -s /usr/local/python3/bin/python3.6 /usr/bin/python
# 测试
pythton -V  #执行3.6.6 表示成功
~~~



**建立pip软连接**

~~~linux
#pip 
~~~





## 安装虚拟环境

**建议安装虚拟环境,便于管理不同的项目**

~~~linux
#安装
pip install virtualenv
#建立软连接
ln -s /usr/local/python3/bin/virtualenv /usr/bin/virtualenv
~~~



安装成功在根目录下建立两个文件夹,主要用于存放evn和网站文件

~~~linux
#创建报错的虚拟环境目录-p没有目录自动创建
mkdir -p/data/env
#个人网站发布文件夹  名字任意
mkdir -p/data/wwwroot
~~~

**创建指定版本的虚拟环境**

~~~liunx
#进入env目录
cd /data/env
#创建虚拟环境
virtualenv --python=/usr/bin/python3 py3_django2
#启动
cd /data/env/py3_django/bin
source activate
#退出
deactivate
#安装django
pip  install django
#退出虚拟环境
cd  /data/env/py3_django2/bin
deactivate 

# 安装uwsgi(web项目发布需要使用)
pip install uwsgi
#建立软连接
ln -s /usr/local/python3/bin/uwsgi /usr/bin/uwsgi
~~~

### 激活虚拟环境



### 本地项目上传到wwwroot(自己建的)目录

~~~linux
#!在项目根目录生成项目需要的依赖包文档描述
pip freeze > requirements.txt
~~~



**上传项目到wwwroot下,启动测试是否正常运行~~~**

~~~linux
#使用winscp 上传到 /data/env/wwwroot 
#测试项目是否正常启动
cd /data/env/py3_django/bin
#激活虚拟环境
source activate
#进入项目目录
cd /data/env/wwwroot/项目文件夹
#下载当前项目需要的python依赖包
pip install -r requirements.txt
#测试姓名是否正常
python manage.py  runserver

~~~

### 配置uwsgi

在mysite的项目根目录,新建mysite.xml配置文件,上传到data/wwwroot/mysite下,内容入下

~~~xml
<uwsgi>    
   <socket>127.0.0.1:8000</socket> <!-- 内部端口，自定义 --> 
   <chdir>/data/wwwroot/mysite/</chdir> <!-- 项目路径 -->            
   <module>mysite.wsgi</module>  <!-- mysite为wsgi.py所在目录名--> 
   <processes>4</processes> <!-- 进程数 -->     
   <daemonize>uwsgi.log</daemonize> <!-- 日志文件 -->
</uwsgi>
~~~

保存注意<module> 里面的mysite ,为wsgi.py所在的目录名



### 下载nginx安装和配置

~~~python
#下载
cd /usr/local
wget http://nginx.org/download/nginx-1.13.7.tar.gz
#解压
tar -zxvf nginx-1.13.7.tar.gz
#进入目录
cd nginx-1.13.7
#一次执行命令
./configure --prefix=/usr/local/nginx make make install > my_nginx.log 
# nginx一般默认安装好的路径为/usr/local/nginx在/usr/local/nginx/conf/中先备份一下 nginx.conf文件，以防意外。 
cd /usr/local/nginx/conf/ 
cp nginx.conf nginx.conf.bak 
# 然后打开nginx.conf，把原来的内容删除，直接加入以下内容： 
events {    worker_connections  1024; } 
http {    include       mime.types;
         default_type  application/octet-stream;    sendfile        on;    server {        
             listen 80;        
             server_name  自己域名; #改为自己的域名，没域名修改为127.0.0.1:80        
             charset utf-8;        
             location / {           
                 include uwsgi_params;           
                 uwsgi_pass 127.0.0.1:8000;  #端口要和uwsgi里配置的一样           
                 uwsgi_param UWSGI_SCRIPT mysite.wsgi;  #wsgi.py所在的目录名+.wsgi           
                 uwsgi_param UWSGI_CHDIR /data/wwwroot/mysite/; #项目路径                   }        
                 location /static/ {        alias /data/wwwroot/mysite/static/; #静态资源路径        
                                   }   
             } 
         } 
                                    # 启动,执行./nginx -t命令先检查配置文件是否有错，没有错就执行以下命令： 
      cd  /usr/local/nginx/sbin/ 
      ./nginx 
      # 终端没有任何提示就证明nginx启动成功
      # 测试 
      curl 1270.0.0.0:80 
      #就可以看到网站!
 

~~~









### 启动django项目

~~~python
#进入django项目
cd /data/wwwroot/mysite/
#uwsgi 解析项目中的配置文件
uwsgi -x mysite.xml
#以上步骤没出错执行下一步
cd /usr/local/nginx/sbin/
#重启ngix
./nginx -s reload
#服务器内部测试是否发布成功
curl 127.0.0.0:80
 #关闭防火墙 测试远程
systeamctl stop firewalld.service

#最后用自己的IP进行测试

~~~



### 查看软件端口

通过监控端口命令,查看程序是否启动



~~~python
#查看进程端口号和运行的程序
netstat -atunp
#由端口号port(8000)查看进程id
netstat -anp |grep 8000
#停止
#杀死指定进程根据p id(进程id)uwsgi
kill pid
#强制杀死指定进程根据pid(进程id)ngix
kill -9 pid
~~~



























