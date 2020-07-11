# python 异常类
# python 异常需要自己去管理？ 异常类不去处理，程序会停止的哟
# print(5/0)ZeroDivisionError: division by zero 报上述错误

# 处理
# try:
#     print(5 / 0)
# except ZeroDivisionError:
#     print("不好意思亲，你不能进行此操作，0是不允许被整除的")

# 使用异常避免崩溃
# print("如果想退出程序，请输入：‘exit’")
# while True:
#
#     first_num = input("\nfirst_nums")
#     if first_num == 'exit':
#         break
#     second_num = input("\n second_num")
#     if second_num == 'exit':
#         break
#     result = int(first_num) / int(second_num)
#     print(result)
# 输入10 2 没问题，输入2，0 ZeroDivisionError: division by zero
# 对异常进行处理
# 上面的变种
print("如果想退出程序，请输入：‘exit’")
while True:

    first_num = input("\nfirst_nums")
    if first_num == 'exit':
        break
    second_num = input("\n second_num")
    try:
        result = int(first_num) / int(second_num)
    except ZeroDivisionError:
        print("不能输入0谢谢")
    else:
        print(result)