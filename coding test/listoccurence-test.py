Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #Write a Python function to count the occurrences of a specific element in a list.
>>> lis = ['a', 'd', 'd', 'c', 'a', 'b', 'b', 'a', 'c', 'd', 'e']
>>> occurrence = {item: lis.count(item) for item in lis}
>>> print(occurrence.get('d'))
3
