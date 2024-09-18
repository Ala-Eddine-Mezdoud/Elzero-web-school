"""
this file is the solution of ELZERO WEB SCHOOL assignments 33 to 37

### Operators & Type convesion ###
"""



#solution 1
print(bool(1))
print(bool(1.5))
print(bool("hello world"))
print(bool([1,2]))
print(bool([]))
print(bool(0))
print(bool(""))
print(bool(None))


#solution 2
html = 80
css = 60
javascript = 70
print((html and css and javascript)> 50)


#solution 3
num_one = 10
num_two = 20
num = 20
print((num_one or num_two) < num)
print((num_one and num_two) < num)


#solution 4
num_one = 10
num_two = 20
result = num_one + num_two 
print(result)
print(result**3)
print( ( (result**3) % 26000) / 5 )
print( type (str(( (result**3) % 26000) / 5 )))