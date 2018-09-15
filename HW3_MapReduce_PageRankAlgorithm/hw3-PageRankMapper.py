
# coding: utf-8

# In[1]:

#!/usr/bin/env python

import sys

for content in sys.stdin:
    content = content.strip()
    content = content.split('\n')
    # split [string,string,...] to [['string','string'...]...]
    content = [linkList.split() for linkList in content]
    # make float-like string to exact float
    for linkList in content:
        linkList[-1] = float(linkList[-1])

    # HW Requriement 1: Print out the original outlinks information
    OOI = ""
    for linkList in content:
        for element in linkList[:-1]:
            OOI = OOI + element + " "
    OOI += '\n'
    OOI = OOI.rstrip('\n') # delete the last blank line
    print(OOI)

    
    # initialize a Dictionary of PageRank
    DictPageRank = {}
    # add initial PR and respective Page to DictPageRank
    for PR_List in content:
        addDictPR = {PR_List[0] : PR_List[-1]}
        DictPageRank.update(addDictPR)
        # now we get initial value for every page
    list_content_noValue = [linkList[:-1] for linkList in content]
    # mapping DictPageLinkList
    # initialize the mappingList as a Dictionary
    MapList = []

    for linkList in list_content_noValue:
        for DictPgRk_Key , DictPgRk_Value in DictPageRank.items():
            # parse KeyPage from list content
            source_page = linkList[0]
            source_value = DictPageRank[source_page]
            source_divider = len(linkList[1:])
            source_divided_value = source_value / source_divider
        for element in linkList[1:]:
            outbound_Key = element
            toAppendList = [outbound_Key , source_page , source_divided_value]
            MapList.append(toAppendList)

    resultString = ""
    for listResult in MapList:
        listResult[-1] = str(listResult[-1])
        for element in listResult:
            resultString += element + " "
        resultString += '\n'
    

    resultString = resultString.rstrip('\n')

    print(resultString)

