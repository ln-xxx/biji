#### CSRF（Cross Site Request Forgery, 跨站请求伪造）
CSRF（Cross Site Request Forgery, 跨站域请求伪造）是一种网络的攻击方式，它在 2007 年曾被列为互联网 20 大安全隐患之一。其他安全隐患，比如 SQL 脚本注入，跨站域脚本攻击等在近年来已经逐渐为众人熟知，很多网站也都针对他们进行了防御。然而，对于大多数人来说，CSRF 却依然是一个陌生的概念。即便是大名鼎鼎的 Gmail, 在 2007 年底也存在着 CSRF 漏洞，从而被黑客攻击而使 Gmail 的用户造成巨大的损失。


#### Django的解决方法


Django预防CSRF攻击的方法是在用户提交的表单中加入一个csrftoken的隐含值，这个值和服务器中保存的csrftoken的值相同，这样做的原理如下:

1. 在用户访问django的可信站点时，django反馈给用户的表单中有一个隐含字段csrftoken，这个值是在服务器端随机生成的，每一次提交表单都会生成不同的值

2. 当用户提交django的表单时，服务器校验这个表单的csrftoken是否和自己保存的一致，来判断用户的合法性

3. 当用户被csrf攻击从其他站点发送精心编制的攻击请求时，由于其他站点不可能知道隐藏的csrftoken字段的信息这样在服务器端就会校验失败，攻击被成功防御

#### Django防攻击策略

1. 不推荐禁用掉django中的CSRF。

2. 我们可以再html页面的form表单中添加csrf_token，带着表单的请求一起发送到服务器去验证。
```
<form action  method="post" >
    {% csrf_token %}
</form>

```　　
3. 在后端一定要使用render()的方法返回数据。
```
return render(request, 'index.html', {'hello': '123})

全局：

中间件 django.middleware.csrf.CsrfViewMiddleware

局部：

@csrf_protect，为当前函数强制设置防跨站请求伪造功能，即便settings中没有设置全局中间件。

@csrf_exempt，取消当前函数防跨站请求伪造功能，即便settings中设置了全局中间件。

exempt:免除

注意：from django.views.decorators.csrf import csrf_exempt,csrf_protect

```






























