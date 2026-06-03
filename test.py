##import keyword
####import decimal
####
####print("woshinidie");
####a=0;
####b=0.5;
####c=0.50;
####print(type(a));
####print(type(b));
####print(type(c));
####
####
####print(10/4);
####print(10//4);
####print(10%4);
####print(2.6-1.2);#浮点数计算不精确
####print(round(2.6-1.2,3));#精确小数方法1
####print(decimal.Decimal(2.6)-decimal.Decimal(1.2));
####
####
####print("大家好，我叫%s，今年%d岁，喜欢%s,%s和%s"%('王新宇',18,'唱跳','rap','篮球'))
####print("大家好，我叫{:s}，今年{:d}岁，喜欢{:s},{:s}和{:s}".format('王新宇',18,'唱跳','rap','篮球'))
####print(f"大家好，我叫{'王新宇'}，今年{18:d}岁，喜欢{'唱跳'},{'rap'}和{'篮球'}")
##
##
##
##print(keyword.kwlist)           #查看关键字
##print(dir(__builtins__))        #查看内置函数

##小练习
Pork=15
Broccoli=3
Chili=5
##买三斤猪肉,一斤西蓝花，两斤辣椒,用代码计算需要多少钱
print(Pork*3+Broccoli*1+Chili*2)
##第二天肉涨价到18，购买相同的量，用代码计算需要多少钱
Pork=18
second_day=Pork*3+Broccoli*1+Chili*2
print(f'第二天买菜需要花费{second_day:d}')


print(Chili,second_day,sep='$')
print(Pork,Chili,Broccoli,sep=' ',end='end')
print()
print(Pork,Chili,Broccoli,end='end',sep=' ')
print()
cherry=float(input('请输入樱桃价格(仅允许输入数字）：'))
