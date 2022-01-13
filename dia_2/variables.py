#Day 2: 30 Days of python programming

#Declare a first name variable and assign a value to it
primer_nombre = 'Marbellys'

#Declare a last name variable and assign a value to it
segundo_nombre = 'Campos'

#Declare a full name variable and assign a value to it
nombre_y_apellido = 'Marbellys Campos'

#Declare a country variable and assign a value to it
pais = 'Venezuela'

#Declare a city variable and assign a value to it
ciudad = 'Puerto Ordaz'

#Declare an age variable and assign a value to it
edad = 50

#Declare a year variable and assign a value to it
anno = 2022

#Declare a variable is_married and assign a value to it
es_casado = 'S'

#Declare a variable is_true and assign a value to it
es_verdad = True

#Declare a variable is_light_on and assign a value to it
luz_encendida = False

#Declare multiple variable on one line
profesion, sexo = 'Ingeniero','F'

#  Exercises: Level 2

# Check the data type of all your variables using type() built-in function

print(type(primer_nombre))
print(type(segundo_nombre))
print(type(nombre_y_apellido))
print(type(pais))
print(type(ciudad))
print(type(edad))
print(type(anno))
print(type(es_casado))
print(type(es_verdad))
print(type(luz_encendida))
print(type(profesion))
print(type(sexo))

 
# Using the len() built-in function, find the length of your first name
print(len(primer_nombre))
print(len(segundo_nombre))

# Compare the length of your first name and your last name
if len(primer_nombre) == len(segundo_nombre):
    print('igual tamaño')
elif  len(primer_nombre) > len(segundo_nombre):
    print('primer nombre mayor')
else:
    print('primer nombre menor')
    
# Declare 5 as num_one and 4 as num_two
num_one = 5
num_two = 4

# Add num_one and num_two and assign the value to a variable total
total = num_one + num_two

# Subtract num_two from num_one and assign the value to a variable diff
diff = num_one - num_two

# Multiply num_two and num_one and assign the value to a variable product
product = num_one * num_two

# Divide num_one by num_two and assign the value to a variable division
division = num_one / num_two

# Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder = num_two % num_one

# Calculate num_one to the power of num_two and assign the value to a variable exp
exp = num_one ** num_two

# Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division = num_one // num_two


#The radius of a circle is 30 meters. 
#Calculate: the area of a circle and assign the value to a variable name of area_of_circle
pi = 3.1416
r = 30
area_of_circle = pi * r**2
print(f'El area de un circulo con radio de {r} metros es: {area_of_circle} ')

#Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
#c=2r* pi
circum_of_circle = 2*r*pi
print(f'La circunferencia del circulo con radio de {r} metros es: {circum_of_circle} ')

#Take radius as user input and calculate the area.
radio = input('Radio de la circunferencia:')

area_of_circle = pi * (float(radio)**2)
print(f'El area de lacircunferencia de radio {radio}, es {area_of_circle}')

#Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
first_name = input('Nombre:')
last_name = input('Apellido:')
country = input('Pais:')
age = input('Edad:')

#Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords

