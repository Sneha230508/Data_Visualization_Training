l = float(input("Enter length: "))
b = float(input("Enter breadth: "))
h = float(input("Enter height: "))

volume = l * b * h
csa = 2 * h * (l + b)
tsa = 2 * (l*b + b*h + l*h)

print("Volume =", volume)
print("Curved Surface Area =", csa)
print("Total Surface Area =", tsa)