print('|---欢迎进入通讯录程序---|')
print('|---1.查询联系人资料---|')
print('|---2.插入新的联系人---|')
print('|---3.删除已有联系人---|')
print('|---4.查看所有通讯录---|')
print('|---5.退出通讯录---|')

dict = {}


while True:
    i = int(input('请输入需要操作的编号：'))
    if i == 1:
        name = input('请输入联系人姓名：')
        if name in dict:
            print('姓名\t手机号码')
            print(name,'\t',dict[name])
        else:
            print('抱歉，您查询的姓名不在通讯录内!')
            
    elif i == 2:
        name = input('请输入联系人姓名：')
        if name in dict:
            print('联系人已存在！')
            print(name,'\t',dict[name])
            if input('是否需要更改用户信息（YES/NO）：').upper() == 'YES':
                dict[name] = input('请输入联系人手机号码：')
        else:
            #dict[name] = input('请输入联系人手机号码：')，，字典添加元素方法
            #和下面两句功能一样
            tel = input('请输入联系人手机号码:')
            dict.update({name:tel})
            print('添加成功！')
    elif i == 3:
        name = input('请输入需要删除的联系人姓名：')
        if name in dict:
            del(dict[name])
            print('删除成功！')
        else:
            print('您需要删除的联系人不存在！',end =' ')
            name = input('请重新输入需要删除的联系人姓名:')
    elif i == 4:
        print('姓名\t手机号码')
        for key,value in dict.items():
            print(key,value)
    elif i == 5:
        break
    else:
        print('请输入1—5之间的编号！')
        i = int(input('请输入需要操作的编号：'))
