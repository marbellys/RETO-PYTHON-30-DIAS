# Ing. Marbellys Campos

# Exercises: Day 6
# Exercises: Level 1
# Create an empty tuple
t = tuple()
print(t)

#otra forma
t = ()
print(t)

# Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
sisters = ('Maury','Derbi','Maiquelis','Mariflor')
brothers = ('Fari','Gui')
print(brothers,sisters)

# Join brothers and sisters tuples and assign it to siblings
siblings = sisters + brothers
print(siblings)

# How many siblings do you have?
total = len(siblings)
print(total)

# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
parents = ('margarita' , 'lino')
family_members = siblings + parents
print(family_members)

# Exercises: Level 2
# Unpack siblings and parents from family_members
siblings = family_members[:6]
parents = family_members[-2:]
print(siblings)
print(parents)

# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('banana','pera','manzana')
vegetables = ('lechuga','zanahoria') 
animales = ('vaca','conejo','pescado')

food_stuff_tp = fruits + vegetables + animales
print(food_stuff_tp)

# Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)

# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
middle = food_stuff_tp[3:5]
print(middle)

# Slice out the first three items and the last three items from food_staff_lt list
first_three = food_stuff_lt[:3]

last_three = food_stuff_lt[-3:]
print(first_three)
print(last_three)

# Delete the food_staff_tp tuple completely

#del food_stuff_tp
print(food_stuff_tp)

# Check if an item exists in tuple:
existe = 'pera' in food_stuff_tp
print(existe)

# Check if 'Estonia' is a nordic country
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
es = 'Estonia' in nordic_countries
print(es)

# Check if 'Iceland' is a nordic country
es = 'Iceland' in nordic_countries
print(es)
