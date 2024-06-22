# float -> floating point values 
x=123.369
print(type(x))

# round(number, ndigits=None)
x=float(input("Enter your number-"))
y=float(input("Enter your number-"))
z=(x*y)
print(z)
z=round(z)
print(f"{z:,}")

print(f"{z:.2f}")