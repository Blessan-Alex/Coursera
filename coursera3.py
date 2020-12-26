
hours=input('enter hours')
rate=input('enter rate')
hr=float(hours)
r=float(rate)
def computepay(hr,r):
    if(hr>40) :
        reg=hr*r
        otp=(hr-40)*(r*0.5)
        xp=reg+otp
    else:
        xp=hr*r
    return xp
print('Pay',computepay(hr,r))