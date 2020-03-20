#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import pandas as pd

np.random.seed(42)


# **Exercise 1.** How likely is it that you roll doubles when rolling two dice?

# In[2]:


rolls = np.random.choice([1, 2, 3, 4, 5, 6], size=(2, 100_000))
rolls


# In[3]:


rolls[0].size


# In[4]:


die1 = rolls[0]
die2 = rolls[1]


# In[5]:


print(die1[1])
print(die2[1])


# In[6]:


(die1 == die2).mean()


# In[7]:


rolls = rolls.T
df = pd.DataFrame(rolls)
df.head(10)


# In[8]:


df["doubles"] = df[0] == df[1]
df.doubles.mean()


# In[9]:


df


# **Exercise 2.** If you flip 8 coins, what is the probability of getting exactly 3 heads? What is the probability of getting more than 3 heads?

# In[10]:


# 1. represent our data -- 0 is tails, 1 is heads
# 2. create a matrix (nrows, ncols)
# n_coins = 8
# n_simulations = 100_000
# flips = np.random.choice([0, 1], n_simulations * n_coins).reshape(n_simulations, n_coins)
flips = np.random.choice([0,1], size=(100_000, 8))
flips


# In[11]:


num_heads = flips.sum(axis=1)
(num_heads == 3).mean()


# - getting more then 3 heads

# In[12]:


(num_heads > 3).mean()


# **Exercise 3.** There are approximitely 3 web development cohorts for every 1 data science cohort at Codeup. 
# 
# - Assuming that Codeup randomly selects an alumni to put on a billboard, what are the odds that the two billboards I drive past both have data science students on them?

# In[13]:


# 
billboard = np.random.choice([0,1], p=[.75, .25], size=(10_000, 2))
billboard


# In[14]:


billboard_count = billboard.sum(axis=1)
billboard_count


# In[15]:


(billboard_count == 2).mean()


# **Exercise 4.** Codeup students buy, on average, 3 poptart packages (+- 1.5) a day from the snack vending machine. 
# - If on monday the machine is restocked with 17 poptart packages, how likely is it that I will be able to buy some poptarts on Friday afternoon?

# In[16]:


poptarts = np.round(np.random.normal(3, 1.5, size=(100_000, 5)))


# In[17]:


(poptarts.sum(axis=1) < 17).mean()


# **Exercise 5.** Compare Heights
# 
# - Men have an average height of 178 cm and standard deviation of 8cm.
# - Women have a mean of 170, sd = 6cm.
# - If a man and woman are chosen at random, P(woman taller than man)?

# In[18]:


men = np.random.normal(178, 8, size=10_000)
women = np.random.normal(170, 6, size=10_000)
df = pd.DataFrame({'men': men, 'women': women})
(df.men < df.women).mean()


# **Exercise 6.** When installing anaconda on a student's computer, there's a 1 in 250 chance that the download is corrupted and the installation fails. 

# In[19]:


# function that returns the succcess percentage
def no_failures(trials):
    installs = np.random.choice([1, 0], p=[1/250, 249/250], size=(10_000,trials))
    return (installs.sum(axis=1) == 0).mean()


# - What are the odds that after having 50 students download anaconda, no one has an installation issue? 

# In[20]:


no_failures(50)


# - 100 students?

# In[21]:


no_failures(100)


# - What is the probability that we observe an installation issue within the first 150 students that download anaconda?

# In[22]:


1 - no_failures(150)


# - How likely is it that 450 students all download anaconda without an issue?

# In[23]:


no_failures(450)


# **Exercise 7.** There's a 70% chance on any given day that there will be at least one food truck at Travis Park. 

# In[24]:


trucks = np.random.choice([1, 0], p=[.7, .3], size=(100_000, 3))
df = pd.DataFrame(trucks)
df.columns = ["day_1", "day_2", "day_3"]
df


# - However, you haven't seen a food truck there in 3 days. How unlikely is this?

# In[25]:


df["present"] = df.day_1 + df.day_2 + df.day_3
(df.present == 0).mean()


# - How likely is it that a food truck will show up sometime this week?

# In[26]:


trucks = np.random.choice([1, 0], p=[.7, .3], size=(100_000, 7))
df = pd.DataFrame(trucks)
df


# In[27]:


df["present"] = df.sum(axis=1)
df.head()


# In[28]:


(df.present > 0).mean()


# **Exercise 8.** If 23 people are in the same room, 

# In[29]:


n_sims = 100_000
n_people = 23
birthdays = np.random.choice(range(365), size=(n_sims, n_people))
df = pd.DataFrame(birthdays)
df  


# In[30]:


df["n_unique"] = df.nunique(axis=1)
df.head(3)


# - what are the odds that two of them share a birthday? 
# 
# + same month and day

# In[32]:


(df.n_unique == n_people - 1).mean()


# - What if it's 20 people? 

# In[33]:


n_people = 20
birthdays = np.random.choice(range(365), size=(n_sims, n_people))
df = pd.DataFrame(birthdays)
df  


# In[34]:


df["n_unique"] = df.nunique(axis=1)
df.head(3)


# In[35]:


(df.n_unique == n_people - 1).mean()


# - 40?

# In[36]:


n_people = 40
birthdays = np.random.choice(range(365), size=(n_sims, n_people))
df = pd.DataFrame(birthdays)
df  


# In[37]:


df["n_unique"] = df.nunique(axis=1)
df.head(3)


# In[38]:


(df.n_unique == n_people - 1).mean()

