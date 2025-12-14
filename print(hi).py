print("enter the number to convert temperature")
print("1.convert fahreheit to celsius ")
print("2.convert celsius to  fahreheit ")

choice = input("enter the number between(1 or 2): ")
if choice == "1":
    fahreheit = float(input("enter the temperature:"))
    celsius = (fahreheit - 32) * 5 / 9
    print(f"{fahreheit}F is equal to {celsius}C")
if choice == "2":
    celsius = float(input("enter the temperature: "))
    fahreheit = (celsius * 9 / 5) + 32
    print(f"{celsius}C is equal to {fahreheit}F")
else :
    print(" invalid number")

    print (f"the value of  celsius {celsius}")
    print (f"the value of fahreheit  {fahreheit}")



