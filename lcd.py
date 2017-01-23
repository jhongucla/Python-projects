from __future__ import print_function
import sys

def zero(s): # function draws the 0 digit
    output = [] # creates empty array and appends hyphens and vertical bars to draw digit
    output.append([' '] + ['-']*s + [' '])
    for x in range(s):
        output.append(['|'] + [' ']*s + ['|'])
    output.append([' ']*(s + 2))
    for x in range(s):
        output.append(['|'] + [' ']*s + ['|'])
    output.append([' '] + ['-']*s + [' '])
    return output

def one(s):
    output = []
    output.append([' ']*(s + 2))
    for x in range(s):
        output.append([' ']*(s + 1) + ['|'])
    output.append([' ']*(s + 2))
    for x in range(s):
        output.append([' ']*(s + 1) + ['|'])
    output.append([' ']*(s + 2))
    return output

def two(s):
    output = []
    output.append([' '] + ['-']*s + [' '])
    for x in range(s):
        output.append([' ']*(s + 1) + ['|'])
    output.append([' '] + ['-']*s + [' '])
    for x in range(s):
        output.append(['|'] + [' ']*(s + 1))
    output.append([' '] + ['-']*s + [' '])
    return output

def three(s):
    output = []
    output.append([' '] + ['-']*s + [' '])
    for x in range(s):
        output.append([' ']*(s + 1) + ['|'])
    output.append([' '] + ['-']*s + [' '])
    for x in range(s):
        output.append([' ']*(s + 1) + ['|'])
    output.append([' '] + ['-']*s + [' '])
    return output

def four(s):
    output = []
    output.append([' ']*(s + 2))
    for x in range(s):
        output.append(['|'] + [' ']*s + ['|'])
    output.append([' '] + ['-']*s + [' '])
    for x in range(s):
        output.append([' ']*(s + 1) + ['|'])
    output.append([' ']*(s + 2))
    return output

def five(s):
    output = []
    output.append([' '] + ['-']*s + [' '])
    for x in range(s):
        output.append(['|'] + [' ']*(s + 1))
    output.append([' '] + ['-']*s + [' '])
    for x in range(s):
        output.append([' ']*(s + 1) + ['|'])
    output.append([' '] + ['-']*s + [' '])
    return output

def six(s):
    output = []
    output.append([' '] + ['-']*s + [' '])
    for x in range(s):
        output.append(['|'] + [' ']*(s + 1))
    output.append([' '] + ['-']*s + [' '])
    for x in range(s):
        output.append(['|'] + [' ']*s + ['|'])
    output.append([' '] + ['-']*s + [' '])
    return output

def seven(s):
    output = []
    output.append([' '] + ['-']*s + [' '])
    for x in range(s):
        output.append([' ']*(s + 1) + ['|'])
    output.append([' ']*(s + 2))
    for x in range(s):
        output.append([' ']*(s + 1) + ['|'])
    output.append([' ']*(s + 2))
    return output

def eight(s):
    output = []
    output.append([' '] + ['-']*s + [' '])
    for x in range(s):
        output.append(['|'] + [' ']*s + ['|'])
    output.append([' '] + ['-']*s + [' '])
    for x in range(s):
        output.append(['|'] + [' ']*s + ['|'])
    output.append([' '] + ['-']*s + [' '])
    return output

def nine(s):
    output = []
    output.append([' '] + ['-']*s + [' '])
    for x in range(s):
        output.append(['|'] + [' ']*s + ['|'])
    output.append([' '] + ['-']*s + [' '])
    for x in range(s):
        output.append([' ']*(s + 1) + ['|'])
    output.append([' '] + ['-']*s + [' '])
    return output

for line in sys.stdin: # reads in a line from standard input
    s, n = line.split() # first number indicates size of digits, second is the number to draw
    s = int(s)
    if s == 0:
        quit()
    counter = 0
    display = []
    c = (s + 2)*len(n) + len(n) - 1
    r = s*2 + 3
    for num in n: # chooses the right function to write each digit
        digit = int(num)
        if digit == 0:
            number = zero(s)
        elif digit == 1:
            number = one(s)
        elif digit == 2:
            number = two(s)
        elif digit == 3:
            number = three(s)
        elif digit == 4:
            number = four(s)
        elif digit == 5:
            number = five(s)             
        elif digit == 6:
            number = six(s)             
        elif digit == 7:
            number = seven(s)             
        elif digit == 8:
            number = eight(s)            
        elif digit == 9:
            number = nine(s)
        if counter >= 1: # appends each drawn out digits to the array of digits
            for x in range(r):
                display[x].extend(number[x])
        else:
            for x in range(r):
                display.append(number[x])
        counter += 1
        for x in range(r):
            display[x].extend([' '])
    for x in range(r): # prints out the entire array of drawn out digits
        for y in range(c):
            print(display[x][y], end='')
        print()
    print()
