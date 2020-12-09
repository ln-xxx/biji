
#### 配置视图

```

from django.core import serializers

def showMenuInfo(request):
    pid = request.GET.get('pid',-1)
    pid = int(pid)
    areaList = Area.objects.filter(parentid=pid)
    jAreaList = serializers.serialize('json',areaList)


    return JsonResponse({'areaList':jAreaList})

```



#### 配置模板页面

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <script type="text/javascript" src="http://apps.bdimg.com/libs/jquery/1.9.0/jquery.min.js"></script>

    <script>
        $(function(){
            showProvince();
        });

        function showProvince(){
            showArea('province',0,showCity);
        }

        function showCity(){
            showArea('city',$('#province').val(),showTown);
        }

        function showTown(){
            showArea('town',$('#city').val());
        }


        function showArea(selectId,pid,nextLoad){
            $('#'+selectId).empty();
            $.get('/stu/showMenu/',{'pid':pid},function(result){
                //将JSON字符串转成JSON对象
                areaList = JSON.parse(result.areaList);


                for(var i=0;i<areaList.length;i++){
                    var area = areaList[i];
                    $('#'+selectId).append("<option value='"+area.pk+"'>"+area.fields.areaname+"</option>")


                }

                if(nextLoad!=null){
                    nextLoad();
                }

            })
        }

    </script>
</head>
<body>



    <select id="province" onchange="showCity();"></select>
    <select id="city" onchange="showTown();"></select>
    <select id="town"></select>
</body>
</html>
```













