
def getScore(wordlist, user_wordlist):
    score=0
    if(len(wordlist) != len(user_wordlist)):
        return score
    for i in range(len(wordlist)):
        if wordlist[i].upper() == user_wordlist[i].upper():
            score+=1
    return score
def checkWord(wordList,user_wordList):
    n=len(wordList)
    check=[False] * n
    for i in range(n):
        if wordList[i].upper() == user_wordList[i].upper():
            check[i]=True
    return check