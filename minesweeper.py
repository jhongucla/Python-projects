from __future__ import print_function
import random

def nummine(solved, i, j): # counts the number of mines adjacent to the coordinates passed in
        count = 0
        for x in range(-1, 2):
                for y in range(-1, 2):
                        if not (x == 0 and y == 0):
                                if valid(solved, i + x, j + y):
                                        if solved[i + x][j + y] == '*':
                                                count += 1
        return count

def valid(solved, i, j): # checks if the coordinates are within the bounds of the array
        if i < 0 or j < 0:
                return False
        if i >= len(solved) or j >= len(solved[0]):
                return False
        return True        

def print_blank(blank, r, c): # prints the array passed in
        for x in range(r):
                for y in range(c):
                        print(blank[x][y], end='')
                print()
        print()

def check(solved, counter, bombs, bombs_hit, blank, mode, i, j, r, c):
        while True:
                while i > r or i <= 0 or j <= 0 or j > c: # checks for invalid input
                        i, j = map(int, raw_input('\nEnter valid row column\n').split())
                blank[i - 1][j - 1] = solved[i - 1][j - 1] # copies the coordinate from the solved array to the empty array
                if blank[i - 1][j - 1] == '*': # if the chosen coordinates are a bomb
                        print('\nYou have hit a bomb!\n')
                        counter -= 1
                        bombs_hit += 1
                        if mode == 'on':
                                print('You lost!')
                                break
                else:
                        print()
                print_blank(blank, r, c) # prints the array coordinates already played
                counter += 1
                if counter == (r*c) - bombs: # if there are no more bombs, the game is over
                        break
                i, j = map(int, raw_input('Which row column location to check?\n').split())
        return bombs_hit
        
def __main__():
        r, c = map(int, raw_input('To quit enter 0 0\nEnter field dimensions: rows columns\n').split())
        if r == 0 and c == 0:
            quit()
        bomb_num = int(raw_input('\nEnter bomb probability: most 1-5 fewest\n'))
        mode = raw_input('\nInstant death mode on or off?\n')
        tracker = 1
        while not (r == 0 and c == 0):
                solved = []
                blank = []
                bombs = 0
                for x in range(r): # randomly places bombs
                        line = []
                        for y in range(c):
                                line.append(random.choice('*' + '.'*bomb_num))
                        solved.append(line)
                for x, l in enumerate(solved): # calculates the numbers of bombs around each non-bomb coordinate
                        for y, e in enumerate(l):
                                if e != '*':
                                        solved[x][y] = nummine(solved, x, y)
                                else:
                                        bombs += 1
                print('\nField #' + str(tracker) + ':')
                for x in range(r):
                        blank.append(list('.'*c))
                print_blank(blank, r, c)
                i, j = map(int, raw_input('Which row column location to check?\n').split())
                counter = 0
                bombs_hit = 0
                bombs_hit = check(solved, counter, bombs, bombs_hit, blank, mode, i, j, r, c)
                if mode == 'off':
                        print('You are done!\nYou have hit', bombs_hit, 'bomb(s).')
                tracker += 1
                r, c = map(int, raw_input('\nTo quit enter 0 0\nEnter field dimensions: rows columns\n').split())
                if r == 0 and c == 0:
                        break
                bomb_num = int(raw_input('\nEnter bomb probability: most 1-5 fewest\n'))
                mode = raw_input('\nInstant death mode on or off?\n')

if __name__ == '__main__':
        __main__()
