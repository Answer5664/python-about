###课堂小练1：请用户告知当前的天气情况，然后根据天气决定今天的行程
##weather=input("请用户告知当前的天气情况：")
##if weather=="晴天":
##    print("今天适宜出门散步")
##elif weather=="雨天":
##    print("今天适宜在家看剧")
##else:
##    print("今天既不是晴天也不是阴天，用户自己决定干嘛吧")
##



###课堂小练2：判断学员的考试成绩，进行评级
##score=int(input("请输入考试成绩："))
##if score>90 and score<=100:
##    print("A")
##elif score>80 and score<=90:
##    print("B")
##elif score>70 and score<=80:
##    print("C")
##elif score>60 and score<=70:
##    print("D")
##else:
##    print("不及格")


###作业一：完善学员查看学习时长的功能(#加一个密码，密码正确才允许查看 pwd=qwe123)
##pwd=input("请输入密码：")
##if pwd=='qwe123':
##    student=input("请输入你的名字：")
##    class_diversity=input("请输入你的课程：")
##    learn_time=input("请输入你的学习时间：")
##    print(f"尊敬的{student}同学，你当前所学习的{class_diversity}课程，目前已学习{float(learn_time):.2f}时间")
##else:
##    print("密码错误，你没有权限查询")

#作业二：写一个体重健康查询功能
'''
用户BMI值处于什么范围 给用户对应的提示
计算公式为：BMI=体重/身高的平方
偏瘦（BMI < 18.5）
正常（18.5 ≤ BMI < 24）
超重（24 ≤ BMI < 28）
肥胖（BMI ≥ 28）
'''
height=float(input("请输出身高(m)："))
weight=float(input("请输出体重(kg)："))
BMI=weight/height**2
if BMI<18.5:
    print(f"BMI为{BMI:.2f},偏瘦")
elif 18.5<=BMI<24:
    print(f"BMI为{BMI:.2f},正常")
elif 24<=BMI<28:
    print(f"BMI为{BMI:.2f},超重")
else:
    print(f"BMI为{BMI:.2f},肥胖")
