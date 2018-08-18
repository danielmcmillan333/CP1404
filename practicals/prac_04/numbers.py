
numbers = []

number_count = 0

while number_count < 5:
    number = int(input("Number: "))
    numbers.append(number)
    number_count += 1

print("The first number is {}".format(numbers[0]))
print("The last number is {}".format(numbers[-1]))
print("The smallest number is {}".format(min(numbers)))
print("The largest number is {}".format(max(numbers)))
average = sum(numbers) / len(numbers)
print("The average of the numbers is {}".format(average))
