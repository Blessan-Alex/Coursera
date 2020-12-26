
fname=input('Enter filename : ')
fh=open(fname)
dictionary=dict()
lists=list()
tn=list()
for line in fh:
    if line.startswith('From'):    
        word=line.split()
        ##print(word)
        if word[0]=='From':
         time=word[5]
         time=time.split(':')
         ##print(time)
         tn.append(time[0])
##print(tn)
for t in tn:
     dictionary[t]=dictionary.get(t,0)+1
##print(dictionary)
for k,v in sorted(dictionary.items()):
    print(k,v)
