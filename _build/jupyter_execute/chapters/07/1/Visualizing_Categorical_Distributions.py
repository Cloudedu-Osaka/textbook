#!/usr/bin/env python
# coding: utf-8

# In[1]:


from datascience import *
import matplotlib
path_data = '../../../assets/data/'
matplotlib.use('Agg')
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plots
plots.style.use('fivethirtyeight')
import numpy as np
np.set_printoptions(threshold=50)


# # Visualizing Categorical Distributions
# 
# Data come in many forms that are not numerical. Data can be pieces of music, or places on a map. They can also be categories into which you can place individuals. Here are some examples of *categorical* variables.
# 
# - The individuals are cartons of ice-cream, and the variable is the flavor in the carton.
# - The individuals are professional basketball players, and the variable is the player's team.
# - The individuals are years, and the variable is the genre of the highest grossing movie of the year.
# - The individuals are survey respondents, and the variable is the response they choose from among "Not at all satisfied," "Somewhat satisfied," and "Very satisfied."

# The table `icecream` contains data on 30 cartons of ice-cream. 

# In[12]:


icecream = Table().with_columns(
    'Flavor', make_array('Chocolate', 'Strawberry', 'Vanilla'),
    'Number of Cartons', make_array(16, 5, 9)
)
icecream


# The *values* of the categorical variable "flavor" are chocolate, strawberry, and vanilla. 
# 
# Each of the cartons had exactly one of the three flavors. In a *distribution*, each individual belongs to exactly one category and thus has exactly one value. So we have a distribution of flavors.
# 
# The table shows the number of cartons of each flavor. We call this a *distribution table*. A distribution table shows all the values of the variable along with the frequency of each one.

# ## Bar Chart
# The bar chart is a familiar way of visualizing categorical distributions. It displays a bar for each category. The bars are equally spaced and equally wide. The length of each bar is proportional to the frequency of the corresponding category.
# 
# We will draw bar charts with horizontal bars because it's easier to label the bars that way. The Table method is therefore called `barh`. It takes two arguments: the first is the column label of the categories, and the second is the column label of the frequencies.

# In[13]:


icecream.barh('Flavor', 'Number of Cartons')


# If the table consists just of a column of categories and a column of frequencies, as in `icecream`, the method call is even simpler. You can just specify the column containing the categories, and `barh` will use the values in the other column as frequencies.

# In[14]:


icecream.barh('Flavor')


# ## Design Aspects of Bar Charts
# Apart from purely visual differences, there is an important fundamental distinction between bar charts and the two graphs that we saw in the previous sections. Those were the scatter plot and the line plot, both of which display two quantitative variables – the variables on both axes are quantitative. In contrast, the bar chart has categories on one axis and numerical quantities on the other.
# 
# This has consequences for the chart. First, the width of each bar and the space between consecutive bars is entirely up to the person who is producing the graph, or to the program being used to produce it. Python made those choices for us. If you were to draw the bar graph by hand, you could make completely different choices and still have a perfectly correct bar graph, provided you drew all the bars with the same width and kept all the spaces the same.
# 
# Most importantly, the bars can be drawn in any order. The categories "chocolate," "vanilla," and "strawberry" have no universal rank order, unlike for example the numbers 5, 7, and 10.
# 
# This means that we can draw a bar chart that is easier to interpret, by rearranging the bars in decreasing order. To do this, we first rearrange the rows of `icecream` in decreasing order of `Number of Cartons`, and then draw the bar chart.

# In[15]:


icecream.sort('Number of Cartons', descending=True).barh('Flavor')


# This bar chart contains exactly the same information as the previous ones, but it is a little easier to read. While this is not a huge gain in reading a chart with just three bars, it can be quite significant when the number of categories is large.

# ## Grouping Categorical Data
# To construct the table `icecream`, someone had to look at all 30 cartons of ice-cream and count the number of each flavor. But if our table does not already include frequencies, we have to compute the frequencies before we can draw a bar chart. Here is an example where this is necessary.
# 
# The table `top` consists of U.S.A.'s top grossing movies of all time, as of 2017. The first column contains the title of the movie; *Star Wars: The Force Awakens* has the top rank, with a box office gross amount of more than 900 million dollars in the United States. The second column contains the name of the studio that produced the movie. The third contains the domestic box office gross in dollars, and the fourth contains the  gross amount that would have been earned from ticket sales at 2016 prices. The fifth contains the year in which the movie was released. 
# 
# There are 200 movies on the list. Here are the top ten according to unadjusted gross receipts.

# In[3]:


top = Table.read_table(path_data + 'top_movies_2017.csv')
top


# The studios MGM, Fox, Universal, and Paramount show up more than once in the top ten. Which studios will appear most frequently if we look among all 200 rows?
# 
# To figure this out, first notice that all we need is a table with the movies and the studios; the other information is unnecessary.

# In[4]:


movies_and_studios = top.select('Title', 'Studio')


# The Table method `group` allows us to count how frequently each studio appears in the table, by calling each studio a category and collecting all the rows in each of these new categories. 
# 
# The `group` method takes as its argument the label of the column that contains the categories. It returns a table of counts of rows in each category. 
# 
# Thus `group` creates a distribution table that shows how the individuals (movies) are distributed among the categories (studios). 
# 
# The `group` method lists the categories in ascending order. Since our categories are studio names and therefore represented as strings, ascending order means alphabetical order.
# 
# The column of counts is always called `count`, but you can change that if you like by using `relabeled`.

# In[11]:


studio_distribution = movies_and_studios.group('Studio')
studio_distribution


# The table shows that there are 23 different studios and provides the count of movies released by each one. The total of the count is 200, the total number of movies.

# In[12]:


sum(studio_distribution.column('count'))


# We can now use this table, along with the graphing skills acquired above, to draw a bar chart that shows which studios are most frequent among the 200 highest grossing movies.

# In[13]:


studio_distribution.sort('count', descending=True).barh('Studio')


# Buena Vista and Warner Brothers are the most common studios among the top 200 movies. Warner Brothers produces the Harry Potter movies and Buena Vista produces Star Wars. 

# ## Towards Quantitative Variables
# 
# Though years are numerical, we could treat the year of release as a categorical variable and plot the its distribution. That is, for every year we could find how many movies were released that year, and then draw the bar chart of that distribution.
# 
# Let's do that and just look at the 10 earliest years in the distribution.

# In[8]:


movies_and_years = top.select('Title', 'Year')
movies_and_years.group('Year').take(np.arange(10)).barh('Year')


# The years appear in increasing order because `group` sorts the categories from lowest to highest. That is important here because years have a chronological order that has to be maintained. But there is something disquieting about this bar chart. The bars at 1921 and 1937 are just as far apart from each other as the bars at 1937 and 1939. The bar chart doesn't show that none of the 200 movies were released in the years 1922 through 1936, nor in 1938. Such inconsistencies and omissions make the distribution in the early years hard to understand based on this visualization.
# 
# The distribution of a categorical variable can be displayed using a bar chart. But if the variable is not categorical but quantitative, then the numerical relations between its values have to be taken into account when we create visualizations. That is the topic of the next section.

# In[ ]:




