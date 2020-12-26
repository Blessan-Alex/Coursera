fname=input("enter file name ")
fh=open(fname)
lst=list()
for line in fh:
    line=line.rstrip()
    line=line.split()
    for a in line:
        if a in lst:
            continue
        else:
            lst.append(a)
lst.sort()
print (lst)\
