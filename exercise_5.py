def rect(length=5,width=5,symbol='*'):
    symbol = symbol * width
    for y in range(0,length):
        print(symbol)

rect()
rect(4,3,)
rect(2,6,'!')