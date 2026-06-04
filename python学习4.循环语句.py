###条件判断作业一：完善学员查看学习时长的功能(#加一个密码，密码正确才允许查看 pwd=qwe123)
###完善作业一，添加循环，直至输入的密码正确才停止循环
##count=1;
##while count:
##    pwd=input("请输入密码：")
##    if pwd=='qwe123':
##        count=count-1
##        student=input("请输入你的名字：")
##        class_diversity=input("请输入你的课程：")
##        learn_time=input("请输入你的学习时间：")
##        print(f"尊敬的{student}同学，你当前所学习的{class_diversity}课程，目前已学习{float(learn_time):.2f}时间")
##    else:
##        print("密码错误，请重新输入")


####案例1：输出1-10之间的偶数
##a=1
##while a<=10:
##    if a%2==0:
##        print(a,end=' ')
##    a=a+1


####案例2：计算1-10所有数之和
##count=0
##i=0
##while i<=10:
##    count+=i
##    i+=1
##print(f"1-10所有数之和为{count}")


####案例3：for循环实现1-20所有数之和
##count=0
##for i in range(1,21,1):
##    count+=i
##    print(f"1-{i}所有数相加之和为{count}")
##print()
##print(f"1-20所有数相加之和为{count}")


###条件判断作业一：完善学员查看学习时长的功能(#加一个密码，密码正确才允许查看 pwd=qwe123)
###完善作业一，添加循环，直至输入的密码正确用break才停止循环
##
##while 1:
##    pwd=input("请输入密码：")
##    if pwd=='qwe123':
##        count=count-1
##        student=input("请输入你的名字：")
##        class_diversity=input("请输入你的课程：")
##        learn_time=input("请输入你的学习时间：")
##        print(f"尊敬的{student}同学，你当前所学习的{class_diversity}课程，目前已学习{float(learn_time):.2f}时间")
##        break
##    else:
##        print("密码错误，请重新输入")



####案例4：99乘法表
##for i in range(1,10):
##    for j in range(1,i+1):
##        k=i*j
##        print(f'{j}*{i}={k}',end=' ')
##    print()
        
##作业1：猜数字
'''
完成一个猜数字的小游戏，范围1-100之间，5次猜的机会
猜对打印游戏胜利，游戏结束
猜错提示猜大了还是猜小了
如果机会使用完毕，提示用户机会已经使用完毕，游戏失败
'''
import random

a=random.randint(1,100)
for i in range(1,6):
    goal=int(input("请猜一个1-100范围内的数字："))
    if goal==a:
        print("猜对啦")
        break
    elif goal>a:
        print("猜大了")
    else:
        print("猜小了")
else:
    print(f"5次机会全部使用完了，游戏失败，正确为{a}")


