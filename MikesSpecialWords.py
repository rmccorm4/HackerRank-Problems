numberWords = input()
myList = []
for line in range(int(numberWords)):
    myList.append(str(input()))

for element in myList:
    ctr=0
    if len(element)%2 == 0:
        middle = len(element)//2
        element1=element[:middle] #yo
        element2=element[middle:] #yo
        for ch in element1:
            if ch not in element2:
                ctr += 1
            else:
                element2 = element2.replace(ch, '', 1)
                
        for ch in element2:
            if ch not in element1:
                ctr += 1
            else:
                element1 = element1.replace(ch, '', 1)
        if ctr != 0:
            print("NO")
        else:
            print("YES")
    elif len(element) == 1:
        print("YES")
    else:
        middle = (len(element)//2) + 1
        element1=element[:middle-1]
        element2=element[middle:]
        for ch in element1:
            if ch not in element2:
                ctr += 1
            else:
                element2 = element2.replace(ch, '', 1)
                
        for ch in element2:
            if ch not in element1:
                ctr += 1
            else:
                element1 = element1.replace(ch, '', 1)
        if ctr != 0:
            print("NO")
        else:
            print("YES")

