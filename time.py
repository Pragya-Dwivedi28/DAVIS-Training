sec = int(input("Enter time in seconds :"))

if(sec >= 0) :
    hours = 0
    mins = 0

    if(sec >= 3600) :
        hours = sec//3600
        sec = sec%3600

    if(sec >= 60) :
        mins = sec//60
        sec = sec%60
    
    print(hours,"Hours", mins, "Minutes", sec, "Seconds")

else :
    print("time must be positive")