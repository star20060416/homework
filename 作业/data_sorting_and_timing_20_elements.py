#20个数据排序
import time
import random

data_20 = [random.randint(1, 100) for _ in range(20)]
start_time = time.time()
data_20.sort(reverse=True)
end_time = time.time()
print(f"20个数据排序结果: {data_20}, 耗时: {end_time - start_time} 秒")

#20000个数据排序
import time
import random

data_20m = [random.randint(1, 100) for _ in range(20000000)]
start_time = time.time()
data_20m.sort(reverse=True)
end_time = time.time()
print(f"2000万个数据排序结果: {data_20m}, 耗时: {end_time - start_time} 秒")