# Exercises - Day 3
# 1.	Declare your age as integer variable

edad = 45
print('edad',edad)

# 2.	Declare your height as a float variable
altura = 1.54 
print('altura:',altura)

# 3.	Declare a variable that store a complex number
complejo = 1 + 5j

# 4.	Write a script that prompts the user to enter base and height of the triangle and calculate an area of this triangle (area = 0.5 x b x h).
#     Enter base: 20
base = input('Base del triangulo:')

#     Enter height: 10
altura = input('Altura del triangulo:')
#     The area of the triangle is 100
area = 0.5 * float(base) * float(altura)
print('Area del triangulo: ',area)

# 5.	Write a script that prompts the user to enter side a, side b, and side c of the triangle. Calculate the perimeter of the triangle (perimeter = a + b + c).
# Enter side a: 5
a = input('lado a:?')
# Enter side b: 4
b = input('lado b:?')
# Enter side c: 3
c = input('lado c:?')

# The perimeter of the triangle is 12
perimetro = float(a) + float(b) + float(c)
print('Area del triangulo: ',perimetro)

# 6.	Get length and width of a rectangle using prompt. Calculate its area (area = length x width) and perimeter (perimeter = 2 x (length + width))
ancho = input('ancho:?')
altura = input('Altura:?')

#     The area of the triangle is 100
area = float(ancho) * float(altura)
perimetro = 2 * (float(ancho) + float(altura))

print('Area: ',area, ' .....perimetro:', perimetro)


# 7.	Get radius of a circle using prompt. Calculate the area (area = pi x r x r) and circumference (c = 2 x pi x r) where pi = 3.14.
pi = 3.1416
radio = input('radio:?')
area = pi * float(radio) * float(radio)
circunferencia = 2 * float(pi) * float(radio)

print('Area: ',area, ' .....circunferencia:', circunferencia)

# 8.	Calculate the slope, x-intercept and y-intercept of y = 2x -2


# 9.	Slope is (m = y2-y1/x2-x1). Find the slope and Euclidean distance between point (2, 2) and point (6,10)
# 10.	Compare the slopes in tasks 8 and 9.
# 11.	Calculate the value of y (y = x^2 + 6x + 9). Try to use different x values and figure out at what x value y is going to be 0.
# 12.	Find the length of 'python' and 'dragon' and make a falsy comparison statement.
if len('python') == len('dragon'):
    print(' las palabras dagron y python, tienen la misma cantidad de letras')

# 13.	Use and operator to check if 'on' is found in both 'python' and 'dragon'
if 'on' in ('python' and 'dragon'):
     print(' si esta')
else:
    print(' NO esta')
    
# 14.	I hope this course is not full of jargon. Use in operator to check if jargon is in the sentence.
if 'jargon' in 'I hope this course is not full of jargon':
      print(' si esta')
    
# 15.	There is no 'on' in both dragon and python
if 'on' not in ('python' and 'dragon'):
     print(' No esta')
else:
    print(' Si esta')
    
# 16.	Find the length of the text python and convert the value to float and convert it to string
l = len('python')
f = float(l)
s = str(f)
print('float:',f)
print('str:',s)


# 17.	Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?
x = 36
if x % 2 == 0:
    print('par') 
# 18.	Check if the floor division of 7 by 3 is equal to the int converted value of 2.7.
# 19.	Check if type of '10' is equal to type of 10
if type('10') is type(10):
    print('Tipos iguales')
else:
    print('tipos diferentes')
# 20.	Check if int('9.8') is equal to 10
n = 9.8
if int(n) == 10:
    print("int('9.8') is equal to 10",)
else:
    print("int('9.8') NO is equal to 10 es igual a:",int(n))

# 21.	Writ a script that prompts the user to enter hours and rate per hour. Calculate pay of the person?
