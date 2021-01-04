def square(num):
    '''
    This funtion is get square of passed number in parameter num
    :param num:  int
    :return:  int
    '''
    out = num ** 2
    print('in function')
    print(out)
    return out

def main():
    print('In main function')
   # square(number)

if __name__ == '__main__':
    number = 8
    main()
    result = square(number)
    print(f'result is {result}')
    print(type(result))