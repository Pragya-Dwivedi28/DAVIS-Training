#To count the numbers between 100 to 1000 which is even and divisible by 3
count=0
for x in range(100,1000) :
    if(x%2==0 and x%3==0) :
        print(x, ",",end="")
        count=count+1

print("\n -------------------------------------")
print("\n The count of numbers between 100 and 1000 which is even and also divisible by 3 :",count)      

        

