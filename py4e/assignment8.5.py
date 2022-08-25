fname = input("Enter file name:")
if len(fname) < 1:
    fname = "mbox-short.txt"
fh = open(fname)

count = 0
for line in fh:
    line = line.rstrip()
    if not line.startswith("From:"): #要注意冒號或是空白
        continue
    count = count + 1
    work = line.split()
    #print(work)
    e = work[1]

    print(e)


print("There were", count, "lines in the file with From as the first word")
