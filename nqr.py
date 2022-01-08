V = int(input("Enter the total number of vehicles: "))
print("Total number of vehicles(two-wheeler + four-wheeler) are {}".format(V))
W = int(input("Enter the total number of Wheels: "))
print("Total number of Wheels are {}".format(W))

FW = (W/2) - V
print("Number of Four wheelers is {}".format(int(FW)))

TW = V - FW
print("Number of Two wheelers is {}".format(int(TW)))
