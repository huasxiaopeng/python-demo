##Python supports two types of numbers -
# integers and floating point numbers.
# (It also supports complex numbers,
# which will not be explained in this tutorial)
myint=7
print(myint)
myint=int(10)

myfloat=7.0
print(myfloat)

myfloat=float(7)

print(myfloat)
#从上面可以发现，python 可以进行类型推导


#Strings are defined either with a single quote or a double quotes.
mystring='hello'
print(mystring)
mystring="world"
print(mystring)


mystring = "Don't worry about apostrophes"
print(mystring)
#Simple operators can be executed on numbers and strings:
one=1
two =2
three=one+two
print(three)


hello="hello"

world="world"
helloworld=hello+""+world
print(helloworld)


name="Ada Angent of Shield"
print("变大写"+name.upper())

print("测试title"+name.title())
# \t \n的使用
print("\tlala")
print("\nl\nla\nlall")
# 空格去除

python="python  "
print(python.rstrip())

# 去除左右空格

python="  hello  "
print(python.rstrip())
print(python.lstrip())


#Assignments
# can be done on more than one variable "simultaneously" on the same line like this
a,b=3,4
print(a,b)
#Mixing operators between numbers and strings is not supported:
one =1
two =2
hello="hello"
# print(one+hello+two) 不支持的操作

