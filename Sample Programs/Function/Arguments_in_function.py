
def Local_print(*args):
     for item in args:
        print(item)


def Local_key_print(**kargs):
     for item in kargs.values():
        print(item)


def Local_both_print(*args, **kargs):
    print(args)
    print(kargs)
    for item in kargs.values():
        print(item)
    return  args.count()

if __name__ == '__main__':
    Local_print(1, 2, 3,'3' , 4)
    Local_key_print(fruit='apple', game='a')
    Local_both_print(1, 2, 3,'3' , 4,fruit='apple', game='a')
