"""
this file is the solution of ELZERO WEB SCHOOL assignments 33 to 37

### Control Flow ###
"""

#solution 1
while True:
    operation =  input("Choose your operation: \n\t'+' Addition\n\t'-' Substartion\n\t'*' Multiplication\n\t'/' Division\n\t'%' Modulus\n\t'q' Quit the app\nChoice: ").strip()
    if operation == '+':
        num1 = int(input("\tFirst number = "))
        num2 = int(input("\tSecond number = "))
        print(str(num1) + " + "+ str(num2) + " = " + str(num1 + num2))
    elif operation == '-':
        num1 = int(input("\tFirst number = "))
        num2 = int(input("\tSecond number = "))
        print(str(num1) + " - "+ str(num2) + " = " + str(num1 - num2))
    elif operation == '*':
        num1 = int(input("\tFirst number = "))
        num2 = int(input("\tSecond number = "))
        print(str(num1) + " * "+ str(num2) + " = " + str(num1 * num2))
    elif operation == '/':
        num1 = int(input("\tFirst number = "))
        num2 = int(input("\tSecond number = "))
        print(str(num1) + " / "+ str(num2) + " = " + str(num1 / num2))
    elif operation == '%':
        num1 = int(input("\tFirst number = "))
        num2 = int(input("\tSecond number = "))
        print(str(num1) + " % "+ str(num2) + " = " + str(num1 % num2))
    elif operation == "q":
        break
    else:
        print("Invalid choice")


#solution 2
age = int(input("Your age please: ").strip())
print("App is suitable for you" if age > 16 else "App is not suitable for you")


#solution 3
age = int(input("your age please: ").strip())
if age >= 10 and age <= 100:
    print("You lived for: ")
    print(f"\t{age * 365 * 24 * 60 * 60} seconds")
    print(f"\t{age * 365 * 24 * 60} minutes")
    print(f"\t{age * 365 * 24} hours")
    print(f"\t{age * 365} days")
    print(f"\t{age * 12 * 4} weeks")
    print(f"\t{age * 12} Months")
else : 
    print("age out of range 10 to 100")


#solution 4
country = input("Input Your Country ").strip().title()
countries = ["Egypt", "Palestine", "Syria", "Yemen", "KSA", "USA", "Bahrain", "England"]
price = 100
discount = 30
if country in countries:
    print(f"Your Country {country} Eligible For Discount And The Price After Discount Is ${price - discount}")
else:
    print(f"Your Country Not Eligible For Discount And The Price Is ${price}")
