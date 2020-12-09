# virtualenvwrapper

> virtualenv 可以方便的创建虚拟环境, 但是有以下不足:
>
> 1. 创建的虚拟环境在当前操作的目录下, 不方便管理,(如果每次创建虚拟环境能够自己放到统一的地方管理就好啦)
> 2. 进入虚拟环境, 需要先进入到虚拟环境所在的目录下的scripts文件夹下, 然后执行activate.(如果不用进入目录直接就能通过一个命令进入虚拟环境就好啦)

###1.	virtualenvwrapper简介：

`virtualenvwrapper`这个软件包可以让我们管理虚拟环境变得更加简单。不用再跑到某个目录下通过`virtualenv`来创建虚拟环境，并且激活的时候也要跑到具体的目录下去激活。

###2.	安装`virtualenvwrapper`：

1. *nix：`pip install virtualenvwrapper`。
2. windows：`pip install virtualenvwrapper-win`。

> 实际开发时, 其实没有必要先安装virtualenv再安装virtualenvwrapper这样操作
>
> 可以直接安装virtualenvwapper, 会自动将virtualenv安装下来

###3. `virtualenvwrapper`基本使用：

1. 创建虚拟环境：

   ```
    mkvirtualenv 虚拟环境名
   ```

   那么会在你当前用户下创建一个`Envs`的文件夹，然后将这个虚拟环境安装到这个目录下。
   如果你电脑中安装了`python2`和`python3`，并且两个版本中都安装了`virtualenvwrapper`，那么将会使用环境变量中第一个出现的`Python`版本来作为这个虚拟环境的`Python`解释器。

2. 切换到某个虚拟环境：

   ```
    workon my_envde
   ```

3. 退出当前虚拟环境：

   ```
    deactivate
   ```

4. 删除某个虚拟环境：

   ```
    rmvirtualenv my_env
   ```

5. 列出所有虚拟环境：

   ```
    lsvirtualenv
   ```


#### 1.6.3    修改`mkvirtualenv`的默认路径：

在`我的电脑->右键->属性->高级系统设置->环境变量->系统变量`中添加一个参数`WORKON_HOME`，将这个参数的值设置为你需要的路径。

#### 1.6.4    创建虚拟环境的时候指定`Python`版本：

在使用`mkvirtualenv`的时候，可以指定`--python`的参数来指定具体的`python`路径：

```
    mkvirtualenv --python==C:\Python36\python.exe [virutalenv name]
```

