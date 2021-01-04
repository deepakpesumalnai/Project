def Check_even(number_list):

    for num in number_list:
        if num % 2 == 0:
            print(f'number {num} is even')
        else:
            print(f'number {num} is odd')

if __name__ == '__main__':
    numberlist = [2,3,4,5,6]
    Checkeven(numberlist)