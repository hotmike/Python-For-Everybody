# Learn how to manage file

fname = input("Enter file name: ")
fh = open(fname)
for x in fh:
    x = x.rstrip() #取消右邊空白
    print(x.upper()) #把每一行變大寫列出來
