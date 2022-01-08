num=input('enter the number:')

string_maps = {
        "1": "abc",
        "2": "def",
        "3": "ghi",
        "4": "jkl",
        "5": "mno",
        "6": "pqrs",
        "7": "tuv",
        "8": "wxy",
        "9": "z"
    }
result=[]
a=string_maps[num[0]]
b=string_maps[num[1]]

for i in a:
    for j in b:
        result.append(i+j)

print(result)



