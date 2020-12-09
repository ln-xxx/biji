# 第一天数据结构简介DataFrame

### 数据帧

**DataFrame简介**

* **DataFrame**是一个二维标记数据结构，具有可能不同类型的列。您可以将其视为电子表格或SQL表，或Series对象的字典。它通常是最常用的pandas对象。与Series类似，DataFrame接受许多不同类型的输入:

  * 1D ndarray,list  dicts或者Series的Dict
  * 二维numpy.ndarray
  * 一个Series
  * l另一个DataFrame

  除了数据,您还可以选择传递索引(航标签)和 列(列标签) 参数.如果传递索引和/或列,则可以保证生产的DataFrame的索引和/或列.因此,系列的字典加上特定索引将丢弃与传递的索引不匹配的所有数据.

  如果未传递轴标签,则根据常识规则从输入数据构造他们.

### 索引/选择

索引的基础知识如下：

| 手术             | 句法            | 结果   |
| ---------------- | --------------- | ------ |
| 选择列           | `df[col]`       | 系列   |
| 按标签选择行     | `df.loc[label]` | 系列   |
| 按整数位置选择行 | `df.iloc[loc]`  | 系列   |
| 切片行           | `df[5:10]`      | 数据帧 |
| 按布尔向量选择行 | `df[bool_vec]`  | 数据帧 |



## ｎp.dot()



![1546500774491](C:\Users\ADMINI~1\AppData\Local\Temp\1546500774491.png)

### ndarray/list的字典

ndarray 必须都是相同的长度,如果传递索引,则它必须明显与数组的长度相同,如果没有传递索引,结果将是range(n),n数组长度在哪里

~~~python
In [41]: d = {'one' : [1., 2., 3., 4.],
   ....:      'two' : [4., 3., 2., 1.]}
   ....: 

In [42]: pd.DataFrame(d)
Out[42]: 
   one  two
0  1.0  4.0
1  2.0  3.0
2  3.0  2.0
3  4.0  1.0

In [43]: pd.DataFrame(d, index=['a', 'b', 'c', 'd'])
Out[43]: 
   one  two
a  1.0  4.0
b  2.0  3.0
c  3.0  2.0
d  4.0  1.0
~~~



### 从结构化或记录数组

这种情况的处理方式与数组的字典相同.

`注意:DataFrame并不像二维Numpy ndarray那样工作`

### 从dicts列表   列表套字典

~~~python
In [49]: data2 = [{'a': 1, 'b': 2}, {'a': 5, 'b': 10, 'c': 20}]

In [50]: pd.DataFrame(data2)
Out[50]: 
   a   b     c
0  1   2   NaN
1  5  10  20.0

In [51]: pd.DataFrame(data2, index=['first', 'second'])
Out[51]: 
        a   b     c
first   1   2   NaN
second  5  10  20.0

In [52]: pd.DataFrame(data2, columns=['a', 'b'])
Out[52]: 
   a   b
0  1   2
1  5  10
~~~



### 从元祖的词典

**可以通过传递元祖字典自动创建多索引框架**

# 备用构造函数

**DataFrame.from_dict**

* **DataFrame.from_dict采用dicts的dict或类似数组序列的dict并返回DataFrame.\;DataFrame除了默认情况下的`orient`参数外,他的操作类似于构造函数`columns`但可以将其设置`index`为使用dict建作为行标签**
* 如此通过 orient='index',则建将是行标签,还可以传递所需要的列名



**DataFrame.from_records**

* **DataFrame.from_records获取元祖列表或带有结构化dtypes的ndarray.他类似于普通DataFrame构造函数,但生产的DataFrame索引可能是结构化dtype的特定字段**

  ~~~python
  In [56]: data
  Out[56]: 
  array([(1,  2., b'Hello'), (2,  3., b'World')],
        dtype=[('A', '<i4'), ('B', '<f4'), ('C', 'S10')])
  
  In [57]: pd.DataFrame.from_records(data, index='C')
  Out[57]: 
            A    B
  C               
  b'Hello'  1  2.0
  b'World'  2  3.0
  ~~~


### 列 的  选择  添加  删除

* 取出某列
  * **数组.列名/数组['列名']**
* 添加新列
  * **数组['新列名'] = 值**
* 删除 某列
  * del 数组['列名']
  * 数组.drop('列名')
* **插入新列**
  * 数组.inser(插入的位置索引值,插入的列名,插入的值)

### 在方法链中分配新列

DataFrame有一种**assign()**方法可以轻松创建可能从现有列派生的新列

~~~python
In [71]: iris = pd.read_csv('data/iris.data')

In [72]: iris.head()
Out[72]: 
   SepalLength  SepalWidth  PetalLength  PetalWidth         Name
0          5.1         3.5          1.4         0.2  Iris-setosa
1          4.9         3.0          1.4         0.2  Iris-setosa
2          4.7         3.2          1.3         0.2  Iris-setosa
3          4.6         3.1          1.5         0.2  Iris-setosa
4          5.0         3.6          1.4         0.2  Iris-setosa

In [73]: (iris.assign(sepal_ratio = iris['SepalWidth'] / iris['SepalLength'])
   ....:      .head())
   ....: 
Out[73]: 
   SepalLength  SepalWidth  PetalLength  PetalWidth         Name  sepal_ratio
0          5.1         3.5          1.4         0.2  Iris-setosa       0.6863
1          4.9         3.0          1.4         0.2  Iris-setosa       0.6122
2          4.7         3.2          1.3         0.2  Iris-setosa       0.6809
3          4.6         3.1          1.5         0.2  Iris-setosa       0.6739
4          5.0         3.6          1.4         0.2  Iris-setosa       0.7200
~~~





**assign还可以传入函数**;`assign` **始终**返回数据的副本，保持原始DataFrame不变

~~~python
In [74]: iris.assign(sepal_ratio = lambda x: (x['SepalWidth'] /
   ....:                                      x['SepalLength'])).head()
   ....: 
Out[74]: 
   SepalLength  SepalWidth  PetalLength  PetalWidth         Name  sepal_ratio
0          5.1         3.5          1.4         0.2  Iris-setosa       0.6863
1          4.9         3.0          1.4         0.2  Iris-setosa       0.6122
2          4.7         3.2          1.3         0.2  Iris-setosa       0.6809
3          4.6         3.1          1.5         0.2  Iris-setosa       0.6739
4          5.0         3.6          1.4         0.2  Iris-setosa       0.7200
~~~



**从Python 3.6开始，`**kwargs`保留了顺序。这允许*依赖*赋值，其中稍后的表达式`**kwargs`可以引用先前在其中创建的列[`assign()`](http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.assign.html#pandas.DataFrame.assign)。**

~~~python
In [76]: dfa = pd.DataFrame({"A": [1, 2, 3],
   ....:                     "B": [4, 5, 6]})
   ....: 

In [77]: dfa.assign(C=lambda x: x['A'] + x['B'],
   ....:            D=lambda x: x['A'] + x['C'])
   ....: 
Out[77]: 
   A  B  C   D
0  1  4  5   6
1  2  5  7   9
2  3  6  9  12
~~~



**数据对齐和算术**

**DataFrame对象之间的数据对齐自动在列和索引(行标签)上对齐,同样,生成的对象将具有列和行标签的并集**

~~~python
df = pd.DataFrame(np.random.randn(10, 4), columns=['A', 'B', 'C', 'D'])
 df2 = pd.DataFrame(np.random.randn(7, 3), columns=['A', 'B', 'C'])
 df + df2
"""
        A       B       C   D
0  0.0457 -0.0141  1.3809 NaN
1 -0.9554 -1.5010  0.0372 NaN
2 -0.6627  1.5348 -0.8597 NaN
3 -2.4529  1.2373 -0.1337 NaN
4  1.4145  1.9517 -2.3204 NaN
5 -0.4949 -1.6497 -1.0846 NaN
6 -1.0476 -0.7486 -0.8055 NaN
7     NaN     NaN     NaN NaN
8     NaN     NaN     NaN NaN
9     NaN     NaN     NaN NaN
"""
~~~



**在DataFrame和Series之间进行操作时,默认行为是在Dataframe列上对齐Series索引,从而按行进行广播**

~~~python
df - df.iloc[0]
"""
        A       B       C       D
0  0.0000  0.0000  0.0000  0.0000
1 -1.3593 -0.2487 -0.4534 -1.7547
2  0.2531  0.8297  0.0100 -1.9912
3 -1.3111  0.0543 -1.7249 -1.6205
4  0.5730  1.5007 -0.6761  1.3673
5 -1.7412  0.7820 -1.2416 -2.0531
6 -1.2408 -0.8696 -0.1533  0.0004
7 -0.7439  0.4110 -0.9296 -0.2824
8 -1.1949  1.3207  0.2382 -1.4826
9  2.2938  1.8562  0.7733 -1.4465
"""
~~~





**在使用时间序列数据的特殊情况下,DataFrame索引还包括日期,广播按`列`进行广播**

df - df['A'] **这种方法不可以用**

**df.sub(df['A'],axis=0)**

### 使用标量值得操作

df*5+2

1/df

df**4

### 布尔运算符

df&df2

df|df2

df^df2

-df

### 行列转换

**df.T**

### DataFrame于Numpy函数的互操作性

 **Elementwise NumPy ufuncs（log，exp，sqrt，...）和各种其他NumPy函数可以在DataFrame上使用，假设其中的数据是数字：**

* np.exp(df)
* np.array(df)

**DataFrame上的点方法实现矩阵乘法**

* df.T.dot(df)

**Series上的dot方法实现了dot产品**

~~~python
s1 = pd.Series(np.arange(5,10))
s1.dot(s1)

    
~~~



**DataFrame并不是ndarray的替代品，因为它的索引语义与矩阵的位置完全不同**



### 控制台显示

它的索引语义与矩阵的位置完全不同

**将截断非常大的DataFrame已在控制台中显示他们;获取摘要  数组.info()**

**to_string将以表格形式返回DataFrame的字符串表示形式**

数组.to_string()

**默认情况下;宽数据框将跨多行打印**

* 可以通过设置display.width 选项来更改单行打印的数量

  ~~~python
  pd.set_option('display.width', 40) # default is 80
  pd.DataFrame(np.random.randn(3, 12))
  ~~~

* 还可以通过设置调整个列的最大宽度 **display.max_colwidth**

  ~~~python 
  pd.set_option('display.max_colwidth',30)
  ~~~

* 您也可以通过该`expand_frame_repr`选项禁用此功能。这将在一个块中打印表

### DataFrame列属性访问和ipython完成

**如果DataFrame列标签是有效的Python变量名称，则可以像属性一样访问该列：**

~~~python
df = pd.DataFrame({'foo1' : np.random.randn(5),'foo2':np.random.randn(5)})
df.fool
~~~



### 面板

**Panel是一种使用较少但任然很重要的三维数据容器**

* items:axis 0,每个项目对应一个包含在其中的DataFrame
* major_axis    轴1,他是每个DataFrame的索引(行)
* minor_axis   轴2    它是每个DataFrame的列

**面板构建**

1. **从3Dndarray可选轴标签**

   ~~~python
   In [121]: wp = pd.Panel(np.random.randn(2, 5, 4), items=['Item1', 'Item2'],
      .....:               major_axis=pd.date_range('1/1/2000', periods=5),
      .....:               minor_axis=['A', 'B', 'C', 'D'])
      .....: 
   
   In [122]: wp
   Out[122]: 
   <class 'pandas.core.panel.Panel'>
   Dimensions: 2 (items) x 5 (major_axis) x 4 (minor_axis)
   Items axis: Item1 to Item2
   Major_axis axis: 2000-01-01 00:00:00 to 2000-01-05 00:00:00
   Minor_axis axis: A to D
   ~~~

2. 从数据帧的 对象字典

   ~~~PYTHON 
   In [123]: data = {'Item1' : pd.DataFrame(np.random.randn(4, 3)),
      .....:         'Item2' : pd.DataFrame(np.random.randn(4, 2))}
      .....: 
   
   In [124]: pd.Panel(data)
   Out[124]: 
   <class 'pandas.core.panel.Panel'>
   Dimensions: 2 (items) x 4 (major_axis) x 3 (minor_axis)
   Items axis: Item1 to Item2
   Major_axis axis: 0 to 3
   Minor_axis axis: 0 to 2
   ~~~

   | 参数 | 默认    | 描述                                  |
   | ---- | ------- | ------------------------------------- |
   | 相交 | `False` | 丢弃索引不对齐的元素                  |
   | 东方 | `items` | 用于`minor`将DataFrames的列用作面板项 |

3. Panel.from_dict

   ~~~python
   In [125]: pd.Panel.from_dict(data, orient='minor')
   Out[125]: 
   <class 'pandas.core.panel.Panel'>
   Dimensions: 3 (items) x 4 (major_axis) x 2 (minor_axis)
   Items axis: 0 to 2
   Major_axis axis: 0 to 3
   Minor_axis axis: Item1 to Item2
   ~~~



**把DataFrame变成panel**

df.to_panel()

### 转置

**panel可以使用其transponse方法重新排列**

~~~python
In [138]: wp.transpose(2, 0, 1)
Out[138]: 
<class 'pandas.core.panel.Panel'>
Dimensions: 4 (items) x 3 (major_axis) x 5 (minor_axis)
Items axis: A to D
Major_axis axis: Item1 to Item3
Minor_axis axis: 2000-01-01 00:00:00 to 2000-01-05 00:00:00
                    
~~~

### 索引/选择

| 手术                       | 句法               | 结果   |
| -------------------------- | ------------------ | ------ |
| 选择物品                   | `wp[item]`         | 数据帧 |
| 在major_axis标签处获取切片 | `wp.major_xs(val)` | 数据帧 |
| 获取minor_axis标签的切片   | `wp.minor_xs(val)` | 数据帧 |

### 挤压

**另一种改变对象维度的方法是squeeze 1-len对象,类似wq['Iteml']**

~~~python 
In [143]: wp.reindex(items=['Item1']).squeeze()
Out[143]: 
                   A         B         C         D
2000-01-01  1.588931  0.476720  0.473424 -0.242861
2000-01-02 -0.014805 -0.284319  0.650776 -1.461665
2000-01-03 -1.137707 -0.891060 -0.693921  1.613616
2000-01-04  0.464000  0.227371 -0.496922  0.306389
2000-01-05 -2.290613 -1.134623 -1.561819 -0.260838

In [144]: wp.reindex(items=['Item1'], minor=['B']).squeeze()
Out[144]: 
2000-01-01    0.476720
2000-01-02   -0.284319
2000-01-03   -0.891060
2000-01-04    0.227371
2000-01-05   -1.134623
Freq: D, Name: B, dtype: float64
~~~



### 转换数据帧

* panel.to_frame()   三维转二维
*  p.to_xarray()          三维转一维

### 弃用面板

~~~python
p = tm.makePanel()
p
~~~





