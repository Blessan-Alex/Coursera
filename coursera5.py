text = "X-DSPAM-Confidence:    0.8475"
pos1=text.find('0.8475')
pos2=pos1+6
sentence=float(text[pos1:pos2])
print(sentence)
