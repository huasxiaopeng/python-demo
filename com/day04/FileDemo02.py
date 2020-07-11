# 文件的写入
# 写空数据
fileName = 'empty.txt'
with open(fileName, 'w') as fle_obj:
    fle_obj.write("l love python")

# 写入中文
with open(fileName, 'w', True, "utf-8") as fils:
    fils.write("伟大的全世界人民，你们在干嘛你额？")

print("写入完毕")

# 写入多行
with open(fileName, 'w') as fle_obj:
    fle_obj.write("l love python")
    fle_obj.write("l love java")

print("多行写入完毕")  # 发现输入的l love pythonl love java，不符合预期

with open(fileName, 'w') as fle_obj:
    fle_obj.write("l love python\n")
    fle_obj.write("l love java")

print("多行带换行功能写入完毕")

# 上面的例子全部是覆盖原来的内容，着显然不符合我们的预期
fileName = 'list.txt'
with open(fileName, 'a')as file_b:
    file_b.write("lalalalla\n")
    file_b.write("lalalalla\n")

print("追加内容全部写完")
