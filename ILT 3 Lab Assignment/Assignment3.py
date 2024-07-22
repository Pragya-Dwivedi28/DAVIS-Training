'''1. Write a Python program to Count all letters, digits, and special
symbols from the given string
Input = “P@#yn26at^&i5ve”
Output: Chars = 8 Digits = 2 Symbol = 3'''

input_string=" “P@#yn26at^&i5ve” "
char_count = 0
digit_count = 0
symbol_count = 0

for char in input_string:   
    if char.isalpha():
        char_count += 1
    elif char.isdigit():
        digit_count += 1
    else:
        symbol_count += 1
print("Chars = ",char_count, "Digits =", digit_count, "Symbol =", symbol_count)




'''2. Write a Python program to remove duplicate characters of a given
string.
Input = “String and String Function”
Output: String and Function'''

def remove_dup_word(string):
    # Used to split string around spaces.
    words = string.split()
     
    # To store individual visited words
    hsh = set()
    # Traverse through all words
    for word in words:
        # If current word is not seen before.
        if word not in hsh:
            print(word, end=" ")
            hsh.add(word)
 
# Driver function
#the given string is\n String and String Function
if __name__ == '__main__':
    string = "String and String Function"
    remove_dup_word(string)



'''3. Write a Python program to count Uppercase, Lowercase, special
character and numeric values in a given string
Input = “Hell0 W0rld ! 123 * # welcome to pYtHoN”
Output:
UpperCase : 5
LowerCase : 18
NumberCase : 5
SpecialCase : 11'''

input_str= "Hell0 W0rld ! 123 * # welcome to pYtHoN"
uppercase_count=0
lowercase_count=0
digit_count=0
special_count=0
for char in input_str:
    if char.isupper():
        uppercase_count += 1
    elif char.islower():
        lowercase_count += 1
    elif char.isdigit():
        digit_count += 1
    else:
        special_count += 1

print("UpperCase = ",uppercase_count)
print("LowerCase = ",lowercase_count)
print("NumberCase = ",digit_count)
print("SpecialCase = ",special_count)




'''4. Write a Python Count vowels in a string
input= “Welcome to Python Assignment”
Output: Total vowels are: 8'''

input_string="Welcome to Python Assignment"
vowels = "aeiouAEIOU"
vowel_count = 0
for char in input_string:
    if char in vowels:
        vowel_count += 1    
print("Total vowels are:",vowel_count)


