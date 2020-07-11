# python中的字典相当于java 的map
# 外星人，颜色和点数
alien={'color':'green',"points":5}

print(alien['color'])
print(alien['points'])
print(alien)
# add
alien['color']='yellow'
alien["points"]=10

print(alien)
# 添加属性坐标x,y
alien['x_pos']=0
alien['y_pos']=23
print(alien)

# 创建空字典
alien_0={}
# 添加数据
alien_0['demo']='green'
alien_0['points']=1
print(alien_0)

# 修改数据
alien_0['demo'] = 'black'
print("now demo "+alien_0['demo'])

# 删除
del  alien_0['points']
print(alien_0)

# 遍历
user_o={
    'name':'lktbz',
    'age':'18',
    'last':'feim'
}
for k,v in user_o.items():
    print(k+","+v)

# 遍历所有的key

for k in user_o.keys():
    print(k.title())

favorite_languages={
    'jen':'python',
    'sca':'c',
    'jms':'java',
    'phil':'ruby',
    'kaNn':'java'
}

friends=['jen','phil']

for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print("hi "+name.title()+",i see your favority language is"+favorite_languages[name].title()+"!")



# 顺序遍历
for name in sorted(favorite_languages.keys()):
    print(name.title())



# 遍历值
for lan in favorite_languages.values():
    print("字典的值为"+lan.title())


# 将字典中的数据提取到集合set中
for lan in set(favorite_languages.values()):
    print(lan.title())




