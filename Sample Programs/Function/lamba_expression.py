def square(num):
    return num**2

my_nums = [1 ,2, 3, 4, 5]

for item in map(square, my_nums):
    print(item)

print(list(map(square,my_nums)))

def Slices(input):
    if len(input)%2 == 0:
        return 'Even'
    else:
        return input[0]

names = ['deepak','ankitaa','bony']

for item in map(Slices, names):
    print(item)

sum = lambda number : number + number

print(sum(13))

for item in map(sum, my_nums):
    print(item)
