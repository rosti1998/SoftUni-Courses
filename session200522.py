# exercise 1
name = input()

if name == "Johnny":
    print('Hello, my love!')
else:
    print(f'Hello, {name}!')

# exercise 2
age = int(input())

if age <= 14:
    print('drink toddy')
elif age <= 18:
    print('drink coke')
elif age <= 21:
    print('drink beer')
else:
    print('drink whisky')

# exercise 3
n = int(input())

for i in range(n):
    number = int(input())
    if number == 88:
        print('Hello')
    elif number == 86:
        print('How are you?')
    elif number < 88:
        print('GREAT!')
    else:
        print('Bye.')

# exercise 4
n1 = int(input())
n2 = int(input())

while True:
    if n2 % n1 == 0:
        print(n2)
        break
    else:
        n2 -= 1

# exercise 5
number_of_orders = int(input())
total = 0

for i in range(0, number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())
    if price_per_capsule < 0.01 or price_per_capsule > 100:
        continue
    elif days < 1 or days > 31:
        continue
    elif capsules_per_day < 1 or capsules_per_day > 2000:
        continue
    price = price_per_capsule * days * capsules_per_day
    total += price
    print(f'The price for the coffee is: ${price:.2f}')


print(f'Total: ${total:.2f}')


# exercise 6
number_of_strings = int(input())
count = 0
pure = True

while count < number_of_strings:
    string = input()
    for i in range(0, len(string)):
        if string[i] == ',' or string[i] == '.' or string[i] == '_':
            print(f'{string} is not pure!')
            pure = False
            break
    if pure is False:
        pure = True
    else:
        print(f'{string} is pure.')
    count += 1

# exercise 7
while True:
    command = input()
    if command == 'SoftUni':
        continue
    if command == "End":
        break
    for i in range(0, len(command)):
        if i == len(command) - 1:
            print(command[i] * 2)
        else:
            print(command[i] * 2, end='')

# exercise 8
coffees = 0

while True:
    command = input()
    if command == 'END':
        break
    elif command == 'coding' or command == 'dog' or command == 'cat' or command == 'movie':
        coffees += 1
    elif command == 'CODING' or command == 'DOG' or command == 'CAT' or command == 'MOVIE':
        coffees += 2

if coffees <= 5:
    print(coffees)
else:
    print('You need extra sleep')

# exercise 9

while True:
    name = input()
    if name == 'Voldemort':
        print('You must not speak of that name!')
        break
    elif name == 'Welcome!':
        print('Welcome to Hogwarts.')
        break
    elif len(name) < 5:
        print(f'{name} goes to Gryffindor.')
    elif len(name) == 5:
        print(f'{name} goes to Slytherin.')
    elif len(name) == 6:
        print(f'{name} goes to Ravenclaw.')
    elif len(name) > 6:
        print(f'{name} goes to Hufflepuff.')

# exercise 10
str1 = input()
str2 = input()
copy = str2


for i in range(0, len(str1)):
    if str1[i] != str2[i]:
        str1_list = list(str1)
        str1_list[i] = str2[i]
        str11 = "".join(str1_list)
        str1 = str11
        print(str1)

# exercise 11
budget = float(input())
kg_flour = float(input())
egg_price = kg_flour * 0.75
milk_needed = kg_flour * 1.25 / 4
total_for_1loaf = kg_flour + egg_price + milk_needed
loafs = 0
eggs = 0

while budget > total_for_1loaf:
    budget -= total_for_1loaf
    loafs += 1
    eggs += 3
    if loafs % 3 == 0:
        eggs -= loafs - 2

print(f'You made {loafs} loaves of Easter bread! Now you have {eggs} eggs and {budget:.2f}BGN left.')
