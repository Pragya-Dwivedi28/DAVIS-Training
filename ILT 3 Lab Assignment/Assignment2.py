'''1. Write a Python program to count the occurrences of each word in a
given sentence
string = "To change the overall look of your document. To change the look
available in the gallery" '''

#to count no.of occurence of each word in the sentence

str = "To change the overall look your document. To change the look available in the gallery"
c = dict()
txt = str.split(" ")
for t in txt:
	if t in c:
		c[t] += 1
	else:
		c[t] = 1
print(c)


'''2. Write a Python program to remove a newline in Python
String = "\nBest \nDeeptech \nPython \nTraining\n" '''

# initialize list
test_list = ["\nBest \nDeeptech \nPython \nTraining\n"]

# printing original list
print("The original list : " + str(test_list))

# Removing newline character from string
# using loop
res = []
for sub in test_list:
	res.append(sub.replace("\n", ""))

# printing result
print("List after newline character removal : " + str(res))


'''3. Write a Python program to reverse words in a string
String = “Deeptech Python Training” '''


## initializing the string
string = "Deeptech Python Training"
print("the string is",string)
## splitting the string on space
words = string.split()
## reversing the words using reversed() function
words = list(reversed(words))
## joining the words and printing
a=(" ".join(words))
print("the reversed string is :",a)




'''4. Write a Python program to count and display the vowels of a given
text
String="Welcome to python Training" '''

String = "Welcome to python Training"
vowels = "aeiouAEIOU"  # Define a string containing all vowels
vowel_counts = {}      # Initialize an empty dictionary to store vowel counts
for char in String:
    if char in vowels:
        # If the character is a vowel, count it
        if char in vowel_counts:
            vowel_counts[char] += 1
        else:
            vowel_counts[char] = 1
print("Total number of vowels prsent in the given string :",vowel_counts)