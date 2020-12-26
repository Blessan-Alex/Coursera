fname=input('filename: ')
fh=open(fname)
count=0
for line in fh:
    if line.startswith("From"):
        word=line.split()
        if word[0]=='From':
            print(word[1])
            count+=1
print('There were',count, 'lines in the file with From as the first word')

        