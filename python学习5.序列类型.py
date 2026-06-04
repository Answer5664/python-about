####作业一：判断用户输入的是否是正确的手机号
####数字1开头，十一位，纯数字
##tel=input("请输入手机号码：")
##if tel[0]=='1' and len(tel) and tel.isdigit():
##    print("是手机号码")
##else:
##    print("不是手机号码")
##print(tel[0]=='1')
##print(len(tel))
##print(tel.isdigit())


####作业二：让用户输入五门考试成绩，去掉最高分和最低分，求平均值
##count=0
##score=input("请输入五门考试成绩，用逗号隔开：")
##li=score.split(',')
##li_1=[int(i) for i in li]
##li_1.sort()
##li_1.pop(0)
##li_1.pop(3)
##for i in li_1:
##    count+=i
##count/=3
##print(f"去掉最高分和最低分，求出的平均值为{count:.2f}")
##print(li_1)
