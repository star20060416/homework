count = 0
for year in range(1001, 3000):
    if year % 7 == 0 and year % 5 != 0:
        print(year, end="#")
        count += 1
        if count % 5 == 0:
            print()