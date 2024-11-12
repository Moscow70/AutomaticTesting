a = input()
# python中使用input输入都是以字符串的形式储存的，若需要输入数字，则需要用int()、double()等函数转换
a = int(a)

print(a)

print("-------------------------------")

#一行中的多个输入需要通过split函数来将其分隔开来读入，否则会作为一个整体
b = input("2 numbers\n")
m, n = list(map(int, b.split(' ')))

print(b)
print(m, n)

print("-------------------------------")

#要输出指定位数的浮点数：
f = float(input("float\n"))

print(f"{f:.2f}")