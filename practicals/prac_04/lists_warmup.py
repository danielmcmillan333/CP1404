
numbers = [3, 1, 4, 1, 5, 9, 2]

# 1

numbers.pop(0)
numbers[0] = "ten"

# 2

numbers.pop(0)
numbers[-1] = 1

# 3

print(numbers[2:len(numbers)])

# 4

if 9 in numbers:
    print("True")
else:
    print("False")

