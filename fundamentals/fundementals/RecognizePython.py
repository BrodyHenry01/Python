num1 = 42 #variable declaration, Numbers
num2 = 2.3 #variable declaration, Numbers
boolean = True #variable declaration, Boolean
string = 'Hello World' #varibale declaration, String
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #varibale declaration, list, strings
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #varibale declaration, dictionary, strings, numbers
fruit = ('blueberry', 'strawberry', 'banana') #varibale declaration, tuple, strings
print(type(fruit)) #type check
print(pizza_toppings[1]) #length check, access value
pizza_toppings.append('Mushrooms') #log statement
print(person['name']) #access value log statment
person['name'] = 'George' #access value, change value, initialize
person['eye_color'] = 'blue' #access value, change value, initialize
print(fruit[2]) #length check, access value 

if num1 > 45:  #if, numbers, conditional
    print("It's greater") #log statement
else: #else,
    print("It's lower")#log statement

if len(string) < 5:# if, access value, conditional 
    print("It's a short word!")#log statement
elif len(string) > 15: #else if, access value, conditional
    print("It's a long word!")#log statement
else: #else
    print("Just right!")#log statement

for x in range(5): #  Length check, parameter, numbers for loop
    print(x)
for x in range(2,5): # Length check, parameter, numbers for loop
    print(x)
for x in range(2,10,3):# Length check, parameter, numbers for loop
    print(x)
x = 0 #variable declaration, numbers
while(x < 5):# while loop, numbers
    print(x)
    x += 1 #access value, add value, change value, increment

pizza_toppings.pop() #list
pizza_toppings.pop(1) #list, access value, delete value

print(person)
person.pop('eye_color') #access value, delete value
print(person)

for topping in pizza_toppings: #for loop, start, dictionary, access value
    if topping == 'Pepperoni': #conditional, access value, change value 
        continue #continue
    print('After 1st if statement') #string
    if topping == 'Olives': #conditional, access value, change value
        break #stop

def print_hello_ten_times(): #function
    for num in range(10): #for loop, length check, numbers
        print('Hello')#log statement

print_hello_ten_times()#function

def print_hello_x_times(x):
    for num in range(x):#for loop, length check,
        print('Hello') #log statement

print_hello_x_times(4) #function, parameter

def print_hello_x_or_ten_times(x = 10): #function
    for num in range(x):#for loop, length check,
        print('Hello')#log statement

print_hello_x_or_ten_times() #function
print_hello_x_or_ten_times(4) #function, parameter


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)