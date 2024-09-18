"""
this file is the solution of ELZERO WEB SCHOOL assignments 21 to 23

### List & Methods ###
"""

#solution 1
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
print(friends[0])               # "Osama" => Method One
print(friends[-len(friends)])   # "Osama" => Method Two
print(friends[-1])              # "Mahmoud" => Method One
print(friends[4])               # "Mahmoud" => Method Two


#solution 2
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
print(friends[0],friends[2],friends[4] , sep=",")   # "Osama", "Sayed", "Mahmoud"
print(friends[1],friends[3], sep=",")               # "Ahmed", "Ali"


#solution 3
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
print(friends[1],friends[2],friends[3], sep=",")      # "Ahmed", "Sayed", "Ali",
print(friends[-2],friends[-1], sep=",")               # "Ali", "Mahmoud"


#solution 4
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahmoud"]
friends[-1] = "Elzero"
friends[-2] = "Elzero"
print(friends)  # ["Osama", "Ahmed", "Sayed", "Elzero", "Elzero"]


#solution 5
friends = ["Osama", "Ahmed", "Sayed"]
friends.insert(0,"Nasser")
friends.append("Salem")
print(friends)  # ["Nasser", "Osama", "Ahmed", "Sayed", "Salem"]


#solution 6
friends = ["Nasser", "Osama", "Ahmed", "Sayed", "Salem"]
friends.remove("Nasser")
friends .remove("Osama")
print(friends)  # ["Ahmed", "Sayed", "Salem"]
friends.pop()
print(friends)  # ["Ahmed", "Sayed"]


#solution 7
friends = ["Ahmed", "Sayed"]
employees = ["Samah", "Eman"]
school = ["Ramy", "Shady"]
friends.extend(employees)
friends.extend(school)
print(friends)  # ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]


#solution 8
friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]
friends.sort()
print(friends)  # ['Ahmed', 'Eman', 'Ramy', 'Samah', 'Sayed', 'Shady']
friends.sort(reverse=True)
print(friends)  # ['Shady', 'Sayed', 'Samah', 'Ramy', 'Eman', 'Ahmed']


#solution 9
friends = ["Ahmed", "Sayed", "Samah", "Eman", "Ramy", "Shady"]
print(len(friends)) # 6


#solution 10
technologies = ["Html", "CSS", "JS", "Python", ["Django", "Flask", "Web"]]
print(technologies[-1][0])  # Django
print(technologies[-1][-1]) # Web