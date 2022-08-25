fname = input("Enter file name: ")
fh = open(fname)
lst = list()

for line in fh:
    for i in line.rstrip().split():
        lst.append(i) #要把列表一個個讀入
lst = list(set(lst)) #用set(）去重複
lst.sort() #sort()沒有返回值，所以要單獨寫一行，不能寫在print裡面
print(lst)
