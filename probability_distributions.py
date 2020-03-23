#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
import pandas as pd

np.random.seed(123)


# **Exercise 1** 
# - A bank found that the average number of cars waiting during the noon hour at a drive-up window follows a Poisson distribution with a mean of 2 cars. Make a chart of this distribution and answer these questions concerning the probability of cars waiting at the drive-up window.

# - What is the probability that no cars drive up in the noon hour?

# In[38]:


x = range(0, 10)
y = stats.poisson(2).pmf(x)
per_hour = 2


# In[39]:


plt.bar(x, y)
plt.title("Probabilty of seeing x number of cars.\n")
plt.ylabel("Probabilty")
plt.xlabel("Number of cars")
plt.show()


# - What is the probability that 3 or more cars come through the drive through?

# In[41]:


theory = stats.poisson(2).sf(2)

# from exercise walkthrough
simulated = (stats.poisson(per_hour).rvs(10_000) >= 3).mean()

theory, simulated


# - How likely is it that the drive through gets at least 1 car?

# In[5]:


stats.poisson(2).sf(0)


# **Exercise 2**
# - Grades of State University graduates are normally distributed with a mean of 3.0 and a standard deviation of .3. Calculate the following:

# In[6]:


μ = 3.0
σ = .3

grades = stats.norm(μ, σ)


# - What grade point average is required to be in the top 5% of the graduating class?

# In[45]:


top_5_percent_grade_avg = grades.isf(.05)
print('The top 5% grade point average is {:.3f}'.format(top_5_percent_grade_avg))


# - What GPA constitutes the bottom 15% of the class?

# In[46]:


bottom_15_percent_grade_avg = grades.ppf(.15)
print('The bottom 15% grade point average is {:.3f}'.format(bottom_15_percent_grade_avg))


# - An eccentric alumnus left scholarship money for students in the third decile from the bottom of their class. Determine the range of the third decile. Would a student with a 2.8 grade point average qualify for this scholarship?

# In[50]:


gpa = 2.8
third_decile_low = grades.ppf(.2)
third_decile_high = grades.ppf(.3)

does_qualify = third_decile_low < gpa and gpa < third_decile_high
does_qualify


# - If I have a GPA of 3.5, what percentile am I in?

# In[10]:


gpa_to_percentile = grades.cdf(3.5)
gpa_to_percentile


# ### Exercise 3
# A marketing website has an average click-through rate of **2%**. One day they observe **4326** visitors and **97** click-throughs. 
# - How likely is it that this many people or more click through?
# 

# In[54]:


click_distro = stats.binom(4326, .02)

theory = click_distro.sf(96)
theory


# ### Exercise 4
# You are working on some statistics homework consisting of **100** questions where all of the answers are a probability rounded to the hundreths place. Looking to save time, you put down random probabilities as the answer to each question.
# - What is the probability that at least one of your first **60** answers is correct?

# In[57]:


n = 60
p =.01
theory = stats.binom(n, p).sf(0)

simulation = (stats.binom(n, p).rvs(10_000) > 0).mean()
theory, simulation


# ### Exercise 5
# The codeup staff tends to get upset when the student break area is not cleaned up. Suppose that there's a **3%** chance that any one student cleans the break area when they visit it, and, on any given day, about **90%** of the **3** active cohorts of **22** students visit the break area. 
# - How likely is it that the break area gets cleaned up each day?

# In[59]:


# 90% of the three cohorts
n = round(3 * 22 * .90)
p = .03


# In[61]:


theory = stats.binom(n, p).sf(0)
theory


#  - How likely is it that it goes two days without getting cleaned up? 

# In[64]:


not_clean_p = 1 - theory
stats.binom(2,not_clean_p).sf(1)


# - All week?

# In[65]:


not_clean_p = 1 - theory
stats.binom(5,not_clean_p).sf(4)


# ### Exercise 6
# You want to get lunch at La Panaderia, but notice that the line is usually very long at lunchtime. After several weeks of careful observation, you notice that the average number of people in line when your lunch break starts is normally distributed with a mean of **15** and standard deviation of **3**. If it takes **2** minutes for each person to order, and **10** minutes from ordering to getting your food. Assume you have one hour for lunch, and ignore travel time to and from La Panaderia.
# - what is the likelihood that you have at least **15** minutes left to eat your food before you have to go back to class? 

# 

# In[17]:


μ = 15
σ = 3

target = 15

line_time = stats.norm(μ, σ)
line_time.sf(target)


# ### Exercise 7 **I did not get this, the worki is from the walkthrough**
# Connect to the employees database and find the average salary of current employees, along with the standard deviation. Model the distribution of employees salaries with a normal distribution and answer the following questions:

# In[70]:


from env import host, user, password
db_name = "employees"
url = f'mysql+pymysql://{user}:{password}@{host}/employees'
query2 = """
    select emp_no, salary from salaries 
    join dept_emp using(emp_no)
    where salaries.to_date > curdate() 
    and dept_emp.to_date > curdate()
    """

#pd.read_sql('SHOW TABLES', url)


# In[71]:


df = pd.read_sql(query2, url)
salaries = df.set_index("emp_no")


# In[73]:


avg = salaries.mean()["salary"]
stdev = salaries.std()["salary"]
avg, stdev


# In[75]:


(salaries == 60_000).mean()


# **a.** What percent of employees earn less than 60,000?

# In[80]:


theory = stats.norm(avg, stdev).cdf(59_999)
actual = (salaries < 60_000).mean()["salary"]
theory, actual


# **b.** What percent of employees earn more than 95,000?
# 

# In[79]:


theory = stats.norm(avg, stdev).sf(95_000)
theory


# **c.** What percent of employees earn between 65,000 and 80,000?
# 

# In[82]:


above_65 = stats.norm(avg, stdev).sf(65_000)
above_80 = stats.norm(avg, stdev).sf(80_000)
theory = above_65 - above_80
theory


# **d.** What do the top 5% of employees make?

# In[85]:


theory =stats.norm(avg, stdev).isf(.05)
actual = salaries.quantile(.95)["salary"]  # what is the cutoff for the top 95%
theory, actual


# In[ ]:




