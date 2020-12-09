#### 概要

Ajax 即“Asynchronous Javascript And XML”（异步 JavaScript 和 XML），是指一种创建交互式网页应用的网页开发技术。


局部刷新技术。


应用场景：
    在页面比较复杂情况下，只需要更新局部内容。
    
    
    
#### 语法

1. GET请求
```
var data = {'uname':'zhangsan'}

    //发送ajax请求
    $.get('/student/getinfo/',data,function(result){

        alert(result.hello)
    })
    
    
```
 
2. POST请求
```
 var csrf = $('input[name="csrfmiddlewaretoken"]').val();
 var data = {'uname':'zhangsan','csrfmiddlewaretoken':csrf}
 $.post('/student/getinfo/',data,function(result){
                alert(result.hello)
            })

```
3. 自定义AJAX请求
```

 $.ajax({
            url:'/student/getinfo/',
            type:'get',
            data:'uname=lisi&pwd=123',
            async:true,
            success:function (result) {
                var test = result.hello

                $('#hid').html(test)
            }

        })



```