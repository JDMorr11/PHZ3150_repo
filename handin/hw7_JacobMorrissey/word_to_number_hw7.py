#!/usr/bin/env python
# coding: utf-8

# In[10]:


def word_to_number(word):
    """Input a word for a number between one and twenty. Outputs the integer. \n Example \n Input: two \n Output: 2"""
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen', 'twenty']
    number_dict = {}
    for i in range(len(words)):
        number_dict[ words[i] ]=i
    if word in words:
        number = number_dict[ word ]
    else:
        print('not a number between one and twenty')
    return number

