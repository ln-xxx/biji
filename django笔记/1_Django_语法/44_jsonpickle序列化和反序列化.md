```

#coding=utf-8
from django.http import HttpResponse
from django.views import View
import jsonpickle

class User(object):
    def __init__(self,uname,pwd):
        self.uname = uname
        self.pwd = pwd



class IndexView(View):
    def get(self,request,*args,**kwargs):
        uname = request.GET.get('uname','')
        pwd = request.GET.get('pwd','')

        if uname=='zhangsan' and pwd=='123':
            user = User(uname,pwd)
            #{"py/object": "demo5.views.User", "uname": "zhangsan", "pwd": "123"}
            # ustr = jsonpickle.encode(user)

            # {"py/object": "demo5.views.User", "uname": "zhangsan", "pwd": "123"}
            ustr =jsonpickle.dumps(user)
            print ustr
            request.session['user'] = ustr

        return HttpResponse('Get请求')





class GetSession(View):
    def get(self,request,*args,**kwargs):
        user = request.session.get('user','')
        # <demo5.views.User object at 0x0000000003D48588>
        # uuser = jsonpickle.decode(user)

        # <demo5.views.User object at 0x0000000003D1A0F0>
        uuser = jsonpickle.loads(user)
        print uuser
        return HttpResponse('User:%s'%uuser.uname)


```



#### 序列化部分字段

```
class User(object):
    def __init__(self,uname,pwd):
        self.uname = uname
        self.pwd = pwd

    def __getstate__(self):
        data = self.__dict__.copy()
        del data['pwd']
        return data


u = User('zhangsan','123')       
s = jsonpickle.encode(u,unpicklable=False)
# jsonpickle.dumps(u,unpicklable=False)
print s
#{"uname": "zhangsan"}


```
