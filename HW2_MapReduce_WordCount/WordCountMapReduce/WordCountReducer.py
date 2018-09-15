
# coding: utf-8

# In[1]:

#!/usr/bin/env python

import sys
from operator import itemgetter

# mapping word to counts
word_to_count = {}

for lines in sys.stdin:
    # removing excessive whitespace
    lines = lines.strip()
    # extract the result from WordCountMapper.py
    word , count = lines.split(' ', 1)

    try:
        count = int(count)
        word_to_count[word] = word_to_count.get(word , 0) + count
    except ValueError:
        pass

#sorted the result of MapReduce
sorted_word_to_count = sorted(word_to_count.items(), key=itemgetter(0))


for word , summing in sorted_word_to_count:
    print('%s %d' % (word , summing))

