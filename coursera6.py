fname=input('enter file name ')
try:
    fh=open(fname)
except:
    print('cannot find file named',fname,'best of luck next time')
    quit()
for line in fh:
    line=line.upper()
    line=line.rstrip()
    print(line)
