# 第七天matplotlib画图

# **简介**

**是画图的基础库,非常重要~~**

**官网:**https://matplotlib.org/

官网核心资料:案例   教程   API手册

核心:学会绘制各种常用的数据分析图:

* **折线 line/plot**  
* **柱状图  bar/barh/堆叠图/直方图**
* **饼状图   pie**
* **散点图   scatter**
* **箱图    boxplot**

**到入库**

~~~python
import matplotlib.pyplot as plt

~~~

![2](C:\Users\Administrator\Desktop\1804数据分析第二个月\img\2.webp)

* 画图大小  plt.figure(figsize=())
* lengend   图例
* line/plot 折线
* scatter  散点
* title       标题

**画图**

**1.	折线图plot()**

* 每个折线图的名字  label='名字'

* 显示图裂  plt.legend()

* 颜色样式缩写  r 表示颜色的缩写    -实线   --虚线   o圆形   

  * **颜色**

    支持以下颜色缩写：

    | 字符  | 颜色 |
    | ----- | ---- |
    | `'b'` | 蓝色 |
    | `'g'` | 绿色 |
    | `'r'` | 红色 |
    | `'c'` | 青色 |
    | `'m'` | 品红 |
    | `'y'` | 黄色 |
    | `'k'` | 黑色 |
    | `'w'` | 白色 |

  * **标记**

    | 字符  | 描述               |
    | ----- | ------------------ |
    | `'.'` | 点标记             |
    | `','` | 像素标记           |
    | `'o'` | 圆圈标记           |
    | `'v'` | triangle_down标记  |
    | `'^'` | triangle_up标记    |
    | `'<'` | triangle_left标记  |
    | `'>'` | triangle_right标记 |
    | `'1'` | tri_down标记       |
    | `'2'` | tri_up标记         |
    | `'3'` | tri_left标记       |
    | `'4'` | tri_right标记      |
    | `'s'` | 方形标记           |
    | `'p'` | 五边形标记         |
    | `'*'` | 明星标记           |
    | `'h'` | hexagon1标记       |
    | `'H'` | hexagon2标记       |
    | `'+'` | 加上标记           |
    | `'x'` | x标记              |
    | `'D'` | 钻石标记           |
    | `'d'` | thin_diamond标记   |
    | `'|'` | vline标记          |
    | `'_'` | hline标记          |

  * **线条样式**

    | 字符   | 描述       |
    | ------ | ---------- |
    | `'-'`  | 实线风格   |
    | `'--'` | 虚线样式   |
    | `'-.'` | 点划线样式 |
    | `':'`  | 虚线样式   |

  * 示例格式字符串：

    ```python
    'b'    # blue markers with default shape
    'ro'   # red circles
    'g-'   # green solid line
    '--'   # dashed line with default color
    'k^:'  # black triangle_up markers connected by a dotted line
    ```

~~~python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
"""
美国失业率 折线图
"""
df = pd.read_csv(r'C:\Users\Administrator\Desktop\stu_info\UNRATE.csv')

#画图
"""
1.折线图 表示美国失业率1948/1949 失业率对比
    linewidth=5     线的宽度
    color           线条颜色
    linestyle  =''  线条形状
    plt.legend()    #图例
    label           图例的别名
"""
num12 = df[:12]
num24 = df[12:24]
x = [i[5:] for i in num12['DATE']]
#x2 = [i[5:] for i in num24['DATE']]
y = num12['VALUE']
y2 = num24['VALUE']
plt.rcParams['font.sans-serif']=['SimHei']
plt.plot(x,y,'b--',linewidth=5,label='1948')
plt.plot(x,y2,'ro',linewidth=5,label='1949')
plt.legend() #图例
#plt.savefig(r'C:\Users\Administrator\Desktop\1804数据分析第二个月\img\1.svg')
plt.xlabel('月份')
plt.ylabel('失业率')
plt.title('标题')
plt.xticks(rotation=45)
plt.show()
~~~



![1](C:\Users\Administrator\Desktop\1804数据分析第二个月\img\1.svg)

### 图片的大小和保存

~~~python
#设置图形大小   默认100px
plt.figure(figsize(4,5))
#保存图片
plt.savefig(路径)
~~~

**全局参数设置**

~~~python
#全局属性替换
plt.rcParams['font.sans-serif']=['SimHei']  
plt
plt.style.user('grayscale')
~~~



2. **柱状图**

   1. bar(x,y,color='r')
   2. barh(x,y,color='r')
   3. 堆叠 bar(x,y,color='r',bottom='另一组数据的y周')
   4. 直方图  hist()

   ~~~python
   num12 = df[:12]
   num24 = df[12:24]
   x = [i[5:] for i in num12['DATE']]
   x2 = [i[5:] for i in num24['DATE']]
   y = num12['VALUE']
   y2 = num24['VALUE']
   
   #堆叠  bottom
   plt.bar(x,y,color='y')
   plt.bar(x,y2,color='r',bottom=y)
   plt.show()
   ~~~

   ![4](C:\Users\Administrator\Desktop\1804数据分析第二个月\img\4.png)

3. **散点图**

   1. **plt.scatter(x,y,c='颜色',s='大小',marker='o/s/+//^形状')**
   2. **plt.scatter('x轴对应的列名','y轴对应的列名,data=数据源)**

   ~~~pyhton 
   """
   4  散点图scatter
   
   """
   
   #df = pd.DataFrame(np.random.randn(10,2),columns=list('AB'))
   num12 = df[:12]
   num24 = df[12:24]
   x = [i[5:] for i in num12['DATE']]
   x2 = [i[5:] for i in num24['DATE']]
   y = num12['VALUE']
   y2 = num24['VALUE']
   #画图  c/color='r'设置颜色   marker=''设置形状  linewudtg=数字  设置大小
   plt.scatter(x,y)
   plt.scatter(x,y2)
   plt.show()
   ~~~

   ![5](C:\Users\Administrator\Desktop\1804数据分析第二个月\img\5.png)

4. **饼状图**

   * **pie(列名,labels=[标签名称],shadow=True,autopct='%1.2f%%')**

   ~~~python 
   df1 = pd.read_csv(r'C:\Users\Administrator\Desktop\stu_info\titanic_train.csv')
   
   a = df1.groupby(by=['Sex','Survived']).size()
   #画图
   labels=['女未获救','女获救','男未获救','男获救']
   explode = (0,0.2,0,0)  #设置爆炸凸起的效果
   plt.pie(a,
           explode=explode,
           shadow=True,
           autopct='%1.2f%%',
           startangle=90,
           labels=labels)
   plt.axis('equal')  #变元
   plt.show()
   
   ~~~

   ![3](C:\Users\Administrator\Desktop\1804数据分析第二个月\img\3.png)






**箱图  反应数据的集中分布趋势**

- 箱子内数据表示集中分布
- 箱子内有2个标记:平均值,中位数标记
- 箱子2端:圈点表示异常情况