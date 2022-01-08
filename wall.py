interior = int(input("Enter the number of interior wall: "))
exterior = int(input("Enter the number of exterior wall: "))
sum_int = 0.0
sum_ext = 0.0

for i in range(1,interior+1):
    sum_int = sum_int + float(input())

for i in range(1,exterior+1):
    sum_ext = sum_ext + float(input())

total = (sum_int * 18) + (sum_ext * 12)

print("Total estimated Cost : {} INR".format(total))