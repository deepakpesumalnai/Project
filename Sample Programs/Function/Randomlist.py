
from random import shuffle


def shuffle_list(mylist):
    shuffle(mylist)
    return mylist

def player_guess():
    guess = ''
    while guess not in ['0','1','2']:
        guess = input("Pick a number : 0,1 or 2    ")
    return  int(guess)

def check_guess(mylist,guess):
    if mylist[guess] == 'O':
        print('Right guess')
    else:
        print('Wront Guess')
        print(mylist)

if __name__ == '__main__':
    example = [' ', 'O', ' ']
    myindex = player_guess()
    result = shuffle_list(example)
    check_guess(result,myindex)