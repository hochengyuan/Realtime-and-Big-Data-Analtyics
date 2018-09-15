
# coding: utf-8

# In[1]:

#!/usr/bin/env python

import sys

new_content = []


for content in sys.stdin:
    # type(content) == list
    # split [string,string,...] to [['string','string'...]...]
    content = content.split()
    for index_linkList , element in enumerate(content):
        try:
            content[index_linkList] = (float(element))
        except ValueError:
            pass
    new_content.append(content)

OutputLinkList = []
for linkList in new_content:
    if (type(linkList[-1]) == str):
        OutputLinkList.append(linkList)
        new_content.remove(linkList)

for elementList in OutputLinkList:
    elementList.append(0)



for elementList in OutputLinkList:
    for mapValueList in new_content:
        if mapValueList[0] == elementList[0]:
           elementList[-1] += mapValueList[-1]

for elementList in OutputLinkList:
    elementList[-1] = round(elementList[-1] , 6)

      
reduceResult = ""
for resultLinkList in OutputLinkList:
    resultLinkList[-1] = str(resultLinkList[-1])
    for result in resultLinkList:
        reduceResult += result + " "
    reduceResult += '\n' 
reduceResult = reduceResult.rstrip('\n')
    
print(reduceResult)

