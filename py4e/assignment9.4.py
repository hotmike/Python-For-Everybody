#計算哪個email出現過最多次



name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)


maxmail = dict()  #建立字典

for line in handle:
    if not line.startswith('From '):
        continue
    words = line.split()
    maxmail[words[1]] = maxmail.get(words[1],0)+1 #加總出每個email出現的次數


#找到最多次數email
bigcount = None
bigmail = None
for mail, count in maxmail.items(): #用items可以同時算出key跟value
    if bigcount is None or count > bigcount:
        bigmail = mail
        bigcount = count
print (bigmail,bigcount)
