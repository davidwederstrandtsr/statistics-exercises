#!/usr/bin/env python
# coding: utf-8

# In[9]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import pandas as pd


# In[ ]:





# **1.** How likely is it that you roll doubles when rolling two dice?

# In[18]:


def is_double(two_dice):
    return two_dice[0] == two_dice[1]

assert is_double([2,4]) == False
assert is_double([5,5]) == True


# In[21]:


two_dice = np.random.choice([1, 2, 3, 4, 5, 6], size=(10_000, 2))
two_dice


# In[27]:


two_dice = pd.DataFrame(two_dice)
doubled = two_dice.apply(is_double, axis=1)
doubled.mean()


# **2.** If you flip 8 coins, what is the probability of getting exactly 3 heads? What is the probability of getting more than 3 heads?

# In[43]:


# 1. represent our data -- 0 is tails, 1 is heads
# 2. create a matrix (nrows, ncols)

flips = np.random.choice([0,1], size=(10_000, 8))
flips


# In[53]:


num_heads = flips.sum(axis=1)
(num_heads == 3).mean()


# In[54]:


(num_heads > 3).mean()


# **3.** There are approximitely 3 web development cohorts for every 1 data science cohort at Codeup. 
# 
# - Assuming that Codeup randomly selects an alumni to put on a billboard, what are the odds that the two billboards I drive past both have data science students on them?

# In[58]:


# 
billboard = np.random.choice([0,1], p=[.75, .25], size=(10_000, 2))
billboard


# In[60]:


billboard_count = billboard.sum(axis=1)
billboard_count


# In[61]:


(billboard_count == 2).mean()


# **4.** Codeup students buy, on average, 3 poptart packages (+- 1.5) a day from the snack vending machine. 
# - If on monday the machine is restocked with 17 poptart packages, how likely is it that I will be able to buy some poptarts on Friday afternoon?

# In[ ]:





# **5.** Compare Heights
# 
# - Men have an average height of 178 cm and standard deviation of 8cm.
# - Women have a mean of 170, sd = 6cm.
# - If a man and woman are chosen at random, P(woman taller than man)?

# In[ ]:





# **6.** When installing anaconda on a student's computer, there's a 1 in 250 chance that the download is corrupted and the installation fails. 

# - What are the odds that after having 50 students download anaconda, no one has an installation issue? 100 students?

# In[ ]:





# - What is the probability that we observe an installation issue within the first 150 students that download anaconda?

# In[ ]:





# - How likely is it that 450 students all download anaconda without an issue?

# In[ ]:





# **7.** There's a 70% chance on any given day that there will be at least one food truck at Travis Park. 
# - However, you haven't seen a food truck there in 3 days. How unlikely is this?

# In[ ]:





# - How likely is it that a food truck will show up sometime this week?

# In[ ]:





# **8.** If 23 people are in the same room, what are the odds that two of them share a birthday? same month and day

# In[ ]:





# - What if it's 20 people? 

# In[ ]:





# - 40?

# In[ ]:




