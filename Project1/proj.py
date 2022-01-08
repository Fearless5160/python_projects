print("Enter the word:")
word=input().split()
a=0
for i in range(0,len(word[0])):
    for j in range(i+1,len(word[0])):
        if word[0][i] == word[0][j]:
           a=1

if a==0:
    print("True")
if a==1:
    print("False")


