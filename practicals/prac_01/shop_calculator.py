
number = int(input("Number of items: "))
total = 0

while number < 0:
    print("Invalid number of items!")
    number = int(input("Number of items: "))

for i in range(number):
    price = float(input("Price of item: "))
    total += price

if total > 100:
    total *= 0.9  # apply 10% discount

print("Total price for ", number, " items is $", total, sep='')

print("Total price for {} items is ${:.2f}".format(number, total))
