



# 初始PYTHON

* www.cnblogs.com/wupeiqi/articles/543893,html

  * 程序
  * 博客地址(注册一个 账号)

* 开发：

  * 开发语言

    * 高级语言python，JAVA,  C++,PHP,GO,RUBY,C#,  写的时候简单，  高级语言后边用的都是C语言====（字节码）
    * 低级语言c，汇编  （执行效率高，开发效率低）===（010101）
    * 机器码（010101）   和字节码（高级语言的码   ，   ）

  * 语言之间的对比：（以后一定要学习C语言  学习成本高      ，

    * Java  和python 是一类开发软件  可以写网站，和后台， 
    *  php是自己的软件 快速搭建，是适合做网站 ）
    * Java的执行效率高，开发效率底
    *    python开发效率高   。执行效率低 

    ![](C:\Users\86184\Desktop\python笔记\第一月\images\1559367969(1).jpg)

    

  * python的种类：

    * jpython
    * lronpython
    * cpython
    * JavaScriptpython
    * 。。。。
    * pypy这是运用PYTHON开发的PYTHON
    * ![](C:\Users\86184\Desktop\python笔记\第一月\images\1559368456(1).jpg)

  * 安装：

    * python安装在OS上，
    * 执行操作
    * 写一个文件按照python的规则写，将文件交给python软件，然后进行转化和执行，最终取得结果。
    * python软件   python简释器  （内存管理）

  * 下载

    * python3      在继续更新

    * python2     在继续更新（更新到最后就和3一样是一个 慢慢改变的东西。）

    * window: ....
      * python2
      * python3
      * 环境变量：
      * 配置环境变量

    * lindow:
      * python2
      * python3

    * 变量名

      * 字母
      * 数字
      * 下划线

    * ps：

      * 数字不能开头
      * 不能是关键字   closs  and
      * 不能用python中的内置的东西重复
    * 定义的变量名要有意义

* python基础
  * 基础

    * 第一句Python     -后缀名是任意的

    * 导入模块时，如果不是py文件

    * ==<以后文件后缀名是。py

      * ​		两种执行方式
      * python简释器 py文件路径
      * python   进入简释器：
        * 实时输入并获取到执行结果

    * 简释器路径

      * # ！/usr/bin/env python

    * 4编码

      * # -*-conding：utf8 -*-

      * ascill        只有8位码

      * unicode   至少16为码

      *    能用多少表示就用多少表示  

    * 5执行一个复杂的操做

      * 提醒用户输入：用户和密码
      * 获取用户名和密码，  检测：用户名=root  密码=root
      * 真确表示登录成工   否则登录失败

    * ```python
      print ('holle,word')
      
      
      inpot（’请输入用户名‘）
      prin（'你好，李宁'）
      
      ```

      

  * 基本数据类型

    * 字符串  用引号引着的都是字符串
    * name=‘李宁’
    * name=“李宁”
    * neme=“”“李宁”“”

  * 加法  a=“ales”

  * b=“sb”

  * c=“db”

  * d=a+b+c

  * 乘法 

  *  a='alex'

  * b=a*10

  * ![](C:\Users\86184\Desktop\python笔记\第一月\images\1559381211(1).jpg)

    * 除法  /	
    * %÷玩取余
      * //÷玩取商：
      * ​            内部代码块
      * ​          内部代码块
      *    else：
      * 。。。。。
      * print（‘。。。。‘）
      * 
    * if   条件

  * 条件语句

    * 

  * 函数’

  * 面向对象

* 网络编程

* web框架         
  * 用于写网站

* 设计模式 +算法     

* 项目阶段   

```python
a=0
while a<3:
    user=input("请输入账号")
    pwd=input("请输入密码")
    if user=='alex' and pwd=='123':
        print('欢迎登录')
        print ('我爱我家 ，喜欢你没道理' )
        break
else:
    piint('用户名或者密码错误')
    a=a+1
    
```


*  count     去字符串中寻找   寻找子序列出现的次数
* endswith    以什么结尾
* startswith   以什么开始
* find    从开始往后找   找到第一个后获取他的位数
* format     格式化将一个字符串中的占位符替换（按照占位符顺数替换）