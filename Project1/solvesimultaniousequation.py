print('Enter the value of a,b,c,d,e,f:for equation\nax+by=c\ndx+ey=f')
a,b,c,d,e,f=map(float,input().split())
n = (a*e) - (b*d)
if n!=0:
    x = (c * e - b * f) / n
    y = (a * f - c * d) / n
print('{:.3f} {:.3f}'.format(x + 0, y + 0))