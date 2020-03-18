#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


# return the nth triangle number
def triangle_number(n):
    return int(n * (n + 1) / 2)

# unit testing
assert triangle_number(1) == 1
assert triangle_number(2) == 3
assert triangle_number(3) == 6


# In[3]:


triangle_numbers = [triangle_number(n) for n in range(1, 31)]
triangle_numbers


# In[4]:


def alphabetical_value(ch):
    if ch.lower() not in 'abcdefghijklmnopqrstuvwxyz':
        return 0
    return 'abcdefghijklmnopqrstuvwxyz'.index(ch.lower()) + 1
# .index() returns the index of a char

def alpha_value_word(word):
    return sum([alphabetical_value(ch) for ch in word])

assert alpha_value_word('sky') == 55
assert alpha_value_word('ant') == 35


# In[5]:


# this is how we access the drive and pull in the list
words = open('/usr/share/dict/words').read().strip().split('\n')

df = pd.DataFrame({'word': words})
df['alpha_value'] = df.word.apply(alpha_value_word)
df['is_triangle_word'] = df.alpha_value.isin(triangle_numbers)
df


# In[6]:


df.alpha_value.max()


# In[7]:


df.is_triangle_word.sum()


# 

# In[ ]:





# In[ ]:




