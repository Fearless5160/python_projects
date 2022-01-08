count1 = 0
count2 = 0

S = str(input("Enter a string consisting * and #:"))

for i in range(0, len(S)):
    if S[i] == "#":
        count1 = count1 + 1

for j in range(0, len(S)):
    if S[j] == "*":
        count2 = count2 + 1

if count1 < count2:
    print("Postive number")
elif count1 > count2:
    print("Negative Number")
else:
    print("0")