#to display the numbers between 10 to 500,divisible by both 10 and 7

print("to display the numbers between 10 to 500,divisible by both 10 and 7")
for x in range(10,500) :
    if(x%7==0 and x%10 ==0) :
        print(x)