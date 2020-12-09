#### 常用命令

##### 文件添加操作
```
# 1. 工作区中创建新文件hello.py
    $ vi hello.py

# 2. 查看文件状态
    $ git status

# 3. 将源码拷贝到暂存区
    $ git add hello.py

# 4. 将暂存区移动到当前分支
    $ git commit -m "创建新文件hello.py"

# 5. 查看状态
    $ git status
    On branch master
    nothing to commit, working tree clean


```

#### 文件删除操作
```
# 1. 删除工作区中的文件
    rm hello.py 
    
# 2. 删除暂存区中的文件
    git rm hello.py

# 3. 删除当前分支中的文件
    git commit -m '描述信息'



```

#### 文件修改操作
```
# 修改文件
    $ vi hello.py

# 查看状态
    $ git status

# 添加暂存区
    $ git add hello.py
    
# 添加版本库
    $ git commit -m '描述信息'
    
    
# 添加并提交到分支中
    $ git commit -am '描述信息'

```


#### 文件撤销操作

```
# 查看工作区和版本库里面最新版本的区别
    $ git diff HEAD -- hello.py
    
方式1：可以撤销未被追踪的文件
    
# 丢弃工作区的修改
    $ git checkout -- hello.py
    
方式2：可以撤销到任意版本
    # 查看操作日志
    $ git log
    commit c4e993ddb36d77710dad2c7c8c18130f9a761946 (HEAD -> master)

    $ git log --oneline
    c4e993d (HEAD -> master) first add
    
   
    
    # 回退到某个版本2
    $ git reset --hard c4e993ddb36d77710dad2c7c8c18130f9a761946


    #回退到上一个版本
    git reset HEAD
    
    
    



```

