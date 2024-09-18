"""
this file is the solution of ELZERO WEB SCHOOL assignments 33 to 37

### Loop For and training ###
"""


# Solution 1
my_nums = [15, 81, 5, 17, 20, 21, 13]
my_nums.sort(reverse=True)
count = 1
for num in my_nums:
    if num % 5 == 0:
        print(f"{count} => {num}")
        count +=1
print("All Numbers Printed")


# Solution 2
for num in range(1,21):
    if num == 6 or num == 8 or num == 12:
        continue
    if  num < 10:
        print(f"0{num}")
    else:
        print(num)
print("All element printed")


# Solution 3
my_ranks = {
  'Math': 'A',
  "Science": 'B',
  'Drawing': 'A',
  'Sports': 'C'
}
equa = 0
for key, value in my_ranks.items():
    if value == 'A':
        equa += 100
        print(f" My rank in {key} is {value} and this equal 100 Points")
    elif value == 'B':
        equa += 80
        print(f" My rank in {key} is {value} and this equal 80 Points")
    elif value == 'C':
        equa += 40
        print(f" My rank in {key} is {value} and this equal 40 Points")
print(f"total points = {equa}")


# Solution 4
students = {
  "Ahmed": {
    "Math": "A",
    "Science": "D",
    "Draw": "B",
    "Sports": "C",
    "Thinking": "A"
  },
  "Sayed": {
    "Math": "B",
    "Science": "B",
    "Draw": "B",
    "Sports": "D",
    "Thinking": "A"
  },
  "Mahmoud": {
    "Math": "D",
    "Science": "A",
    "Draw": "A",
    "Sports": "B",
    "Thinking": "B"
  }
}

for student in students:
    print("\n")
    print("-" * 20)
    print(f"  student: {student}")
    print("-" * 20)
    total = 0
    for key, value in students[student].items():
        if value == 'A':
            total +=100
            print(f"{key} => 100 points")        
        elif value == 'B':
            total +=80
            print(f"{key} => 80 points")        
        elif value == 'C':
            total +=40
            print(f"{key} => 40 points")        
        elif value == 'D':
            total +=20
            print(f"{key} => 20 points")
    print(f"\n{student} total = {total}")    
