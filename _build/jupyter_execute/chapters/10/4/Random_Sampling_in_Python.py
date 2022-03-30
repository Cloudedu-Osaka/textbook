#!/usr/bin/env python
# coding: utf-8

# In[1]:


from datascience import *
path_data = '../../../assets/data/'
import matplotlib
matplotlib.use('Agg')
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plots
plots.style.use('fivethirtyeight')
import numpy as np


# # Random Sampling in Python 
# 
# This section summarizes the ways you have learned to sample at random using Python, and introduces a new way.
# 
# ## Review: Sampling from a Population in a Table 
# If you are sampling from a population of individuals whose data are represented in the rows of a table, then you can use the Table method `sample` to [randomly select rows](https://inferentialthinking.com/chapters/10/1/Empirical_Distributions.html#id1) of the table. That is, you can use `sample` to select a random sample of individuals.
# 
# By default, `sample` draws uniformly at random with replacement. This is a natural model for chance experiments such as rolling a die.

# In[2]:


faces = np.arange(1, 7)
die = Table().with_columns('Face', faces)
die


# Run the cell below to simulate 7 rolls of a die.

# In[3]:


die.sample(7)


# Sometimes it is more natural to sample individuals at random without replacement. This is called a simple random sample. The argument `with_replacement=False` allows you to do this.

# In[4]:


actors = Table.read_table(path_data + 'actors.csv')
actors


# In[5]:


# Simple random sample of 5 rows
actors.sample(5, with_replacement=False)


# Since `sample` gives you the entire sample in the order in which the rows were selected, you can use Table methods on the sampled table to answer many questions about the sample. For example, you can find the number of times the die showed six spots, or the average number of movies in which the sampled actors appeared, or whether one two specified actors appeared in the sample. You might need multiple lines of code to get some of this information.

# ## Review: Sampling from a Population in an Array 
# 
# If you are sampling from a population of individuals whose data are represented as an array, you can use the NumPy function `np.random.choice` to [randomly select elements of the array](https://inferentialthinking.com/chapters/09/3/Simulation.html#example-number-of-heads-in-100-tosses).
# 
# By default, `np.random.choice` samples at random with replacement.

# In[6]:


# The faces of a die, as an array
faces


# In[7]:


# 7 rolls of the die
np.random.choice(faces, 7)


# The argument `replace=False` allows you to get a simple random sample, that is, a sample drawn at random without replacement.

# In[8]:


# Array of actor names
actor_names = actors.column('Actor')


# In[9]:


# Simple random sample of 5 actor names
np.random.choice(actor_names, 5, replace=False)


# Just as `sample` did, so also `np.random.choice` gives you the entire sequence of sampled elements. You can use array operations to answer many questions about the sample. For example, you can find which actor was the second one to be drawn, or the number of faces of the die that appeared more than once. Some answers might need multiple lines of code.

# ## Sampling from a Categorical Distribution 
# Sometimes we are interested in a categorical attribute of our sampled individuals. For example, we might be looking at whether a coin lands Heads or Tails. Or we might be interested in the political parties of randomly selected voters.
# 
# In such cases, we frequently need the proportions of sampled voters in the different categories. If we have the entire sample, we can calculate these proportions. The function `sample_proportions` in the `datascience` library does that work for us. It is tailored for sampling at random with replacement from a categorical distribution and returns the proportions of sampled elements in each category.
# 
# The `sample_proportions` function takes two arguments:
# - the sample size
# - the distribution of the categories in the population, as a list or array of proportions that add up to 1
# 
# It returns an array containing the distribution of the categories in a random sample of the given size taken from the population. That's an array consisting of the sample proportions in all the different categories, in the same order in which they appeared in the population distribution.
# 
# For example, suppose each plant of a species is red-flowering with chance 25%, pink-flowering with chance 50%, and white-flowering with chance 25%, regardless of the flower colors of all other plants. You can use `sample_proportions` to see the proportions of the different colors among 300 plants of the species.

# In[10]:


# Species distribution of flower colors:
# Proportions are in the order Red, Pink, White
species_proportions = [0.25, 0.5, .25]

sample_size = 300

# Distribution of sample
sample_distribution = sample_proportions(sample_size, species_proportions)
sample_distribution


# As you expect, the proportions in the sample sum to 1.

# In[11]:


sum(sample_distribution)


# The categories in `species_proportions` are in the order Red, Pink, White. That order is preserved by `sample_proportions`. If you just want the proportion of pink-flowering plants in the sample, you can use `item`:

# In[12]:


# Sample proportion of Heads
sample_distribution.item(1)


# You can use `sample_proportions` and array operations to answer questions based only on the proportions of sampled individuals in the different categories. You will not be able to answer questions that require more detailed information about the sample, such as which of the sampled plants had each of the different colors.

# In[ ]:




