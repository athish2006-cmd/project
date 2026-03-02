numbers = input ("Enter a list of numbers separated by spaces: ")
number =[int(num) for num in numbers.split()]
print("choose sorting order.")
print("1. Ascending ")
print("2. Descending ")

choice = input("Enter choice (1 or 2): ") 

if choice == "1":
    number.sort()
    print("Numbers sorted  in ascending order:", number)
elif choice == "2":
    number.sort(reverse=True)
    print("Numbers sorted in descending order:", number)
else:
    print("Invalid choice. please enter 1 or 2.")