

num = int(input("enter a number: "))

if num>0 and num < 100 :
    if num % 2==0:
        print(num, "is even")
    else:
        print(num, "is odd")
else:
    print("number must be less than 100 and greater than 0")