name = input("Enter file:")
if len(name) <= 1:
    name = "mbox-short.txt"
handle = open(name)
counts = dict()
for line in handle:
    if not line.startswith("From "):
        continue
    words = line.split()
    time = words[5]
    hour = time.split(':')
    hour = hour[0]
    #print(hour)
    counts[hour] = counts.get(hour,0) + 1
#print(counts)


for k,v in sorted(counts.items()): #Sorting list of tuple
    print(k,v)
