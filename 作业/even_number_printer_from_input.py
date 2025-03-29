nums = input("请输入一系列逗号分隔的数字: ").split(',')
nums = [int(num) for num in nums]
for num in nums:
    if num % 2 == 0:
        print(num, end=" ")