num = int(input("请输入一个数字: "))
factorial = 1
for i in range(1, num + 1):
    factorial *= i
print(factorial)