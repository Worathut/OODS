print("*** Mod Position ***")
txt, modPos = input("Enter Input : ").split(",")
countTxt = 0
lst = []
for i in txt:
    countTxt+=1
    if countTxt%int(modPos) == 0:
        lst.append(i)
print(lst)