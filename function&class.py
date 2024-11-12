# 创建函数

def repetor(s, n) :
    result = s * n
    return result


res = repetor('go', 3)

print(res)

# python的函数允许返回多个值

def calculator(m, n) :
    return m + n, m - n,  m * n, m / n

print(calculator(2, 4))

# python中的可变参数与不可变参数，与C++中的类似，都是传递一份本身值的副本进去，但是对于列表一类的来说，传递本身值的副本也是传递相同的地址

# 整型、浮点、字符串、元组属于不可变参数
def priceChanger(p):
    p = p + 10 
    print('改变后的价格：{:.2f}'.format(p))
price = 10.8
priceChanger(price)
# 改变后的价格：20.80
print(price)
# 10.8

# 列表，字典，集合是可变类型参数
def contentChanger(name_list):
    name_list[0], name_list[1] = name_list[1], name_list[0]
    print('函数中的 name_list:', name_list)
language_name = ['C', 'Python']
contentChanger(language_name)
# 函数中的 name_list: ['Python', 'C']
print('调用函数后的 language_name:', language_name)
# 调用函数后的 language_name: ['Python', 'C']

# 关键字参数
# python允许调用函数时通过关键字参数的形式指定形参与实参的对应关系

def minus(a, b) :
    return a - b

print(minus(b = 3, a = 5))

# 指定默认参数值
# 在函数定义时，可以为参数指定值，这样会使得该参数在调用时变为可选

def mymod(x, y = 2) :
    return x % y

print(mymod(13))

# * 可以将一组数量不定的参数组合成参数的元组，在函数内部可以通过访问元组中的每个元素来使用参数

def m_value(*values) :
    max_v = max(values)
    min_v = min(values)
    print(max_v, min_v)

m_value(8, 4, 3, 7, 9, 1)

print("-----------------------------------------------------------")

# class 类
# 类的总体内容与C++和Java差不多

class animal() :

    owner = 'None' # 类属性
    
    # 实例属性，必须定义在__init__方法中用self.的变量
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 实例方法
    def show(self):
        print(f'My name is {self.name}, and my age is {self.age}')

    # 静态方法
    # 静态方法不能使用实例属性，不能调用实例方法
    # 但是可以用对象.静态方法来调用，也可以通过类名.静态方法调用
    @staticmethod
    def what():
        print('This is a static method')

    # 类方法
    @classmethod
    def cm(cls):
        print('This is a class method')

dog = animal('Mike', '5')
dog.show()
dog.what()
dog.cm()
animal.cm()

print("-----------------------------------------------")

# 权限控制
class student :
    
    # 前后都有双下划线的是特殊方法
    def __init__(self, name, age, gender):
        self._name = name # protected，允许类和子类访问，不允许外部代码访问（但实际上好像可以
        self.__age = age # private，只允许定义该属性或方法的类本身进行访问
        self.gender = gender # public

        # 变量和方法都遵循上述规定
