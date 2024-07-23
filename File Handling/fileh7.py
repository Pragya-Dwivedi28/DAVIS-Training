txt_file=open("Myfile.txt","w")
txt_file.write("Welcome to Python")
	
txt_file = open("Myfile.txt", "r") 

	
vowel = 0
line = 0
consonants = 0

vowels_list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'] 

for alpha in txt_file.read():
    if alpha in vowels_list:
        vowel += 1
 
    elif alpha not in vowels_list and alpha != "\n":
        consonants += 1

 
print("Number of vowels in ","Myfile.txt" , " = ", vowel) 

print("Number of consonants in ", "Myfile.txt", " = ", consonants)  
txt_file.close()
