print("*** Reading E-Book ***")
txt, highLight = input("Text , Highlight : ").split(',')

for i in txt:
    if i == highLight:
        print("[%c]"%(highLight),end="")
    else:
        print(i,end="")