#xuyuan
import copy
names=["Bob","Mike",["Danny","Alice"],"Mary"]
names3=names.copy()
names[1]="s"
names[2][0]="DANNY"
print(names)
print(names3)


names2=names
names[1]="Lily"
print(names)
print(names2)
'''
names.insert(1,"Xay")#插入，就在其将要插入的位置的前面的的元素的位置
print(names)
names[3]="lilei" #改，将第四个变为了lilei
print(names)
names.remove("Bob")#删，三种删除方式
print(names)
del names[0]#删，写的是下标的位置
print(names)
names.pop()#删，三种删除方式，不写时候默认删除最后一个，写下标的话，就是删除指定位置
print(names)
print(names.index("Alice"))#找其位置
'''