def armstrong(n,l):
  s=0
  while n>0:
        s=s+(n%10)**l
        n//=10
  return s
n=int(input("enter the number"))
l = len(str(n))
sum=armstrong(n,l)
if sum==n:
        print("Is armstrong")
else:
        print("Is not armstrong")