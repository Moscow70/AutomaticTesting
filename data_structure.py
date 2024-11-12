# list 列表

a = [1, 2, "abc", [1, 2, 3]] # list可以同时容纳任意一种类型数据

b = list(range(1, 10)) #可以生成一连串连续的数字

c = list('abcd') #可以拆分字符串

print(b)

print(c)

b[0] #有索引，正向从0开始计数，负数即从后往前，从-1开始

b[1 : 4] #切片，即取它的子集。

b.append("test") #直接往尾部添加

d = a + b # 列表合并

print(d)

print(3 in d) # 成员判断

print("---------------------------------------")

# tuple 元组

t = (1, 2, 3) # 用()而非[]声明

# a[1] = 2  不可修改
# TypeError

t1 = t[1 : 2] #切片操作还是用[]

# 元组自带的方法只有count（计算某个元素的出现次数）和index（返回第一次出现某元素的索引）

t2 = (1,) # 创建单元素元组要加一个, 否则()会被识别为运算符

# 若元组里包含列表，则可以对列表中的元素进行修改，但是不可以删除这个列表

print("---------------------------------------")

# dict 字典

d1 = {
    'Tom': 85,
    'Jerry': 100
}

d2 = {
    'spike': 70
}

dict.fromkeys(['A', 'B']) # 创建值为空的数组

dict.fromkeys(['A', 'B'], 0) # 创建默认值为0的数组

d1['Tom'] # 直接访问

d1.get('Tom') # 使用get方法，这样在该key不存在时不会报错，而是默认返回空

d1.keys() # 获取所有的key

d1.values() # 获取所有的value

d1.items() # 获取所有的键值对，以元组列表的形式返回

d1.keys() & d2.keys() # 交集

d1.keys() - d2.keys() # 差集

d1.keys() | d2.keys() # 并集

d1['Jerry'] = 99 # 修改

d1.pop('Tom') # 删除key并返回value

d1.update(d2) # 合并两个字典，key相同的会被update进来的value替代

d1.setdefault('Tom', 21) # 添加新的键，如果没有默认值则为空，如果键已存在则不会发生变化

for k in d1.keys() :
    print(k, d1[k])

# 使用key遍历

print("---------------------------------------")

# set 集合，它是一个无序不重复的序列

s = {1, 'a', "aaa"}

s1 = set() # 空集合只能用set创建，因为s = { } 创建的是空字典

s.add(3.14) # 添加元素

s.update([-1, 0]) # 一次添加多个。注意，无论以集合形式还是列表形式添加，在set里最终都会变成普通的元素

print(s)

s.remove(0) # 删除元素

s.discard(-2) # 使用discard删除不存在的元素不会报错

# 和字典一样，集合也可以进行交集，并集，差集，对称差的计算。使用运算符或对应的方法都可以

s_new = s.intersection(s1)

# 除了union之外，其它三个方法都有一个update版本。这样就会直接在原集合上进行修改，而不会返回一个新集合

s.intersection_update(s1)


