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
 
maxVal =  max(val)
maxOccur = keyVal[val.index(max(val))]

print ("Max Occuured word: {} for {} times".format(maxOccur, maxVal))