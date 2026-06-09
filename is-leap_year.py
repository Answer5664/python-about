# 案例 写一个函数判断当前年份是否是闰年
# 能被4整除 不能被100整除 能被400整除
def is_leap_year(x):
    if x%4==0 and x%100!=0 or x%400==0:
        print(f"{x}是闰年")
    else:
        print(f"{x}不是闰年")


is_leap_year(2026)
