"""
this file is the solution of ELZERO WEB SCHOOL assignments 11 to 18

### STRING AND METHODS ###
"""


name = "mezdoud ala eddine"
age = "21"
country = "Algeria"

#solution 1
print("\"hello '" + name + "', How you doing \\ \"\"\" Your age is \"" + age + "\"\" + and your contry Is: " + country)


#solution 2
print("\"hello '" + name + "', How you doing\n \\ \"\"\" Your age is \"" + age + "\"\" +\n and your contry Is: " + country)


#solution 3
name_2 = 'Elzero'
print(name_2[1])    #l
print(name_2[2])    #z
print(name_2[-1])   #o


#solution 4
print(name_2[1:4])       # "lze"
print(name_2[::2])       # "Ezr"
print(name_2[-2::-2])    # "rzE"


#solution 5
name_3 = "#@#@Elzero#@#@"
print(name_3.strip("#@")) # Elzero


#solution 6
num = "9"
print(num.zfill(4)) # 0009
num = "15"
print(num.zfill(4)) # 0015
num = "130"
print(num.zfill(4)) # 0130
num = "950"
print(num.zfill(4)) # 0950
num = "1500"
print(num.zfill(4)) # 1500


# solution 7
name_one = "Osama"
print(name_one.rjust(20,"@")) #@@@@@@@@@@@@@@@Osama
name_two = "Osama_Elzero"
print(name_two.rjust(20,"@")) #@@@@@@@@Osama_Elzero


#solution 8
name_one = "OSamA"
print(name_one.swapcase()) # osAMa
name_two = "osaMA"
print(name_two.swapcase()) # OSAma


#solution 9
msg = "I Love Python And Although Love Elzero Web School"
print("Love count: " + str(msg.count("Love")))


#solution 10
name = "Elzero"
print(name.index("z")) # 2


#solution 11
msg = "I <3 Python And Although <3 Elzero Web School"
print(msg.replace("<3","Love",1)) # I Love Python And Although <3 Elzero Web School


#solution 12
msg = "I <3 Python And Although <3 Elzero Web School"
print(msg.replace("<3","Love")) # I Love Python And Although Love Elzero Web School


#solution 13
name = "Osama"
age = 38
country = "Egypt"
print(f"My name is {name}, And My Age Is {age}, And My Country Is {country}")

# Needed Output Using f""
# My Name Is Osama, And My Age Is 38, And My Country Is Egypt