def test():
    #1.定义变量输入门数
    #2.循环，输入成绩，大于0，求平均值，否则自定义异常
    n=int(input('请问你要输入多少门成绩: '))
    s=0.0

    for i in range(1,n+1):
        dd=float(input('请输入成绩: '))
        if dd>0:
            s=s+dd 
        else:
            ex=Exception('成绩不为负数')
            raise ex
            #break#只要有一门为负数就终止
    avg=s/n
    print('平均分:%.2f'%avg)
try:
    test()
except ex:
    print('异常种类',ex)
else:
    print('')
    
