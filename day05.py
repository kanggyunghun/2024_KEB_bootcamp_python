def my_range(first=0, last=10, step=1):
    number = first
    while number < last:
        yield number
        number += step

my_list = my_range(1,5)

for i in my_list:
    print(i)

for j in my_list:
    print(j)