"""
this file is the solution of ELZERO WEB SCHOOL assignments 33 to 37

### Loop While and training ###
"""

#solution 1
num = int(input("Enter number greater than 0\n").strip())
if num <= 0:
    print(f"numer {num} is not larger than 0")
else:
    print("\n")
    count = 0
    while num>=1:
        if num == 6:
            num -=1
            continue
        print(num)
        count +=1
        num -=1
    print(f"{count} Printed successfully")


#solution 2
friends = ["Mohamed", "Shady", "ahmed", "eman", "Sherif"]
count = 0
for friend in friends:
    if friend == friend.title():
        print(friend)
    else:
        count +=1
print(f"All freinds are printed \nIgnored freinds count is {count}")


#solution 3
skills = ["HTML", "CSS", "JavaScript", "PHP", "Python"]

while skills:
    print(f"skill => {skills.pop(0)}")


#solution 4
my_freinds = []
while len(my_freinds)<4:
    name = input("name: ").strip()
    if name == name.upper():
        print("Invalid name")
    else :
        if name == name.title():
                my_freinds.append(name)
                print(f"'{name}' added to your freind list")
                print(f"Places left on the list => {4 - len(my_freinds)}")
        else: 
            name = name.title()
            print(f"name after modification '{name}'")
            my_freinds.append(name)
            print(f"'{name}' added to your freind list")
            print(f"Places left on the list => {4- len(my_freinds)}")
