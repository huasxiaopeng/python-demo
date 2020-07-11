# python中的字典相当于java 的map
# 嵌套

alien_0={'color':'green',"points":5}
alien_1={'color':'yellow',"points":10}
alien_2={'color':'red',"points":15}

# 定义三个字典

aliens=[alien_0,alien_1,alien_2]
# for alin in aliens:
#     print(alin)


# 自动生成创建外星人 创建30个
aliens=[]
for als in range(30):
    new_alien={'color':'green',"points":5,'speed':'slow'}
    aliens.append(new_alien)

# 显示前5个
for five in aliens[:5]:
    print(five)
print("...")


# 显示创建了多少个外星人
print("创建了"+str(len(aliens))+"个外星人")




#字典中存储列表
pizza={
    'curst':'thick',
    'topping':['red','green','yellow']
}

# 遍历其中的列表
for iss in pizza['topping']:
    print(iss)


favorite_languages={
    'jen':['python','java'],
    'sca':'c',
    'jms':['java','go'],
    'phil':['ruby','hadoop'],
    'kaNn':['java','c','js']
}

for name,land in favorite_languages.items():
    print(name.title()+"热爱的编程语言是：")
    for lan in land:
        print(lan.title())



# 字典存储字典
users={
    'lktbz':{
        'first':'al',
        'last':'et',
        'location':'prices'
    },
    'yan':{
            'first':'mk',
            'last':'qq',
            'location':'parids'
        }
}


for kname,kinfo in users.items():
    print("\nUserName:"+kname)
    full_name=kinfo['first']+""+kinfo['last']
    loacation=kinfo['location']

    print(full_name.title())
    print("---------------")
    print(loacation.title())