ls = []
num = int(input('How many numbers: '))
for n in range(num):
    numbers = int(input('Enter number '))
    ls.append(numbers)
print("Sum of elements in given list is :", sum(ls))
