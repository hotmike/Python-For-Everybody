import re

file = open('regex_sum_1590600.txt')

sum = 0

for line in file:
    numbers = re.findall('[0-9]+', line) #把每一行的數字抓出來
    print(numbers)
    for number in numbers:
        sum = sum + int(number) #把每一行抓出來的數字加總
print(sum)
