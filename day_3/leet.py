def addDigits( num: int) -> int:
        s=0
        while num!=0:
            d=num%10
            s=s+d
        if len(str(s))==1:
            return s
        addDigits(s)
num=int(input())
print(addDigits(num))
