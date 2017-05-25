"""List comprehension is a complete substitute for thee lambda function as well as
the functions map(),filter() and reduce().For most people the syntax of list comprehension is
easier to be grasped"""

#Example:

Celsius=[39.2,36.5,37.3,37.8]
Fahrenheit=[((float(9)/5)*x+32) for x in Celsius]

result=[(x,y,z) for x in range(1,30) for y in range(x,30) for z in range(y,30 if x**2+y**2==z**2)]
