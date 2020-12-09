井号是root用户

$是普通用户

在linux中   蓝色的是文件甲   白色的是文件 绿色的是可执行文件  

exit   退出

ssh root  重启

cat  看文件

ls 看目录  ls -l   ====  ll

touch   创建

-l  显示文件的详细信息
-a 显示隐藏文件
-p 创建多个文件
mkdir   创建文件夹
touch   创建文件
cat  查看文件
 rmdir        删除空目录
r'm -r   
rm -rf 一次性彻底删除
rm -rf 文件名/*  删除文件夹内的子文件但保留文件夹



poweroff  关机  









mkdir  -p递归创建目录  mkdir /{a,b,c}

mkdir   -p    添加目

  rmdir  删除

rm   -  i   起的询问 作用

rm  -r    删除目录 可以删除有文件的目录

touch   添加  文件

rm   删除文件

rm  aa.py

rm =rf  强制删除 



mv   移动  类似于剪切   在同一目录下想当与改名

mv aa.py   bb.py   

 绝对路径   只要是在更目录下的都是绝对路径./ 

相对路径/

cd - 回到上次工作的目录

cd -

mv  -v    aa tmp cc

这是  移动改名字



存在目录  想当与添加（看作路径）

  不存在  就会改名 





mv   -v 显示过程 

mv -n同名移动保留原文     想到与没有移动



cp   复制功能

-r  复制文件夹

which是用来看自己敲得命令的



绿色的是可以执行的 文件



pwd 查看 当前目录的位置

whoami 查看当前用户

which   命令  查看命令的绝对路径 

poweroff  关机

reboot  重启

systemctl stop firewalld 关闭防火墙

iptablws -F 清空防火墙规则





退出当前会话  exit    ctr+d   logout 



软连接   （符号链接，）

ln -s 原始文件   绝对路径    目标文件









F文件

d   目录

  find +路径 -name +文件目录全称

find/ -name test.py

  cat 看文件

-b 列出序列   

查看 文件的方法  

cat  -n、显示行号开白行显示  /b显示行号  空白不显示 

more 看大文件 

less  显示大文件 可以向后翻页

tail   默认显示从结尾显示10行    

head   默认从开头显示10行 

 init 0 关机

who  用来看当前用户

date    用来看当前的时间

打包

tar -cvr bb.py.tar bb.py

tar -xvf b.py.tar -C /home

gzip,bzip2 压缩

tar -zcvf bb.py.tar.gz  bb.py  压缩带打包

tar -jcvf bb.py.tar.bz2 bb.py

tar -jxvf bb.py.tar.bz2 bb.py





/  更  目录

/home   家目录下的home

/etc  是保存配置文件     

/bin  可执行的二进制命令

