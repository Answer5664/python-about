##如果有多个数据，如何快速存储这些数据？
li=[24,8,6,2,25,56,24,78,1,6,3,9,5,1005,52,1314]

##如何查找数据24
print(li[0])

##如果对列表进行了排序，又如何查看排序后的24
li.sort()
##print(li)
##很明显，如果在数据够多不输出列表具体情况的条件下，是不太可能知晓24的下标位置的，由此字典派上了用场

##字典的键只能是不可变的，不可变的现在只学了两种，一个是字符串（一般使用偏多），另外一个是元组
##dic={'姓名':'王新宇','年龄':24,'性别':'男','老大种类':'布偶','老大年龄':'8个月','老大性别':'公','老二种类':'金加白','老二年龄':'6个月','老二性别':'母','老三种类':'银渐层','老三年龄':'两个月','老三性别':'母',('最贪吃的','最喜欢叫的'):'聪聪'}
##print(dic)


##作业一：有一段英文文本，帮忙统计文本中每一个字符出现的次数和频率（保留2位小数）
st="It is a highly competitive world. One can feel the existence of competition everywhere, from the classroom to the job-hunting market. Looking for a fair opportunity to prove one's ability has become a matter of survival.If one wants to survive and to be successful in such a challenging society,one must learn to face the competition bravely"
dic={}
timer=0
frequency=0
for i in st:
    timer=st.count(i)
    frequency=timer/len(st)
    dic.update({i:f'次数为{timer},频率为{frequency:.2f}'})
print(dic)
    

