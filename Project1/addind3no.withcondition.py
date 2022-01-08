=input('Entere three inetege:')
list=A.split(',')

x=int("%s"%list[0])
y=int("%s"%list[1])
z=int("%s"%list[2])
def  sum(x,y,z):
    if (x==y or y==z or x==z):
        sum=0
    else:
        sum=x+y+z
    return sum
print(sum(x,y,z))