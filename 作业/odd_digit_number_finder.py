def is_odd_digit(num):
    num_str = str(num)
    for digit in num_str:
        if int(digit) % 2 == 0:
            return False
    return True

result = []
for num in range(1000, 3001):
    if is_odd_digit(num):
        result.append(str(num))
print("@".join(result))