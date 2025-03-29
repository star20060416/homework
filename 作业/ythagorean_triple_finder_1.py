#方法省时
import time
start_time = time.time()
for a in range(1, 333):
    for b in range(a + 1, 500):
        c = 1000 - a - b
        if a ** 2 + b ** 2 == c ** 2:
            print(f"a={a}, b={b}, c={c}")
end_time = time.time()
print(f"运行耗时: {end_time - start_time} 秒")