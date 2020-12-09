#                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    第八天matplotlib画图

### **复习**

- **画图**
  **Python绘图—Matplotlib教程（详细版）前半部分**
  https://blog.csdn.net/hustqb/article/details/76224208
  https://blog.csdn.net/u014465934/article/details/79793679
  https://www.cnblogs.com/zhizhan/p/5615947.html
  https://www.kesci.com/home/project/59e77a636d213335f38daec2
  https://blog.csdn.net/ScarlettYellow/article/details/80458797

**画图的基础库,常用的绘图方法:**

* plot()/line
* 散点图: scatter
* 柱状图:   bar/barh/堆叠(设置bottom)\直方图:hist
* 箱图:boxplot
* 小提琴图:　violinplot
* 饼状图：  pie()
* 子图： suoplot(一次划多个图)

### 文档相关方法

* **x和y轴大小限制**

  * x.lim(最小值，最大值)   y.lim(最小值，最大值)    范围是最小值到最大值之间

* **自定义x和y轴下标：**

  ~~~python
  """
  重点1. 手动设置x和y轴下标
  x轴   0,2月...10月  等差数列(np.linspace(小,大,份数))
  y轴   0--20000万
  """
  x = np.random.randint(200000,size=(10,2))
  plt.rcParams['font.sans-serif']=['SimHei']
  plt.plot(x)
  plt.xticks([0,2,4,6,8,10,12],['0','2月','4月','6月','8月','10月'])
  plt.yticks(np.linspace(0,200000,5),['0','4万','8万','12万','20万'])
  plt.show()
  ~~~


![00](C:\Users\Administrator\Desktop\1804数据分析第二个月\img\自定义.png)

* **子图subplot(行列N):**

  * 2行2列第一个:subplot(221)
  * 2行2列第二个:subplot(222)

* **文本说明:**

  * plt.text(x,y,'文本')

* **添加带箭头的注释:**

  ~~~python
  ax = plt.subplot(111)
  
  t = np.arange(0.0, 5.0, 0.01)
  s = np.cos(2*np.pi*t)
  line, = plt.plot(t, s, lw=2)
  """
  
  '注释',xy(箭头坐标),xytext(箭头尾部文本坐标),
  arrowprops=dict(facecolor='w', shrink=0.05)箭头设置(颜色,)
  """
  plt.annotate('最高值', xy=(1, 1), xytext=(3, 1.5),
               arrowprops=dict(facecolor='w', shrink=0.05),
               )                                               #添加注释
  
  plt.ylim(-2, 2)
  plt.show()
  ~~~




* **是否显示网格:  plt.grid(True)**
* **boxplot:箱图**
* 





             





                                        



