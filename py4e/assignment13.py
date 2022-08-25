### xml assignment


import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET



url = 'http://py4e-data.dr-chuck.net/comments_1590604.xml'
uh = urllib.request.urlopen(url)

data = uh.read()
tree = ET.fromstring(data)
lst = tree.findall('comments/comment')
#print(len(lst))
sum = 0
for x in lst:
    x = int(x.find('count').text)
    sum = sum + x
print(sum)
