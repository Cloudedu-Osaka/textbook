#!/usr/bin/env python
# coding: utf-8

# In[24]:


from datascience import *
import numpy as np
path_data = '../../../assets/data/'
np.set_printoptions(threshold=50)


# # Example: Population Trends
# 
# We are now ready to work with large tables of data. The file below contains "Annual Estimates of the Resident Population by Single Year of Age and Sex for the United States." Notice that `read_table` can read data directly from a URL.

# In[25]:


# As of August 2021, this census file is online here: 
data = 'http://www2.census.gov/programs-surveys/popest/technical-documentation/file-layouts/2010-2019/nc-est2019-agesex-res.csv'

# A local copy can be accessed here in case census.gov moves the file:
# data = path_data + 'nc-est2019-agesex-res.csv'

full_census_table = Table.read_table(data)
full_census_table


# Only the first 10 rows of the table are displayed. Later we will see how to display the entire table; however, this is typically not useful with large tables.
# 
# A [description of the table](https://www2.census.gov/programs-surveys/popest/technical-documentation/file-layouts/2010-2019/nc-est2019-agesex-res.pdf) appears online. 
# 
# The `SEX` column contains numeric codes: `0` stands for the total, `1` for male, and `2` for female. The assumptions underlying this binary categorization are questionable. We will discuss them in the next section.
# 
# In this section we will focus on age and population size.
# 
# The `AGE` column contains ages in completed years, but the special value `999` is a sum of the total population. The "age" `100` too has a special status. In that category, the Census Bureau includes all people aged 100 or more.
# 
# The other columns contain estimates of the US population in each category of sex and age in the years 2010 through 2019. The Census is decennial: it takes place every 10 years. The most recent Census was held in 2020 and the one before that in 2010. The Census Bureau also estimates population changes each year. As explained in the Bureau's description of its [methodology](https://www2.census.gov/programs-surveys/popest/technical-documentation/methodology/2010-2020/methods-statement-v2020-final.pdf), it "adds [the estimated changes] to the last decennial census to produce updated population estimates every year."
# 
# Typically, a publicly available table will contain more information than necessary for a particular investigation or analysis. To get the large table into a more usable form, we have to do some *data cleaning*.
# 
# Suppose we are only interested in the population changes from 2014 to 2019. Let's `select` the relevant columns.

# In[26]:


partial_census_table = full_census_table.select('SEX', 'AGE', 'POPESTIMATE2014', 'POPESTIMATE2019')
partial_census_table


# We can simplify the labels of the selected columns.

# In[27]:


us_pop = partial_census_table.relabeled('POPESTIMATE2014', '2014').relabeled('POPESTIMATE2019', '2019')
us_pop


# ## Ages 97-100
# As a warm-up, let's examine the total population, labeled by `SEX` code 0. Since all these rows will have the same value 0 in the `SEX` column, we will drop that column.

# In[28]:


us_pop_by_age = us_pop.where('SEX', are.equal_to(0)).drop('SEX')
us_pop_by_age


# Now let's look at the population in the highest ages.

# In[29]:


us_pop_by_age.where('AGE', are.between(97, 101))


# Not surprisingly, the numbers of people are smaller at higher ages. For example, there are fewer 99-year-olds than 98-year-olds. 
# 
# But the numbers for `AGE` 100 are quite a bit larger than those for age 99. That is because the row with `AGE` 100 doesn't just represent 100-year-olds. It also includes those who are older than 100. 

# ## Percent Change
# 
# Each column of the table `us_pop_by_age` is an array of the same length, and so columns can be combined using arithmetic. The array below contains the change in population between 2014 and 2019. There is one entry corresponding to each row of `us_pop_by_age`.

# In[30]:


change = us_pop_by_age.column('2019') - us_pop_by_age.column('2014')
change


# We can augment `us_pop_by_age` with a column that contains these changes, both in absolute terms and as percents relative to the value in 2014.

# In[31]:


us_pop_change = us_pop_by_age.with_columns(
    'Change', change,
    'Percent Change', change/us_pop_by_age.column('2014')
)
us_pop_change.set_format('Percent Change', PercentFormatter)


# Almost all the entries displayed in the `Percent Change` column are negative, demonstrating a drop in population at the youngest ages. However, the overall population grew by about 9.9 million people, a percent change of just over 3%.

# In[32]:


us_pop_change.where('AGE', are.equal_to(999))


# Let us compare this to the change at each age. For ease of interpretation, we will sort the table in decreasing order of the absolute change in population, contained in the column `Change`.

# In[33]:


us_pop_change.where(
    'AGE', are.below(999)
).sort('Change', descending=True)


# Take a look at the top few rows. While the percent change is about 3% for the overall population, it jumps to well over 20% for the people in their late sixties and early seventies. This stunning change contributes to what is known as the greying of America.
# 
# What could explain this large increase? We can explore this question by examining the years in which the relevant groups were born.
# 
# - Those who were in the age group 69 to 72 in 2014 were born in the years 1942 to 1945. The attack on Pearl Harbor was in late 1941, and by 1942 U.S. forces were heavily engaged in a massive war that ended in 1945. 
# 
# - Those who were 69 to 72 years old in 2019 were born in the years 1947 to 1950, at the height of the post-WWII baby boom in the United States. 
# 
# The post-war jump in births is a major reason for the large changes that we have observed.

# In[ ]:




