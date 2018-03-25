#xuyuan
age_of_boy=56
count=0
while count<3:
    guss_age = int(input("gusss age:"))
    if guss_age == age_of_boy :
        print("yes,you got it")
        break
    elif guss_age > age_of_boy:
        print("think smaller")
    else:
        print("think bigger")
    count = count + 1
else:
    print("you have use 3 times")
#此处能做到一直猜到这个数字，当然可以限制次数
#xuyuan