part = input("Enter Parent Member name:").split(",")
cho = input("Enter Y if  Parent member has child members otherwise enter N: ")
if cho == "N":
    print("TOTAL MEMBER: {}".format(len(part)))
    print("COMISSION DETAILS")
    print("{}: 250 INR".format(part[0]))
elif cho =="Y":
    child = input("Enter Child Member:").split(",")
    print("TOTAL MEMBER: {}".format(len(part)+len(child)))
    print("COMISSION DETAILS")
    print("{}: {}INR".format(part[0],500*len(child)))
    for i in child:
        print("{}: 250 INR".format(i))
else:
    print("INVALID INPUT")
