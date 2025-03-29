nums = list(map(int, input("请输入一系列逗号分隔的数字: ").split(',')))
result = []
for num in nums:
    if num not in result:
        result.append(num)
print(",".join(map(str, result)))