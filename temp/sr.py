x = 'Sally likes to eat pie and Sally likes to have chocolate'


wordDict = {}
wordArr = x.split(' ')

print(wordArr)


for word in wordArr:
    if word in wordDict:
        wordDict[word] += 1
    else:
        wordDict[word] = 1


count = 0
for key, value in wordDict.items():
    if value > 1:
        count += 1
        
print(count)
    
