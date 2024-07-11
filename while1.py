'''----#to count the numbers between 100 to 1000,
which is divisible by 13 and is even also'''


print("to count the numbers between 100 to 1000, which is divisible by 13 and is even also")
x=100
count =0
while (x<1000) :
    if (x%2==0 and x%3==0) :
        print(x, end=",")
        count += 1
    x=x+1
print("\n --------------------------")
print("Count of numbers is : ", count)
