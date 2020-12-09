

#### 创建视图函数

```

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def page_view(request):
    num = request.GET.get('num',1)
    num = int(num)
    

    movies = Movie.objects.all()
    paginator = Paginator(movies,20)

    try:
        t_per_page = paginator.page(num)#获取当前页码的记录
    except PageNotAnInteger:#如果用户输入的页码不是整数时,显示第1页的内容
        t_per_page = paginator.page(1)
    except EmptyPage:#如果用户输入的页数不在系统的页码列表中时,显示最后一页的内容
        t_per_page = paginator.page(paginator.num_pages)
        
    
    
    #每页开始页码
    begin = (num-int(math.ceil(10.0/2)))
    if begin<1:
        begin = 1

    # 每页结束页码
    end = begin+9
    if end >pager.num_pages:
        end = pager.num_pages

    if end <=10:
        begin = 1
    else:
        begin = end -9

    pagelist = range(begin,end+1)

    return render(request,'movie2.html',{'paginator':paginator,'t_per_page':t_per_page,'pagelist':pagelist})

```

#### 配置模板

```

<div id="header"  class="clearfix">
        <ul class="clearfix">
            <li>首页</li>
            <li>电影</li>
            <li>电视剧</li>
            <li>动漫</li>
            <li>综艺</li>
            <li>音乐</li>
            <li>MV</li>
            <li>视频</li>
            <li>短片</li>
            <li>公开课</li>
        </ul>
    </div>
    <div id="content"  >
        <ul class="clearfix">
           {% for movie in t_per_page %}

               <li>
                   <a href="{{ movie.mlink }}"><img src="{{ movie.mimg }}"/></a>
                    <h1 class="h1">{{ movie.mname }}</h1>
                    <span class="tip">{{ movie.mdesc }}</span>
                </li>


           {% endfor %}



        
        </ul>
    </div>
    <div id="pagebar">
        {% if t_per_page.has_previous %}
            <a href="/movie/page/?num={{ t_per_page.previous_page_number }}">上一页</a>
        {% endif %}
        {% for n in paginator.page_range %}
            {% if n <= 10 %}
                <a href="/movie/page/?num={{ n }}">{{ n }}</a>
            {% endif %}


        {% endfor %}

        {% if t_per_page.has_next %}
            <a href="/movie/page/?num={{ t_per_page.next_page_number }}">下一页</a>
        {% endif %}

```













