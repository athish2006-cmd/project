numbers = input("Enter a list of numbers separated by spaces: ").split()
numbers = [int(num) for num in numbers]
total = sum(numbers)
count = len(numbers)
average = total / count
print("average is:", average)
#[1,2,3,4,5,76,7]