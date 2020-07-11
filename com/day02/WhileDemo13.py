# while 循环
# c_num=1
# while c_num<=5:
#     print(c_num)
#     c_num+=1


# 原则用户什么时候推出
promet="我将重复做一些事情"
promet+="输入 exit 循环将停止"
# message=''
# while message !='exit':
#     message=input(promet)
#     print(message)


# 使用条件推出循环
# active =True
# while active:
#     message=input(promet)
#
#     if message =='exit':
#         active=False
#     else:
#         print(message)

# break 推出循环

# while True:
#     city=input(promet)
#
#     if city=='exit':
#         break
#     else:
#         print("lalal")


# continue 使用
# 1-10 循环，只打印偶数
cu_num=0
while cu_num <10:
    cu_num += 1
    if cu_num%2==0:
        continue

    print(cu_num)