number=input("enter the number:")
list=[]
for i in number:
     list.append(i)
print(list)
comp=['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
print(comp)
value=[]
novalue=[]
for k in comp:
    if k in list:
        value.append(k)
    else:
        novalue.append(k)
print("value present in the number:",value)
print("value not present in number:",novalue)
