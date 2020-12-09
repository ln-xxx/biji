# linux常用命令

* 关机
  * shutdown -h now正常关闭,支持定时关机
    * -r表示重启
  * halt     关闭内存
  * init 0   有局限性,在6能用

* 查看系统版本

  * uname - a
  * cat /etc/redhat-release   这种方法只适合Redhat系的Linux：
  * cat /etc/issue 此命令也适用于所有的Linux发行版

  ## ls命令



  * ls -a 列出目录所有文件,包含以 . 开始的隐藏文件
  * ls -A 不包含隐藏文件
  * ls -r   反序排列
  * ls -S  以文件大小排序
  * ls -h   以易读大小显示
  * ls -l/ll   处理文件名,还将文件的权限,所有者,文件大小等信息详细列出来     
  * ls  -t  以文件修改时间排序
  *  ls | sed "s:^:`pwd`/:"   列出文件绝对路径(不包含隐藏文件)
  *  find $pwd -maxdepth 1 | xargs ls -ld 列出文件的绝对路径(包含隐藏文件)



## cd命令

命令语法：cd [目录名]。说明：切换当前目录至dirName

* 进入目录    cd/
* 进入家目录  cd~
* 进入上一次工作路径   cd -
* 把上个命令的参数作为cd参数使用     cd !$





## pwd命令

查看当前工作目录路径

* 查看当前路径   pwd
* 查看软链接的实际路径  pwd -P



## mkdir命令

创建文件夹

 -m: 对新建目录设置存取权限,也可以用chmod命令设置;

 -p: 可以是一个路径名称。此时若路径中的某些目录尚不存在,加上此选项后,系统将自动建立  		好那 些尚不在的目录,即一次可以建立多个目录;

* mkdir aa  创建名为aa的文件夹
* 在tmp目录下创建路径为test/t1/t的目录，若不存在，则创    mkdir -p /tmp/test/t1/t



## rm命令

























