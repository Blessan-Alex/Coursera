largest=None
smallest=None
while True:
    num=input('Enter number: ')
    if num=='done':
        break
    try:
        n=float(num)
    except:
        print('Invalid input')
        continue
    if smallest is None:
        smallest=n
    elif n<smallest:
        smallest=n
    elif largest is None:
        largest=n
    elif n>largest:
        largest=n
print('Maximum is ',largest)
print('Minimum is ',smallest)
