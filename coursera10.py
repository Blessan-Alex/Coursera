fname='mbox-short.txt'
fh=open(fname)
w=list()
count=dict()
for line in fh:
    if line.startswith('From'):
        word=line.split()
        if word[0]=='From':
         w.append(word[1])
         ##print(word1)
##print(w)
for words in w:
    count[words]=count.get(words,0)+1
bigcount=None
bigword=None
for words,count in count.items():
    if bigcount is None or count > bigcount:
        bigword=words
        bigcount=count
print(bigword,bigcount)
