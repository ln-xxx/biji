#### Git下载安装
    windows版本下载地址:https://git-scm.com/download/win
    
#### 使用前准备
    1. 安装完成后，在开始菜单里找到“Git”->“Git Bash”，弹出命令行窗口，说明Git安装成功。
    2. 安装Git之后，你要做的第一件事情就是去配置你的名字和邮箱，因为每一次提交都需要这些信息。
```
$ git config --global user.name "Your Name"
$ git config --global user.email "Your email@example.com"

```

- 这个命令，会在“ ~/.gitconfig”中以如下形式输出设置文件。
```
[user]
name = Your_Name
email = Your_email@example.com

```


- 将 color.ui 设置为 auto 可以让命令的输出拥有更高的可读性。

```
$ git config --global color.ui auto

```


- ~/.gitconfig”中会增加下面一行。
```

[color]
ui = auto

```


