# minimun occurence of a word in given string
str = input ("Enter a string: ")
subStr = []
#Split the given string into words and store in a list
subStr = str.split()
uniqueWords = set (subStr)
wordFreq = {}
for x in uniqueWords:
       wordFreq[x]= subStr.count(x)

val = list(wordFreq.values())
keyVal = list(wordFreq.keys())
 
minVal =  min(val)
minOccur = keyVal[val.index(min(val))]

print ("Min Occuured word: {} for {} times".format(minOccur, minVal))