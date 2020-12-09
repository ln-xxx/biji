#### 确定需求
```
#访问路径：
http://127.0.0.1:8000/student/only/

```

#### 配置URL

```
# 项目包/urls.py
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^student/', include('stu.urls')),
]

# 应用包/urls.py
#coding=utf-8

from django.conf.urls import url
import views

urlpatterns=[
    url(r'^only/$',views.onlyView),
    url(r'^isExist/$',views.existView),
]



```

#### 创建视图
```
def onlyView(request):

    return render(request,'only.html')


def existView(request):
    #接收请求参数
    uname = request.GET.get('uname','')

    #判断数据库中是否存在
    stuList = Student.objects.filter(sname=uname)

    if stuList:
        return JsonResponse({'flag':True})
    return JsonResponse({'flag':False})


```

#### 创建模板页面（only.html）
```

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>

    <script type="text/javascript" src="http://apps.bdimg.com/libs/jquery/1.9.0/jquery.min.js"></script>
    <script>
        //onblur:失去焦点
        //onfocus:获得焦点

        function checkUname(){
            //1.获取文本框内容
            var uname = $('#uname').val();

            //2.非空校验
            if(uname.length==0){
                $('#unameSpan').html('*');
                $('#unameSpan').css('color','red');

            }else{
            //3.判断唯一性
                $.get('/student/isExist/',{'uname':uname},function(result){
                    //alert(typeof result.flag)
                    r = result.flag;

                    //4.根据服务器端的响应信息进行页面更新
                    if(r){
                        $('#unameSpan').html('此用户名太受欢迎了，请换一个吧~');
                        $('#unameSpan').css('color','red');
                    }else{
                        $('#unameSpan').html('√');
                        $('#unameSpan').css('color','green');

                    }
                })




            }


        }

    </script>
</head>
<body>
    用户名：<input type="text" name="uname" id="uname" onblur="checkUname()"/><span id="unameSpan"></span>

</body>
</html>

```



















