##一个列表，里面都是整数，要求删除一个元素，
##使得剩余元素的乘积最大(需要考虑是否有负数存在)

##
##li=[1,9,5,6,-5,-3,0,-2]
##max=0
##sign=-1
####print(len(li))
##for i in li:
##    temp=1
##    print(f"这次删除的是{i}")
##    sign=li.index(i)
##    li.remove(i)
##    print(li)
##    for k in li:
##        temp*=k
##    else:
##        if temp>max:
##            max=temp
##        li.insert(sign,i)
##print(f"删除第{i+1}个元素后，剩余元素乘积最大，最大为{max}")




##一个列表，里面都是整数，要求删除一个元素，
##使得剩余元素的乘积最大(需要考虑是否有负数存在)
##优化法一
li=[1,9,5,6,-5,-3,0,-2,-6,7,10]
max=-9999999999999
sign=0
for i in range(len(li)):
    temp=1
    print(f"这次删除第{i}个元素")
    li_1=li[0:i]
    li_2=li[i+1:len(li)]
    li_1.extend(li_2)
##    print(li_1)
    for k in range((len(li_1))):
##        print(li_1[k])
        temp*=li_1[k]
        print(temp)
    else:
        if temp>max:
            max=temp
            sign=i
print(f"删除第{sign}个元素后，剩余元素乘积最大，最大为{max}")

        

