Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Write a Python function to count the occurrences of a specific element in a list.
#create function with parameter
#The list in which to count occurrences
#The element to count in the list
def count_occurrences(list, element):
    count = 0

#for loop for iteration    
    for item in list:

#check if item is equal to element        
        if item == element:
            count += 1
    return count

#list
my_list = [1, 4, 3, 2, 4, 6, 5]

#count 4
element_to_count = 4

#function call
occurrences = count_occurrences(my_list, element_to_count)
print(f"The element {element_to_count} occurs {occurrences} times in the list."
