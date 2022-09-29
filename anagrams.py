str = ['tea', 'eat', 'tree', 'teer', 'try', 'ate', 'bye']
newList = []
emptyDict ={}
    
for item in str:
    sortedItem = ''.join(sorted(item))
    if sortedItem not in emptyDict:
        emptyDict[sortedItem] = [item]
    else:
        emptyDict[sortedItem].append(item)
    # return empty_dict 
for key, val in emptyDict.items():
    if len(val)>=1:
        newList.append(val)
print(newList)