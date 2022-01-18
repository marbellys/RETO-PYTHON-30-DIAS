#Ing. Marbellys Campos

# # Exercises: Day 5
# Exercises: Level 1

# Declare an empty list
lista_v = [] 
print(lista_v)

# Declare a list with more than 5 items
lista = ['bailar','comer','saltar','nadar','dormir'] 
print(lista)

# Find the length of your list
print(len(lista))

# Get the first item, the middle item and the last item of the list
primero = lista[0]
ult = lista[-1]

print(primero,ult)

# Declare a list called mixed_data_types, put your(name, age, height, marital status, address)
mixed_data_types = ['Marbellys','50','1.52','Casada','Venezuela. Edo. Bolivar. pto. Ordaz']
  
# Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# Print the list using print()
print(mixed_data_types)
print(it_companies)
# Print the number of companies in the list
print(f'nro de ompañias:{len(it_companies)}')

# Print the first, middle and last company
print(f'primera:{it_companies[0]}, media:{it_companies[3]}, ultima:{it_companies[-1]}')

# Print the list after modifying one of the companies
it_companies[0] = 'IG'
print(it_companies)

# Add an IT company to it_companies
it_companies.append('Whatsapp') 
print(it_companies)

# Insert an IT company in the middle of the companies list
it_companies.insert(3,'youtube') 
print(it_companies)

# Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[1] = it_companies[1].upper()
print(it_companies)

# Join the it_companies with a string '#;  '

#it_companies = '#;  '.join(it_companies)
print(it_companies)

# Check if a certain company exists in the it_companies list.

existe_company = 'Oracle' in it_companies
print('Existe:',existe_company)

# Sort the list using sort() method
it_companies.sort()
print(it_companies)

# Reverse the list in descending order using reverse() method
it_companies.sort(reverse = True)
print(it_companies)

# Slice out the first 3 companies from the list
nuevalista = it_companies[:3]
print(nuevalista)

# Slice out the last 3 companies from the list
nuevalista = it_companies[-3:]
print(nuevalista)

# Slice out the middle IT company or companies from the list
nuevalista = it_companies[4:]
print(nuevalista)

# Remove the first IT company from the list
it_companies.pop(0)
print(it_companies)
# Remove the middle IT company or companies from the list
it_companies.pop(0)
print(it_companies)
# Remove the last IT company from the list
#it_companies.pop(-1)
del it_companies[-1]
print(it_companies)

# Remove all IT companies from the list
del it_companies
#print(it_companies)

# Destroy the IT companies list
#del it_companies

# Join the following lists:
#forma +
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

programadores = front_end + back_end
print(programadores)

#otra forma

front_end.extend(back_end)
print(front_end)

# After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. Then insert Python and SQL after Redux.
full_stack = front_end.copy()
print('full:',full_stack)

# Exercises: Level 2
# The following is a list of 10 students ages:
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list and find the min and max age
ages.sort()
min = ages[0]
max = ages[-1]
print('minimo: {}, maximo: {}'.format(min,max))

# Add the min age and the max age again to the list
print(ages)

# min = min(ages)
# max = max(ages)

ages.append(min)
ages.append(max)
print(ages)

# Find the median age (one middle item or two middle items divided by two)

# Find the average age (sum of all items divided by their number )
cantidad = len(ages)
print('cantidad:',cantidad)
suma = sum(ages)
print(f'promedio:{suma / cantidad}')

# Find the range of the ages (max minus min)
rango = max - min

# Compare the value of (min - average) and (max - average), use abs() method

# Find the middle country(ies) in the countries list
countries = ['Finland', 'Estonia', 'Denmark', 'Sweden', 'Norway']
mitad = int(len(countries) / 2)

print('pais a la mitad de la lista:',countries[mitad])

# Divide the countries list into two equal lists if it is even if not one more country for the first half.
primera = countries[:mitad+1]
segunda = countries[mitad+1:]
print('primera lista:',primera)
print('segunda lista:',segunda)

# ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.

paises = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
ch, ru,us, *res = paises
print(res)
