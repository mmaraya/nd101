#!/usr/bin/env python

import collections

def bag_of_words(text):
    return collections.Counter(text.split(' '))

test_text = 'the quick brown fox jumps over the lazy dog'

print(bag_of_words(test_text))
