# 数据分析web展示步骤

* **创建Dj项目 文件名为house_info,2个app名字为 lianjia和anju**

  ![](C:\Users\Administrator\Desktop\1804数据分析第三个月\img\001.png)







* **配置house_info的py文件**
  * **urls路由配置**



  ![](C:\Users\Administrator\Desktop\1804数据分析第三个月\img\002.png)

  * **setting.py 配置**

  ![](C:\Users\Administrator\Desktop\1804数据分析第三个月\img\003.png)

  ![](C:\Users\Administrator\Desktop\1804数据分析第三个月\img\004.png)

* **lianjia里面的views代码编写**

![](C:\Users\Administrator\Desktop\1804数据分析第三个月\img\005.png)





* **lianjia里面url路由配置**

  ![](C:\Users\Administrator\Desktop\1804数据分析第三个月\img\006.png)

* **创建一个名为templates的文件包**



![](C:\Users\Administrator\Desktop\1804数据分析第三个月\img\007.png)

* 在templates文件包里面创建html网页用来展示数据分析的图,引入百度echars

  ~~~html
  {%load static%}     #引入静态文件
  <!DOCTYPE html>
  <html>
  <head>
      <meta charset="utf-8">
      <title>ECharts</title>
      <!-- 引入 echarts.js -->
      <script src="{%static 'js/echarts.min.js' %}"></script>
  </head>
  <body>
      <!-- 为ECharts准备一个具备大小（宽高）的Dom -->
      <div id="main" style="width: 600px;height:400px;"></div>
      <script type="text/javascript">
          // 基于准备好的dom，初始化echarts实例
          var myChart = echarts.init(document.getElementById('main'));
  
          // 指定图表的配置项和数据
          var option = {
              title: {
                  text: '北京各区房源信息'
              },
              tooltip: {},
              legend: {
                  data:['销量']
              },
              xAxis: {
                  data: [{%for x in xlist%}   #渲染数据
          "{{x}}",
          {%endfor%}]
              },
              yAxis: {},
              series: [{
                  name: '销量',
                  type: 'bar',
                  data:{{ylist}},
              }]
          };
  
          // 使用刚指定的配置项和数据显示图表。
          myChart.setOption(option);
      </script>
  </body>
  </html>
  ~~~

* 运行测试自己写的DJango项目



![](C:\Users\Administrator\Desktop\1804数据分析第三个月\img\008.png)





### 以上就是真个DJango项目的流程



