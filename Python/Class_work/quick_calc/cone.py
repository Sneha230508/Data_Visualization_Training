import math

r = float(input("Enter radius: "))
h = float(input("Enter height: "))
l = float(input("Enter slant height: "))

volume = (1/3) * math.pi * r * r * h
csa = math.pi * r * l
tsa = math.pi * r * (r + l)

print("Volume =", volume)
print("Curved Surface Area =", csa)
print("Total Surface Area =", tsa)