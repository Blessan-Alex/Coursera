hours=input('enter hours')
rate=input('enter rate')
try:
    hr=float(hours)
    r=float(rate)
except:
    print('error')
    quit()
if(hr>40) :
    reg=hr*r
    otp=(hr-40)*(r*0.5)
    xp=reg+otp
else:
    xp=hr*r
print('pay ',xp)
    
