
import os.path
from os import path
print("is file present: " + str( path.isfile('C:\\Users\\deepak\\github\\Project1\\Sample Programs\\File\\sample.txt.txt')))
myfile = open('C:\\Users\\deepak\\github\\Project1\\Sample Programs\\File\\sample.txt.txt','r')
#temp = myfile.read()

test = myfile.readline()
myfile.seek(0)
print(str(myfile.readline()))
print(str(myfile.readline()))
myfile.seek(0)
print(str(myfile.read()))
#print(temp)
print(test)
myfile.seek(0)
print(str(myfile.readlines()))

myfile.seek(0)
print(str(myfile.readlines()[2]))
myfile.close()


with open('C:\\Users\\deepak\\github\\Project1\\Sample Programs\\File\\sample.txt.txt','r') as myfile:
    content = myfile.read()

print(content)

with open('C:\\Users\\deepak\\github\\Project1\\Sample Programs\\File\\sample.txt.txt',mode='w' ) as mywrite:
    content = mywrite.read()
