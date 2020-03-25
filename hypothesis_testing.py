#!/usr/bin/env python
# coding: utf-8

# In[1]:


from math import sqrt

get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

from scipy import stats

from pydataset import data


# ## For each of the following questions, formulate a null and alternative hypothesis (be as specific as you can be), then give an example of what a true positive, true negative, type I and type II errors would look like. Note that some of the questions are intentionally phrased in a vague way. It is your job to reword these as more precise questions that could be tested.

# Has the network latency gone up since we switched internet service providers?

# - Ho: Switching internet providers has no effect on network latency
# - Ha: Switching internet providers has increased network latency

# Is the website redesign any good?

# - Ho: The redesign has not improved the website
# + Ha: The redesign has imporved the website

# Is our television ad driving more sales?

# - Ho: The television ads have had no effect on sales
# - Ha: The television ads have increased sales

# In[2]:


alpha = .05
# office 1:  40 sales, mean od 90 days, standard deviation of 15 days
n1 = 40
xbar1 = 90
sd1 = 15

# office 2: 50 sales, mean of 100 days, standard deviation of 20 days
n2 = 50
xbar2 = 100
sd2 = 20

degf = (n1 + n2) -2

sp = sqrt(
    ((n1 - 1) * sd1**2 + (n2 - 1) * sd2**2)
    /
    degf
)


# In[3]:


t = (xbar1 - xbar2) / (sp * sqrt(1 / n1 + 1 / n2))
p = stats.t(degf).cdf(t) * 2
print(f't: {t:.4f}')
print(f'p: {p:.4f}')


# In[4]:


print(f'''
Because p ({p:.6f}) < alpha ({alpha}), we reject the null hypothesis:
that there is no difference in the average sales time between the two offices.

in plain english: we think there is a diffference in sales time between the two offices
''')


# ###### Load the mpg dataset and use it to answer the following questions:

# In[5]:


mpg = data('mpg')
mpg.head(10)


# Is there a difference in fuel-efficiency in cars from 2008 vs 1999?

# - *Ho:* There is no difference in fuel-efficiency between 2008 and 1999 cars
# - *Ha:* There is a difference in fuel-efficiency between 2008 and 1999 cars

# In[6]:


x1 = mpg[mpg.year == 1999].hwy
x2 = mpg[mpg.year == 2008].hwy

t, p = stats.ttest_ind(x1, x2)
print('p = ', p)


# In[7]:


print(f'''
Because p ({p:.12f}) > alpha {alpha}, we fail to reject the null hypothisis that
there is no difference in ful-efficiency between 2008 and 1999 cars
''')


# Are compact cars more fuel-efficient than the average car?

# - *Ho:* There is no difference in fuel-efficiency between compact cars and the other types
# - *Ha:* There is a difference in fuel-efficiency between compact cars and the other types

# In[8]:


x = mpg[mpg['class'] == 'compact'].hwy
mu = mpg.hwy.mean()

t, p = stats.ttest_1samp(x, mu)


# In[9]:


print(f'''
Because p ({p:.12f}) < alpha {alpha}, we reject the null hypothisis that
there is no difference in ful-efficiency between compact cars and the 
rest of the car type
''')


# Do manual cars get better gas mileage than automatic cars?

# - *Ho*: there is no difference in gas consumption between automatic and manual 
# - *Ha*: there is a difference in gas consumption between automatic and manual

# In[10]:


is_automatic_trsnsmission = mpg.trans.str.startswith('auto')

x1 = mpg[is_automatic_trsnsmission].hwy
x2 = mpg[~is_automatic_trsnsmission].hwy

t, p = stats.ttest_ind(x1, x2)
print('t= ', t)
print('p= ', p)


# In[11]:


print(f'''
Because p ({p:.5f}) < alpha {alpha}, we reject the null hypothesis the there
is no difference is gas consumption between automatic and manual
''')


# In[12]:


plt.hist([x1, x2])
plt.legend()


# In[ ]:





# In[ ]:




