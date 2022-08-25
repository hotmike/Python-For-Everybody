###Use json

import urllib.request, urllib.parse, urllib.error
import json

url = 'http://py4e-data.dr-chuck.net/comments_1590605.json'

uh = urllib.request.urlopen(url)
data = json.load(uh)
#print(data)
clist = data['comments']
sum = 0
for item in clist:
    #print("Count: ",item["count"])
    print(item['name'])
    sum = sum + item['count']

print(sum)
