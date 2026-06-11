n=int(input())
arm=0
temp=n


while n>0:
    digit=n%10
    arm+=digit**3
    n//=10

if temp==arm:
    print(f"{temp} is an armstrong number")
else:
    print(f"{temp} is not an armstrong number")
