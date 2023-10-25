def swapList(newList):
    size = len(newList)
    temp = newList[0]
    newList[0] = newList[size-1]
    newList[size-1]= temp
    return newList

newList = [11,15,19,18,17]
print(swapList(newList))