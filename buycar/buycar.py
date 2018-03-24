#xuyuan
list_shop=[
    ("book",100),
    ("paper",200),
    ("apple",50),
    ("pen",40),
]
shoping_list=[]
salary=input("Input your salary：")
if salary.isdigit():
    salary=int(salary)
    while True:
        for index,item in enumerate(list_shop): #对列表的带序号打印，
            # #对于一个可迭代的（iterable）/可遍历的对象（如列表、字符串），enumerate将其组成一个索引序列，利用它可以同时获得索引和值
            print(index,item)
        user_choice=input("选择买的东西>>>：")
        if user_choice.isdigit():
            user_choice=int(user_choice)
            if user_choice< len(list_shop) and user_choice>=0:
                p_item=list_shop[user_choice] #通过下标将商品取出来
                if p_item[1]<=salary: #买的起，存到购物车
                    shoping_list.append(p_item)
                    salary-=p_item[1]
                    print("Added %s into shopping cart,your current balance is \033[31;1m%s\033[0m" %(p_item,salary))#显示的是红色的
                else:
                    print("\033[41;1m your current balance is[%s]\033[0m" %salary)#41是背景
            else:
                print("product code [%s] is not exist,you count buy"%user_choice)
        elif user_choice=='q':
            print('-----------shonping list-----------')
            for p in shoping_list:
                print(p)
            print("your current balance is %s"%salary)
            exit() #结束循环，退出
        else:
            print("invalid option")
