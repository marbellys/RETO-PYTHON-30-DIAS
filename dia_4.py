#Ing. Marbellys Campos

# Exercises - Day 4
# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
esp =' '
concatenar = 'Thirty' +esp+ 'Days'+esp+ 'Of' +esp+ 'Python'
print(concatenar)
# Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'.
concatenar2 = 'Coding' + esp + 'For'+ esp + 'All' 
print(concatenar2)

# Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding For All"
# Print the variable company using print().
print(company)
# Print the length of the company string using len() method and print().
print(len(company))
# Change all the characters to uppercase letters using upper() method.
print(company.upper())
# Change all the characters to lowercase letters using lower() method.
print(company.lower())
# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(company.title())
print(company.swapcase())

# Cut(slice) out the first word of Coding For All string.
primera_palabra = company[:6]
print(primera_palabra)

#otra forma:
mi_lista = company.split()
primera_palabra_l = mi_lista[0]
print(primera_palabra_l)

# Check if Coding For All string contains a word Coding using the method index, find or other methods.

palabra = 'Coding' 
buscar = company.find(palabra)
if buscar > -1:
    print('encontro la palabra')
else:
    print('NO encontro la palabra')

# Replace the word coding in the string 'Coding For All' to Python.
reemplazar = company.replace('Coding','Python')
print(reemplazar)

# Change Python for Everyone to Python for All using the replace method or other methods.
stri ='Python for Everyone'
print(stri.replace('Everyone','All'))

# Split the string 'Coding For All' using space as the separator (split()) .
palabra = 'Coding For All'
separar = palabra.split(' ')
print(separar)
# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
rs =  "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
lista_rs = rs.split(',')
print(lista_rs)
# What is the character at index 0 in the string Coding For All.
texto = 'Coding For All'
print(texto[0])

# What is the last index of the string Coding For All.
texto = 'Coding For All'
ult_l = len(texto)-1
print(ult_l)

#otra forma"
texto = 'Coding For All'
ult_l = texto[-1]
ult_f = texto.rfind(ult_l)
print(ult_f)

#otra forma"
texto = 'Coding For All'
ult_l = texto[-1]
ult_f = texto.rindex(ult_l)
print(ult_f)

# What character is at index 10 in "Coding For All" string.
texto = 'Coding For All'
print(texto[10]) #" "

# Create an acronym or an abbreviation for the name 'Python For Everyone'.

# Create an acronym or an abbreviation for the name 'Coding For All'.

# Use index to determine the position of the first occurrence of C in Coding For All.
texto = 'Coding For All'
caracter = 'C'
p = texto.index(caracter)
print(p) #

# Use index to determine the position of the first occurrence of F in Coding For All.
texto = 'Coding For All'
caracter = 'F'
p = texto.index(caracter)
print(p) #

# Use rfind to determine the position of the last occurrence of l in Coding For All People.
texto = 'Coding For All'
caracter = 'l'
p = texto.rfind(caracter)
print(p) #

# Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
texto = 'You cannot end a sentence with because because because is a conjunction'
caracter = 'because'
p = texto.find(caracter)
print(p) #

# Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
texto = 'You cannot end a sentence with because because because is a conjunction'
caracter = 'because'
p = texto.rindex(caracter)
print(p) #

# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
texto = 'You cannot end a sentence with because because because is a conjunction'
fuera = texto[31:54]
print(fuera) #because because because

# Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
texto = 'You cannot end a sentence with because because because is a conjunction'
pri = texto.find('because')
print(pri) #31

# Does ''Coding For All' start with a substring Coding?

# Does 'Coding For All' end with a substring coding?
texto = 'Coding For All'

print(texto.endswith('Coding'))  #False

# '   Coding For All      '  , remove the left and right trailing spaces in the given string.
texto = '   Coding For All      '
texto = texto.strip(' ')
print(texto)

# Which one of the following variables return True when we use the method isidentifier():

# 30DaysOfPython
# thirty_days_of_python   
#esta: # thirty_days_of_python   


# The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
texto =  ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
union = '# '.join(texto)
print(union)

# Use the new line escape sequence to separate the following sentences.
# I am enjoying this challenge.
# I just wonder what is next.
print('I am enjoying this challenge. \nI am enjoying this challenge')

# Use a tab escape sequence to write the following lines.
# Name      Age     Country   City
# Asabeneh  250     Finland   Helsinki
print('Name\tAge\tCountry\tCity')
print('Asabeneh\t250\tFinland\tHelsinki')

# Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
texto = 'The area of a circle with radius %d is %2.f meters square.' %(radius,area)
print(texto)


# Make the following using string formatting methods:
# 8 + 6 = 14
# 8 - 6 = 2
# 8 * 6 = 48
# 8 / 6 = 1.33
# 8 % 6 = 2
# 8 // 6 = 1
# 8 ** 6 = 262144



nombre = 'Marbellys'
edad = 50
profesion = 'Ingeniero'
hijos = 2
historial = 'Mi nombre es {}, tengo {} años de edad. Soy {} y tengo {} hijos'.format(nombre,edad,profesion,hijos)
print(historial)

historial2 = f'Mi nombre es {nombre.upper()}, tengo {edad} años de edad. Soy {profesion} y tengo {hijos} hijos'

print(historial2)
nombre6 = 'Mi nombre es marbellys campos'
nombre7 = nombre6.replace(' ','|')
print(nombre7)
nombre5 = 'Mi nombre es marbellys campos'
print(nombre5.split())
print(nombre7.split('|'))