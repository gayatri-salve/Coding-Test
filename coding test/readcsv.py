#Write a python program to read a csv file and display its contents.

import csv

#path to your csv file
csv_path=r"C:\Users\Gayatri Salve\Dropbox\PC\Desktop\python coding\Book.csv"

#open file csv
file=open(csv_path,mode='r')

#Create a CSV reader object
csv_reader=csv.reader(file)

#read and display each row in csv file
for row in csv_reader:
    print(row)


#close the file
 file.close()
 
