Samplelist = [1, 2, 'a', 'b', 99]
print('1st: ', Samplelist)
print('2nd: ', Samplelist[2])
print('3rd: ', Samplelist[2:9])
print('4th: ', Samplelist[0:2])
print('5th: ', Samplelist[2:0])
print('6th: ', Samplelist[-1:2])
print('7th: ', Samplelist[-2])
print('8th: ', Samplelist[1:])
print(Samplelist)
print('pop - Remove based on index', Samplelist.pop(2))
print(Samplelist)
print('Append ', Samplelist.append(45))
print(Samplelist)
print('Remove - Remove based on value ', Samplelist.remove(2))
print(Samplelist)

newlist = Samplelist

print('Appen other list', newlist.append('a'))
print(newlist)
print(Samplelist)

print(id(newlist))
print(id(Samplelist))

secondlist = newlist[:]
print('Append other list', secondlist.append('a'))

print(secondlist)
print(newlist)
print(id(secondlist))
print(id(newlist))

statement = 'Hi how are, you doing?'
print(statement.split(','))