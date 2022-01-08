sub = 1
star1 = ""
num = int(input("Enter number of Rows: "))
# number of Rows
star = (2 * num) - 1
# number of star in base rows
for i in range(1, num + 1):
    gap = (star - sub)/2
    star1 = ( " " * int(gap)) + ("*" * sub)
    sub = sub + 2
    print(star1)
