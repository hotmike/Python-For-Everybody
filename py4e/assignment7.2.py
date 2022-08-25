#Count these lines and extract the floating point values from each
#of the lines and compute the average of those values and produce an
#output as shown below


fname = input("Enter file name: ")
fh = open(fname)
tot = 0
count = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
            continue
    count = count + 1
    #print(count)
    #print(line)
    num  = line.find('0')
    n = (line[num:])
    #print(n)
    tot = tot + float(n)
print(tot)
print("Average spam confidence:" ,tot/count)


#Average spam confidence: 0.7507185185185187
