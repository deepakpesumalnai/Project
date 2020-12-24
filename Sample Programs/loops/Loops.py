for i in range(0, 9):
    print(i)
Simplelist = []
Samplelist = []
for i in range(0, 5):
    print(i)
    for j in range(3, 5):
        print('j :', j)
        if i * j > 10:
            Simplelist.append(i * j)
print(Simplelist)

Samplelist = [i * j > 10 for i in range(0, 5) for j in range(3, 5)]
print(Samplelist)

while i < 51:
    print(i)
    i = i + 10
