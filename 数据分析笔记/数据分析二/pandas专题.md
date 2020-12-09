# pandas文件操作专题

* **读写各种文件方法介绍**

* **各种文件特征**

* **读写案例**

  **案例1:读写csv**

  **方法和参数:**

  **read/to_csv(文件名,sep='分隔符',header=None)**

  * **默认分隔符是逗号**

  * **指定分隔符 sep=''**

  * **跳过头: header = None**

  * **重新指定列名: names=['列名1','列名2',......]**

  * **字符集:encoding='utf-8'**

    ~~~python
    #返回TextFileReader对象(多少块)
    #加快读取速度:按块读取  chunksize=1000
    #返回的是 TextFileReader对象
    import datatime
    
    
    # 开始时间
    start = datatime.datatime.now()
    df1 = pd.read_csv('house.csv',encoding='gbk',chunksize=1000)
    a_list = pd.Series([])
    #循环遍历块，统计块中次数！
    for item in df1:
        a_list = a_list.add(item['地区'].value_counts(), fill_value=0)
    # 结束时间
    end = datatime.datatime.now()
    # 差 = 结束-开始
    cha = end-start
    cha
    ~~~


  **read/to_table(文件名,sep='')**

  * **read_table和read_csv一样功能,他的默认分隔符是\t,**读取按照某个字符分隔的格式化规整的数据,如果是逗号隔开的建议使用read_csv,

    ~~~python
    result= pd.read_table('exs.txt',sep='\s+')
    ~~~



    ### 读取json

    * json.loads(字符串) ==字典

    * DataFrame 直接操作字典

      ~~~python
      # 案例2 处理json
      obj = """
      {"name": "Wes",
       "places_lived": ["United States", "Spain", "Germany"],
       "pet": null,
       "siblings": [{"name": "Scott", "age": 30, "pets": ["Zeus", "Zuko"]},
                    {"name": "Katie", "age": 38,
                     "pets": ["Sixes", "Stache", "Cisco"]}]
      }
      """
      # 1 普通字符串转换为python对象
      import json
      # str--->字典（json格式）
      result = json.loads(obj)
      # pandas 操作字典
      siblings = pd.DataFrame(result['siblings'], 
                              columns=['name', 'age'])
      siblings
      ~~~
