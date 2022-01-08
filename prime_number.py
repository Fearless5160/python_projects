low = int(input("enter the lower bound: "))
high = int(input("enter the upper bound: "))
sum = 0
sum_1 = 0
if (low or high) < 0:
    print("Number is negative")

for i in range(low,high+1,1):
    for j in range(2,i):
        if i % j == 0:
            sum_1 = 0
            break
        else:
            sum_1 = i
    sum = sum + sum_1

print(sum)