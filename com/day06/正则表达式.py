# 使用正则表达式来进行,匹配数据
# 将'你好，hello,世界' 匹配出其中的中文
import re

text = "你好,hello,世界"
# 使用正则表达式正常pattern
pattern = re.compile('[\u4e00-\u9fa5]')
# 查找匹配
result = pattern.findall(text)
print(result)
