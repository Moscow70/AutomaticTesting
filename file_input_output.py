from pathlib import Path


file_name = Path("D:/test.txt")

# open(file_name, mode)，mode是可选项，表示对文件的处理权限
f = open(file_name)

# 读取文件
f.read()

# 写入数据
data = "Hello world"
f.write(data)

# 关闭文件
f.close()

# with方法处理文件，在结束时会帮助关闭文件
with open(f, 'w', encoding='utf-8') as file:
    file.write(data)