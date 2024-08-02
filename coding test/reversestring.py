#3. Write a Python program to reverse words in a string 

#String = “Deeptech Python Training”
def reverse_words(string):
    # Split the string into words
    words = string.split()
    # Reverse the list of words
    reversed_words = words[::-1]
    # Join the reversed words back into a string
    reversed_string = ' '.join(reversed_words)
    return reversed_string

# Given string
string = "Deeptech Python Training"

# Reverse the words in the string
reversed_string = reverse_words(string)

# Print the result
print(reversed_string)

#Output

#Training Python Deeptech
