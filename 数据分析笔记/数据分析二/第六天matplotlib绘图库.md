# 第六天matplotlib绘图库

### pyecharts补充

![1547003591823](C:\Users\ADMINI~1\AppData\Local\Temp\1547003591823.png)




1. 北京各区的房源数量

2. 导出图片

   * nodejs + 魔法.环境js库

     ~~~python
     #安装nodejs
     #替换淘宝镜像[从阿里服务器下载资源,速度快]
     #npm install -g phantomjs-prebuilt 这是从国外服务器下载  速度超慢
     #替换命名 :npm install -g cnpm registry=https://registry.npm.taobao.org
     #然后执行--->  cnpm install -g phantomjs-prebuilt
     
     #重启  notbook
     #使用 bar.render(r'D:/a.png/jpeg/svg/pdf')
     ~~~

**测试安装成功**

![1546995514705](C:\Users\ADMINI~1\AppData\Local\Temp\1546995514705.png)

### matplotlib画图



**简介:是数据分析绘图的基础库~**

**核心:绘制二维图的子库  matplotlib.pyplot**

**画图: plt.plot(x,y) 默认是折线图**

**x/y标签:plt.xlable('名字',fontproperties='SimHei',fontsize=18)**

**保存为图片:  plt.savefig()**

**展示图片: plt.show()**

### 案例

1. **折线图**

~~~python
"""
美国失业率折线图
"""
import matplotlib.pyplot as plt

df = pd.read_csv(r'C:\Users\Administrator\Desktop\stu_info\UNRATE.csv')
cs = df[:12]

#画图 折线图
plt.plot(cs['DATE'],cs['VALUE'])
plt.title('美国失业率')
plt.xlabel('x')
plt.ylabel('y')
plt.xticks(rotation=50)
plt.show()
~~~



![1546999189783](C:\Users\ADMINI~1\AppData\Local\Temp\1546999189783.png)



2. **饼状图**

~~~python
"""
饼状图  那女比例
"""
df1 = pd.read_csv(r'C:\Users\Administrator\Desktop\stu_info\titanic_train.csv')
df2 = df1['Sex'].value_counts()

#画图
plt.rcParams['font.sans-serif'] = ['SimHei']  #设置全局显示汉子
plt.pie(df2,labels=['男','女'],shadow=True,autopct='%1.2f%%')
plt.axis('equal')
plt.show()
~~~



![1546999301349](C:\Users\ADMINI~1\AppData\Local\Temp\1546999301349.png)

~~~python
"""
成年人和未成年人获救概率
"""
df1 = pd.read_csv(r'C:\Users\Administrator\Desktop\stu_info\titanic_train.csv')
def age_old(b):
    
    c = b['Age']
    if c > 18:
        return '成年'
    elif c < 18:
        return '未成年'
    else:
        return '空值'
#创建新列 
df1['chegnnian'] = df1.apply(age_old,axis=1)
all_info = df1.groupby(by=['Survived','chegnnian']).size()


#画图
plt.pie(all_info,labels=['成年未获救','未成年未获救','空值未获救','成年获救','未成年获救','空值获救'],shadow=True,autopct='%1.1f%%',explode=(0,0.02,0.05,0.08,0.1,0.12))
plt.axis('equal') #设置圆的形状 正圆
plt.show()
~~~

![1547036705341](C:\Users\ADMINI~1\AppData\Local\Temp\1547036705341.png)

3. **柱状图**

~~~python
"""
美国失业率柱状图
"""
import matplotlib.pyplot as plt

df = pd.read_csv(r'C:\Users\Administrator\Desktop\stu_info\UNRATE.csv')
cs = df[:12]

#柱状图    bar   barh
plt.barh(cs['DATE'],cs['VALUE'])
plt.xlabel('x')
plt.ylabel('y')
plt.xticks(rotation=50)
plt.show()
~~~





![1546999355043](C:\Users\ADMINI~1\AppData\Local\Temp\1546999355043.png)



![1547001727525](C:\Users\ADMINI~1\AppData\Local\Temp\1547001727525.png)

4. **地图**

~~~python
"""
北京各区房源分析
"""
import numpy as np
import pandas as pd
from pyecharts import Map

df = pd.read_csv(r'C:\Users\Administrator\Desktop\stu_info\house.csv')
df2 = df.groupby('地区').size()
x_zhi = [x+'区' for x in df2.index.format()]
y_zhi = np.array(df2)
#画图
map = Map('北京各区房源信息',width=600, height=500)
map.add('房源信息',x_zhi,y_zhi,maptype='北京',is_label_show=True,is_visualmap=True)
map
~~~



![1547036367881](C:\Users\ADMINI~1\AppData\Local\Temp\1547036367881.png)



















