Sampletupple = (1, 2, 'a', 'b', 99)
print('1st: ', Sampletupple)
print('2nd: ', Sampletupple[2])
print('3rd: ', Sampletupple[2:9])
print('4th: ', Sampletupple[0:2])
print('5th: ', Sampletupple[2:0])
print('6th: ', Sampletupple[-1:2])
print('7th: ', Sampletupple[-2])
print('8th: ', Sampletupple[1:])
print(Sampletupple)
# print('pop - Remove based on index', Sampletupple.pop(2))
print(Sampletupple)
#print('Append ', Sampletupple.append(45))
print(Sampletupple)
#print('Remove - Remove based on value ', Sampletupple.remove(2))
print(Sampletupple)

newtupple = Sampletupple

#print('Appen other tupple', newtupple.append('a'))
print(newtupple)
print(Sampletupple)

print(id(newtupple))
print(id(Sampletupple))

secondtupple = newtupple[:]
#print('Append other tupple', secondtupple.append('a'))

print(secondtupple)
print(newtupple)
print(id(secondtupple))
print(id(newtupple))

statement = 'Hi how are, you doing?'
print(statement.split(','))
