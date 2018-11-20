
password='123456'

i=3

while i<4:
    password1=input('请输入六位密码：')
    l=len(password1)
    if l==6:
        i-=1
        if password1==password:
            print("密码正确，登录成功")
            break
        else:
            if i!=0:
                print("密码错误，你还有",i,"次机会")
            else:
                print("密码输入次数用尽")
                break
    else:
        print("输入密码不足六位")
        print("请再次输入")
        
'''
#一共有3次机会
count=3
#规定6位数密码是123456
pwd=123456

while count:
    count-=1
    key=int(input('请输入密码：'))
    if key ==pwd:
        print("密码正确")
        break

    else:
        if count!=0；
            print("密码输入错误，你还有",count,"次机会")
        else:
            print("密码输入错误")
'''
