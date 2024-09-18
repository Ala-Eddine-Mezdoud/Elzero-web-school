"""
this file is the solution of ELZERO WEB SCHOOL assignments 24 to 25

### Tuples & Methods ###
"""


#solution 1
myTuple = ("Osama",) # we add "," at the end to endicate that this a typle and not a string
print(myTuple[0])       # "Osama"
print(type(myTuple))    # <class 'tuple'>


#solution 2
friends = ("Osama", "Ahmed", "Sayed")
friends = ("Elzero",) + friends[1:]
print(friends)          # ("Elzero", "Ahmed", "Sayed")
print(type(friends))    # <class 'tuple'>
print(len(friends))     # 3 Elements


#solution 3
nums = (1, 2, 3)
letters = ("A", "B", "C")
nums_and_letters_one = nums + letters
print("nums_and_letters_one = "+ str(nums_and_letters_one))         # nums_and_letters_one = (1, 2, 3, "A", "B", "C")
print(str(len(nums_and_letters_one)) + " Elements")    # 6 Elements


#solution 4
my_tuple = (1, 2, 3, 4)
a,b,_,c = my_tuple
print(a)    # 1
print(b)    # 2
print(c)    # 4