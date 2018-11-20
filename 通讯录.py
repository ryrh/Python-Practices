

#通讯录

contact={'lily':'123456','mike':'234567','lucy':'345678','cane':'456789'}

print('---欢迎进入通讯录---')
print('---1：查找联系人---')
print('---2：退出通讯录---')
print('---3：修改通信录---')

while True:
    num=int(input('请输入指令数字：'))
    if num==1:
        name=input('请输入联系人姓名：')
        if name in contact:
            print(name,':',contact[name])
        else:
            print('该联系人不存在')
    if num==2:
        break
    if num==3:
        print(contact)
        print('1：删除联系人  2：增加联系人')
        num1=int(input('请输入指令数字：'))
        if num1==1:
              name=input('请输入联系人姓名：')
              if name in contact:
                  contact.pop(name)
                  print('删除完成')
              else:
                  print('该联系人不存在')
        if num1==2:
            name=input('请输入联系人姓名：')
            number=input('请输入联系人号码：')
            contact[name] = number
            print('号码录入完成',name,contact[name])
print('感谢使用通信录')
