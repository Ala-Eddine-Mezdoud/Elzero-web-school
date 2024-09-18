"""
this file is the solution of ELZERO WEB SCHOOL assignments 26 to 32

### Set,Dectionary & Methods ###
"""

#solution 1
my_list = [1, 2, 3, 3, 4, 5, 1]
unique_list = [1,2,3,4,5]
print(unique_list)                          # 1, 2, 3, 4, 5
print(type(unique_list))                    # <class 'list'>
print(unique_list[:len(unique_list)-1])     # 1, 2, 3, 4


#solution 2
nums = {1, 2, 3}
letters = {"A", "B", "C"}
set_one = set(nums)
set_two = set(letters)

print(set_one.union(set_two))        #Method one


print(set_one | set_two)             #Method two

set_one.update(set(letters))
print(set_one)                       #Method three


#solution 3
my_set = {1, 2, 3}
letters = {"A", "B", "C"}

print(my_set)               # {1, 2, 3}

my_set.clear()
print(my_set)               # set()

my_set.update(letters)
my_set.remove("C")
print(my_set)               # {"A", "B"}


#solution 4
set_one = {1, 2, 3}
set_two = {1, 2, 3, 4, 5, 6}
print(set_one.issubset(set_two))        #Method one
print(set_one.issuperset(set_one))      #Method two


#solution 5
my_dic = {
    "HTML":"90%",
    "CSS":"80%",
    "Python":"30%",
    "AI":"20%"
}

print(f"HTML Progress is {my_dic["HTML"]}")         #"HTML Progress Is 90%"
print(f"CSS Progress is {my_dic["CSS"]}")           #"CSS Progress Is 80%"       
print(f"Python Progress is {my_dic["Python"]}")     #"Python Progress Is 30%"
print(f"AI Progress is {my_dic["AI"]}")             #"AI Progress Is 20%"