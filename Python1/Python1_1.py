def formatNum(number):
    return ("{:,}".format(number)) 

print("*** Converting hh.mm.ss to seconds ***")
h, m, s = [int(x) for x in input("Enter hh mm ss : ").split()]
hh, mm, ss = ['','',''] #turn int to str
t = 0
t += h*60*60
t += m*60
t += s

if h < 10:
    hh = f"0{h}"
else:
    hh = f"{h}"
    
if m < 10:
    mm = f"0{m}"
else:
    mm = f"{m}"

if s < 10:
    ss = f"0{s}"
else:
    ss = f"{s}"

if h < 0:
    print("hh",'(',h,')'," is invalid!",sep=(""))
if m >= 60 or m < 0:
    print("mm",'(',m,')'," is invalid!",sep=(""))
elif s >= 60 or s < 0:
    print("ss",'(',s,')'," is invalid!",sep=(""))
else:
    print(hh,':',mm,':',ss," = ",formatNum(t)," seconds",sep="")