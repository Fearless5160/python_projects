n = int(input("Enter the number: "))

binary = ""
for i in range(0,100):
    if n > (2 ** i):
        value = i
    else:
        break

for i in range(value,-1,-1):
    if n >= (2**i):
        n = n - (2**i)
        binary = binary + "1"
    else:
        binary = binary + "0"

print(binary)