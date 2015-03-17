#!/usr/bin/python
'''
MEGA USEFUL GENERAL PURPOSE STUFF
'''

def strip(character, string):
    ''' strip a character from a string'''
    new_string = ""
    for s in string:
        if s != character:
            new_string += s
    return new_string
