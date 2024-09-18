"""
this file is the solution of ELZERO WEB SCHOOL assignments 33 to 37

### User input & Practice ###
"""

# solution 1
name = input("Enter your name please: ").strip().title()
print(f"hello {name}, Happy to see you Here")
#solution 2
age = int(input("Enter your age please: "))
if age < 16:
    print("Hello Your Age Is Under 16, Some Articles Is Not Suitable For You")
else:
    print(f"Hello Your Age Is {age}, All Articles Is Suitable For You")

#solution 3
fname = input("Enter your first name: ").strip().capitalize()
lname = input("Enter your last name: ").strip().capitalize()
print(f"hello {fname} {lname:.1s}")


#solution 4
email = input("Your email please: ").strip().lower()
print("name: "+email[:email.index("@")].replace("."," ").capitalize())
print("host: "+email[email.index("@")+1:email.index(".",email.index("@"))])
print("domain: "+email[email.index(".",email.index("@")) + 1 :])