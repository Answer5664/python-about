#作业一：接受长方形的长和宽，计算长方形的面积和周长
length=input("请输入长方形的长：")
width=input("请输入长方形的宽：")
L=float(length)*2+float(width)*2   ##计算周长四条边相加，由于input接收的是字符类型，所以转成float(数值可以为小数)
S=float(length)*float(width)
print(f"此长和宽构成的长方形的周长为{L:.2f},面积为{S:.2f}")



###作业二：模拟一个学习时长查看功能，接收学员名，课程名，学习时长(输出格式为‘尊敬的XX同学，你当前所学习的xx课程，目前已学习XX时间’）
##student=input("请输入你的名字：")
##class_diversity=input("请输入你的课程：")
##learn_time=input("请输入你的学习时间：")
##print(f"尊敬的{student}同学，你当前所学习的{class_diversity}课程，目前已学习{float(learn_time):.2f}时间")
