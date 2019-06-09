num=int(input(("enter a number:")))
total=0
while(num>0):
    s=num%10
    total=total+s
    num=num//10
print("sum of digits:",total)
