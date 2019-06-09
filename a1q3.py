def binarysearch(a,b):
   f=0
   l=len(a)-1
   found=False
   while f<=l and not found:
       mid=int((f+l)//2)
       if int(a[mid])==b:
           found=True
           return mid+1
       else:
           if b<int(a[mid]):
               l=mid-1
           else:
               f=mid+1
   return found
a=input("enter a sorted list:").split(",")
b=int(input("enter a number:"))
print(binarysearch(a,b))

