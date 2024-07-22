'''1. Declare a div() function with two parameters. Then call the function and pass two
numbers and display their division.'''

# Define the div function
def div(a, b):
    return a / b

# Call the div function with two numbers
result = div(10, 2)

# Display the result
print("Division result:", result)



'''Declare a square() function with one parameter.Then call the function and pass
one number and display the square of that number .'''

def square(a):
    d=(a*a)
    print("the numbers is",a)
    print("the square of number is",d)

(square(4))

'''3. Using max() and min() functions display the maximum and minimum of 5 random
numbers. '''

import random
for random_number in range(0,5):
    random_number = random.randint(1, 20)
    lis1=[random_number]
    print(lis1)
    
print("the maximum of random numbers is",max(lis1))
print("the minimum of random numbers is",min(lis1))

'''4. Accept a name from the user and display that in lower case using lower()
function.'''

str = "Hell0 W0rld ! 123 * # welcome to pYtHoN"
print("Original strings : ",str)
upr, lwr, num, spl = 0, 0, 0, 0
for i in range(len(str)):
	if str[i] >= 'A' and str[i] <= 'Z':
		upr += 1
	elif str[i] >= 'a' and str[i] <= 'z':
		lwr += 1
	elif str[i] >= '0' and str[i] <= '9':
		num += 1
	else:
		spl += 1
 
print("UpperCase : ",upr)
print("LowerCase : ",lwr)
print("NumberCase : ",num)
print("SpecialCase : ",spl)