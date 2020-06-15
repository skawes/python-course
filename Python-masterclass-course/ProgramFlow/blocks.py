for i in range(1,12):
    print("No {} has squared {} and cube {}".format(i,i*i,i*i*i))
print("*"*80)

name=input("Enter your name")
age=int(input("whats your age,{0}?".format(name)))
if(age>18):
    print("You are eligible to vote")
else:
    print("You are not eligible")

if(age<18):
    print("age less than 18")
elif age==60:
    print("900")
else:
    print("else")