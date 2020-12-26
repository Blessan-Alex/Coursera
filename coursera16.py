
import urllib
import urllib.request
import xml.etree.ElementTree as ET
accumulator = 0
url = input("Enter location: ")
if len(url) < 1:
    url = "http://python-data.dr-chuck.net/comments_1055925..xml"
print ("Retrieving " , url)
xml = urllib.request.urlopen(url).read()
print ("Retrieved: " ,str(len(xml)) , " characters")
tree = ET.fromstring(xml)
counts =  tree.findall('.//count')
print ("Count: " + str(len(counts)))
for count in counts:
    accumulator+= int(count.text)
print ("Sum:" + str(accumulator))