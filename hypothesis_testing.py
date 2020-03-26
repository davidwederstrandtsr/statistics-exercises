#!/usr/bin/env python
# coding: utf-8

# In[1]:


from math import sqrt

get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import env

from scipy import stats
from datetime import date

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


# ## Correlation Exercise
# Correlation measures the linear relationship between two continuous variables

# #### Use the telco_churn data. 

# In[12]:


url = f'mysql+pymysql://{env.user}:{env.password}@{env.host}/telco_churn'
    
sql = """select * from customers
join internet_service_types using(internet_service_type_id)"""


# In[13]:


telco = pd.read_sql(sql, url)
telco.head()


# In[14]:


telco[['tenure', "monthly_charges", "total_charges"]].dtypes


# In[15]:


telco.total_charges.value_counts()


# In[16]:


telco.total_charges = telco.total_charges.str.strip()
# count the number of empty string entries
telco[telco.total_charges == '']


# In[17]:


# remove those 11 rows
telco = telco[telco.total_charges != ""]
# make sure everything else is a float
telco.total_charges = telco.total_charges.astype(float)


# In[18]:


telco[['tenure', "monthly_charges", "total_charges"]].dtypes


# #### Does tenure correlate with monthly charges? 

# In[19]:


telco


# In[20]:


alpha = .01
r, p = stats.pearsonr(telco.tenure, telco.monthly_charges)
if p < alpha:
    print("Reject our null hypothesis")
else:
    print("Accept the null hypothesis")
r, p


# #### Total charges? 

# In[21]:


alpha = .01
r, p = stats.pearsonr(telco.tenure, telco.total_charges)
if p < alpha:
    print("Reject our null hypothesis")
    print("There is a linear relationship")
else:
    print("Accept the null hypothesis")
r, p


# #### What happens if you control for phone and internet service?

# In[22]:


telco.columns


# In[23]:


telco.phone_service.value_counts()


# In[24]:


telco.internet_service_type.value_counts()


# In[25]:


phone_no_internet = telco[(telco.phone_service == "Yes") & (telco.internet_service_type == 'None')]
phone_no_internet = phone_no_internet[['tenure', "monthly_charges", "total_charges"]]
phone_no_internet


# In[26]:


stats.pearsonr(phone_no_internet.tenure, phone_no_internet.total_charges)


# In[27]:


phone_fiber = telco[(telco.phone_service == "Yes") & (telco.internet_service_type == "Fiber optic")]
phone_fiber = phone_fiber[['tenure', "monthly_charges", "total_charges"]]
phone_fiber


# In[28]:


stats.pearsonr(phone_fiber.tenure, phone_fiber.total_charges)


# In[ ]:





# #### Total charges? What happens if you control for phone and internet service
# 
# - is there a relationship between how long an employee has been with the company and their salary?

# ## Use the employees database.

# In[29]:


from env import host, user, password
db_name = "employees"
url = f'mysql+pymysql://{user}:{password}@{host}/employees'
query = """
    select emp_no, salary, datediff(curdate(), hire_date) as "days"
    from salaries
    join employees using(emp_no)
    where to_date > curdate()
    """
df = pd.read_sql(query, url)


# In[30]:


df = df.set_index("emp_no")


# In[31]:


df.head()


# Is there a relationship between how long an employee has been with the company and their salary?

# In[32]:


alpha = .01


# In[33]:


r, p = stats.pearsonr(df.days, df.salary)
r, p


# Is there a relationship between how long an employee has been with the company and the number of titles they have had?

# In[34]:


sql = """
select emp_no,
    datediff(curdate(), hire_date) as tenure,
    count(*) as n_titles
from employees
join titles using(emp_no)
group by emp_no
"""

df = pd.read_sql(sql, url)
df = df.set_index("emp_no")
df.head()


# In[ ]:





# ## Use the sleepstudy data. 

# In[35]:


sleep = data('sleepstudy')
sleep.Subject = 'subject_' + sleep.Subject.astype(str)
sleep.head()


# In[36]:


sleep.plot.scatter("Days", "Reaction")


# Is there a relationship between days and reaction time?
# 
# - *Ho:* there is no relationship between the days and the reaction time
# - *Ha:* Ther is a relationship between the days and the reaction time.

# In[37]:


r, p = stats.pearsonr(sleep.Reaction, sleep.Days)

print('r=', r)
print('p=', p)


# In[38]:


print(f'''
Because p ({p:.16f}) < alpha {alpha}, we reject the null hypothesis the there
is no relationship between the days and the reaction times
''')


# ## chi2 Exercises
# $$ \chi^2 = \sum{\frac{(O - E)^2}{E}} $$

# Use the following contingency table to help answer the question of whether using a macbook and being a codeup student are independent of each other.                     
# 
# Macbook Status.        |  Codeup Student |Not Codeup Student  |
# -----------------------|-----------------|--------------------|
# Uses a Macbook         |       49	     |          20        |
# Doesn't Use A Macbook  |	    1	     |          30        |

# - $H_0$: using a macbook and being a codeup student are independent of each ohter
# - $H_a$: using a macbook and being a codeup student are dependent

# In[39]:


df = pd.DataFrame([[49, 20], [1, 30]])
df.columns = ["codeup student", "not codeup"]
df.index = ["macbook", "not macbook"]
df


# In[40]:


chi2, p, degf, expected = stats.chi2_contingency(df)
chi2, p, degf


# In[41]:


alpha = 0.01

if p < alpha:
    print("We reject the null hypothesis")
    print("We can say that we have confidence that having a macbook and being a codeup student are dependent")
else:
    print("We fail to reject the null hypothesis")


# ## 2. Choose another 2 categorical variables from the mpg dataset and perform a 
# c
# h
# i
# 2
#  contingency table test with them. Be sure to state your null and alternative hypotheses.
#  
# - $H_0$: highway fuel efficiency and number of cylinders are independent of each other
# - $H_a$: highway fuel efficiency and number of cylinders are dependent

# In[42]:


mpg = data('mpg')
mpg.head()


# In[43]:


observed = pd.crosstab(mpg.hwy, mpg.cyl)


# In[44]:


n = mpg.shape[0]

hwy_proportions = mpg.hwy.value_counts() / n


# In[45]:


cylinder_proportions = mpg.cyl.value_counts() / n


# In[46]:


expected = pd.DataFrame()

for hwy_group, h_prop in hwy_proportions.iteritems():
    for cylinder_group, c_prop in cylinder_proportions.iteritems():
        expected.loc[cylinder_group, hwy_group] = h_prop * c_prop

expected.sort_index(inplace=True)
expected *= n
expected


# In[47]:


observed = pd.crosstab(mpg.cyl, mpg.hwy)
observed


# In[48]:


chi2, p, degf, expected = stats.chi2_contingency(observed)
p


# In[49]:


print(f'''
Because p ({p:.22f}) < alpha {alpha}, we reject the null hypothesis that
highway fuel efficiency and number of cylinders are independent of each other
''')


# ## 3. Use the data from the employees database to answer these questions:
# 
# - Is an employee's gender independent of whether an employee works in sales or marketing? (only look at current employees)

# - $H_0$: Sales or marketing employees are independant of gender
# - $H_a$: department and gender are dependant

# In[50]:


sql = """
    select dept_name, gender from employees
    join dept_emp using(emp_no)
    join departments using(dept_no)
    where to_date > curdate()
"""
df = pd.read_sql(sql, url)
df.head()


# In[51]:


df = df[df.dept_name.isin(["Marketing", "Sales"])]


# In[52]:


observed = pd.crosstab(df.dept_name, df.gender)


# In[53]:


chi2, p, degf, expected = stats.chi2_contingency(observed)
p


# In[54]:


alpha = 0.01

if p < alpha:
    print("reject the null hypothesis")
else:
    print("fail to reject the null hypothesis")
    print("We fail to reject the null hypothesis that employees gender is independent of whether")
    print("\tsomeone works in marketing or sales")


# In[ ]:





# ######  Is an employee's gender independent of whether or not they are or have been a manager?
# 
# - $H_0$: Gender is independant of whether or not someone is or has been a manager
# - $H_a$: Gender and whether or not someone has been or is a manager is dependent

# In[55]:


sql = """
    SELECT
    e.emp_no IN (SELECT emp_no FROM dept_manager) AS is_manager,
    e.gender
FROM employees e
"""
df = pd.read_sql(sql, url)
df.head()


# In[56]:


observed = pd.crosstab(df.is_manager, df.gender)
observed


# In[57]:


chi2, p, degf, expected= stats.chi2_contingency(observed)
p


# In[58]:


alpha = .01
if p < alpha:
    print("we reject the null hypothesis")
else:
    print("we fail to reject the null hypothesis")


# In[ ]:





