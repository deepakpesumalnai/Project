def check_even(num):
    if num%2 == 0:
        return True
    else:
        return False


mynums = [1, 2, 3, 4, 5, 6]

for item in map(check_even, mynums):
    print(item)

for item in filter(check_even, mynums):
    print(item)

print(list(filter(check_even, mynums)))