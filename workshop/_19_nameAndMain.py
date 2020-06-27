# Creating Text File and Write Content

"""
File Modes in Python
Mode	Description
'r'	This is the default mode. It Opens file for reading.
'w'	This Mode Opens file for writing.
If file does not exist, it creates a new file.
If file exists it truncates the file.
'x'	Creates a new file. If file already exists, the operation fails.
'a'	Open file in append mode.
If file does not exist, it creates a new file.
't'	This is the default mode. It opens in text mode.
'b'	This opens in binary mode.
'+'	This will open a file for reading and writing (updating)
"""

fh = open("_19_SampleFile.txt","w")  # here w is write mode, it creates a file if its not present and will overwrite it
# fh = open("_19_SampleFile.txt","a")
fh.write("I am working on file handling in python, this is super smooth.")


for i in range(1, 11, 1):
    fh.write("{0} \n".format(i))
fh.close()


fh = open("_19_SampleFile.txt", "r")
# print(fh.read(3)) starting 3 characters

print(fh.read(20))
print(fh.readline())
print(fh.read())


fh.close()


