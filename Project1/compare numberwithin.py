def compare(n):
    if (abs(2000-n)<=100) or (abs(n-2000)<=100):
        print("The number is within 100 to 2000")
    elif (abs(1000-n)<=100) or (abs(n-1000)<=100):
        print("The number is within 100 to 1000")
    else:
        print("The number is beyond 100 to 2000 or 1000")

n=int(input("enter the number:"))
print(compare(n))