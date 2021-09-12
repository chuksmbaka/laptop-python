import os

filename = "listofnumbers.txt"
numberlist = [2, 3, 5, 6, 7, 9, 10]

file_object = open(filename, 'a+')
for number in numberlist:
    numtostr = str(number)
    file_object.write(numtostr)

os.mkdir("newdirectory")

