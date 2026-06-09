##作业：自定义一个函数，传入一个参数（整数），判断这个参数是不是质数
def prime_number(x):
    if x<=1:
        print(f'{x}不是质数')
    else:    
        for i in range(2,x):
            if x%i==0:
                print(f'{x}不是质数')
                break
        else:
            print(f'{x}是质数')


k=int(input('请输入你要判断的数字：'))
prime_number(k)
