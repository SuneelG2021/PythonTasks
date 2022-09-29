#str=input("Enter a string: ")
str = "Sun Tue Wed Sun"
subStr = [] 
subStr = str.split()
print (subStr)

wordFreq = {}

for i in subStr:
    if i in wordFreq:
        wordFreq[i] = wordFreq[i] + 1
    else:
        wordFreq[i]=1
result = max(wordFreq, key = wordFreq.get)
print (wordFreq.get)
print (result)