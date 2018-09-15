#!/usr/bin/env python

import sys
import re
import string

for lines in sys.stdin:
    lines = lines.lower()
    # removing excessive whitespace
    lines = lines.split("\n")
    # strip punctuation marks
    lines = [re.sub(r'[^A-Za-z0-9]+', ' ', each_line) for each_line in lines]
    # set the counter for each line
    for each_line in lines:
        if "chicago" in each_line:
            print('%s %d'%('Chicago' , 1))
        else:
            print('%s %d'%('Chicago' , 0))
    for each_line in lines:
        if "dec" in each_line:
            print('%s %d'%('Dec' , 1))
        else:
            print('%s %d'%('Dec' , 0))
    for each_line in lines:
         if "java" in each_line:
            print('%s %d'%('Java' , 1))
         else:
            print('%s %d'%('Java' , 0))
    for each_line in lines:
         if "hackathon" in each_line:
            print('%s %d'%('hackathon' , 1))
         else:
            print('%s %d'%('hackathon' , 0))
