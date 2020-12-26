count=0
fname = input("Enter file name: ")
fh = open(fname)
add=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
     continue
    pos1=line.find(':')
    sentence=line[pos1+1:]
    number=float(sentence)
    count+=1
    add+=number
avg=add/count
print('Average spam confidence: ',avg)