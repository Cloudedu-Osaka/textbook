#!/usr/bin/env python
# coding: utf-8

# In[1]:


# initialization for my classroom
import os
from datetime import datetime as dt

def logfile(user=os.environ.get('JUPYTERHUB_USER') or 'jovyan'):
    prefix='/srv'
    if os.path.isdir(prefix) and os.access(prefix, os.W_OK):
        prefix+=('/'+user)
        if not os.path.isdir(prefix):
            os.makedirs(prefix)
    else:
        prefix='.'
    return prefix+'/'+dt.now().strftime('%Y%m%d')+'.log'

path=logfile()
#%logstop
get_ipython().run_line_magic('logstart', '-otq $path append')

# [python - cannot override sys.excepthook - Stack Overflow](https://stackoverflow.com/questions/1261668/cannot-override-sys-excepthook/28758396)
# https://github.com/ipython/ipython/blob/e6432249582e05f438303ce73d082a0351bb383e/IPython/core/interactiveshell.py#L1952

import sys
import traceback
import IPython

try:
    _showtraceback
except NameError:
    _showtraceback=IPython.core.interactiveshell.InteractiveShell.showtraceback

try:
    _showsyntaxerror
except NameError:
    _showsyntaxerror=IPython.core.interactiveshell.InteractiveShell.showsyntaxerror

import logging
logging.basicConfig(filename=path.replace('.log','-exc.log'), format='%(asctime)s %(message)s', level=logging.ERROR, force=True)

import sys
import traceback
import IPython

def showtraceback(self, *args, **kwargs):
    etype, value, tb = self._get_exc_info(kwargs.get('exc_tuple'))
    stb = self.InteractiveTB.structured_traceback(
        etype, value, tb, tb_offset=kwargs.get('tb_offset'))
    logging.error(os.environ.get('JUPYTERHUB_USER') or 'jovyan')
    logging.error(self.InteractiveTB.stb2text(stb))
    _showtraceback(self, *args, **kwargs)

def showsyntaxerror(self, *args, **kwargs):
    etype, value, last_traceback = self._get_exc_info()
    elist = traceback.extract_tb(last_traceback) if kwargs.get('running_compiled_code') else []
    stb = self.SyntaxTB.structured_traceback(etype, value, elist)
    logging.error(os.environ.get('JUPYTERHUB_USER') or 'jovyan')
    logging.error(self.InteractiveTB.stb2text(stb))
    _showsyntaxerror(self, *args, **kwargs)

IPython.core.interactiveshell.InteractiveShell.showtraceback = showtraceback
IPython.core.interactiveshell.InteractiveShell.showsyntaxerror = showsyntaxerror


# In[2]:


from datascience import *
path_data = '../../../assets/data/'
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plots
plots.style.use('fivethirtyeight')

cones = Table.read_table(path_data + 'cones.csv')
nba = Table.read_table(path_data + 'nba_salaries.csv').relabeled(3, 'SALARY')
movies = Table.read_table(path_data + 'movies_by_year.csv')


# # Introduction to Tables
# 
# Pythonを活用してデータを分析することができるようになりました。ここでは表構造に格納されたデータを扱います。
# 
# 表はデータセットを表現する基本的な方法です。表は2つの方法で参照することができます:
# * 各々がデータセット内の全エントリの単一の属性を記述する、名前付きカラム (columns) の列
# * データセットに含まれる各個に関するすべての情報を含む行 (rows) の列
# 
# テーブルについては、次の章以降で詳しく説明します。今のところ、技術的な詳細には触れずに、いくつかの方法を紹介するだけにとどめておきます。
# 
# `cones` テーブルは既にインポートされています; 後でその方法を見ますが、ここではそれを使って作業するだけです。まず、それを見てみましょう。

# In[2]:


cones


# In[ ]:





# In[ ]:





# この表には6つの行があります。各行が1つのアイスクリームコーンに対応しています。アイスクリームコーンはバラ売りです。
# 
# 各コーンはフレーバー、色、価格の3つの属性を持っています。各列はこれらの属性のうちの1つに関するデータを含むので、任意の1つの列のすべてのエントリは同じ種類です。各列はラベルを持ちます。我々は列をそのラベルで呼ぶことにします。
# 
# テーブルメソッド *method* は関数に似ていますが、テーブルに対して操作します。呼び出しは次のようになります。
# 
# `name_of_table.method(arguments)`
# 
# たとえば、テーブルの最初の2行だけを表示したい場合は、テーブルメソッド `show` を使用することができます。

# In[3]:


cones.show(2)


# In[ ]:





# In[ ]:





# 2を任意の列の数で置き換えることができます。もし、6つ以上の列を要求した場合、 `cones` は6列しかないので、6つしか得られません。

# ## Choosing Sets of Columns
# `select` メソッドは、指定された列のみからなる新しいテーブルを作成します。

# In[4]:


cones.select('Flavor')


# In[ ]:





# In[ ]:





# これにより、元のテーブルが変更されることはありません。

# In[5]:


cones


# In[ ]:





# In[ ]:





# 列のラベルをカンマで区切ることにより、複数の列を選択することができます。

# In[6]:


cones.select('Flavor', 'Price')


# In[ ]:





# In[ ]:





# また、不要な列をドロップすることも可能です。上の表は、 `Color` のカラムをドロップすることで作成できます。

# In[7]:


cones.drop('Color')


# In[ ]:





# In[ ]:





# この新しいテーブルに名前を付けて、その名前を入力するだけで再び参照することができます。

# In[8]:


no_colors = cones.drop('Color')

no_colors


# In[ ]:





# In[ ]:





# `select` と同様に、 `drop` メソッドでも小さなテーブルが作成され、元のテーブルは変更されずに残ります。データを調査するために、列の選択またはドロップを使用して、任意の数の小さなテーブルを作成することができます。元のデータテーブルに害を与えることはありません。

# ## Sorting Rows

# `sort` メソッドは、元のテーブルの行を指定した列の値の昇順に並べることで、新しいテーブルを作成します。ここでは、 `cones` のテーブルがコーンの値段の昇順にソートされています。

# In[9]:


cones.sort('Price')


# In[ ]:





# In[ ]:





# 降順に並べ替えるには、`sort` のオプションの引数を使用します。 オプション引数はその名の通り、使わなくてもよいものですが、 メソッドのデフォルトの振る舞いを変えたい場合に使用します。 
# 
# デフォルトでは、 `sort` は指定された列の値の昇順でソートします。降順でソートするには、オプションの引数  `descending=True` を使用します。

# In[10]:


cones.sort('Price', descending=True)


# In[ ]:





# In[ ]:





# `select` and `drop`と同様に、`sort` 方式では元のテーブルが変更されることはありません。

# ## Selecting Rows that Satisfy a Condition
# The `where` メソッドは、指定された条件を満たす行のみからなる新しいテーブルを作成します。この節では、指定した列の値が、同じく指定した値と等しくなければならないという非常に単純な条件を扱います。したがって、 `where` メソッドには2つの引数を与えます。
# 
# 下のセルにあるコードは、チョコレートコーンに対応する行だけからなる表を作成します。

# In[11]:


cones.where('Flavor', 'chocolate')


# In[ ]:





# In[ ]:





# 引数はカンマで区切られ、列のラベルとその列で探している値を取ります。 `where` メソッドは、行が満たすべき条件がより複雑な場合にも使うことができます。そのような状況では、呼び出しも少し複雑になります。
# 
# 値を正確に指定することが重要です。例えば、`chocolate`ではなく、`Chocolate`を指定すると、 `where` はフレーバーが`Chocolate`の行を正しく見つけることができません。

# In[12]:


cones.where('Flavor', 'Chocolate')


# In[ ]:





# In[ ]:





# このセクションの他のすべてのテーブルメソッドと同様に、 `where` は元のテーブルを変更せずに残します。 

# ## Example: Salaries in the NBA

# "The NBA is the highest paying professional sports league in the world," [reported CNN](http://edition.cnn.com/2015/12/04/sport/gallery/highest-paid-nba-players/) in March 2016. The table `nba` contains the [salaries of all National Basketball Association players](https://www.statcrunch.com/app/index.php?dataid=1843341) in 2015-2016.
# 
# Each row represents one player. The columns are:
# 
# | **Column Label**   | Description                                         |
# |--------------------|-----------------------------------------------------|
# | `PLAYER`           | Player's name                                       |
# | `POSITION`         | Player's position on team                           |
# | `TEAM`             | Team name                                           |
# |`SALARY`    | Player's salary in 2015-2016, in millions of dollars|
#  
# The code for the positions is PG (Point Guard), SG (Shooting Guard), PF (Power Forward), SF (Small Forward), and C (Center). But what follows doesn't involve details about how basketball is played.
# 
# The first row shows that Paul Millsap, Power Forward for the Atlanta Hawks, had a salary of almost $\$18.7$ million in 2015-2016.

# In[13]:


nba


# Fans of Stephen Curry can find his row by using `where`.

# In[14]:


nba.where('PLAYER', 'Stephen Curry')


# We can also create a new table called `warriors` consisting of just the data for the Golden State Warriors.

# In[15]:


warriors = nba.where('TEAM', 'Golden State Warriors')
warriors


# By default, the first 10 lines of a table are displayed. You can use `show` to display more or fewer. To display the entire table, use `show` with no argument in the parentheses.

# In[16]:


warriors.show()


# The `nba` table is sorted in alphabetical order of the team names. To see how the players were paid in 2015-2016, it is useful to sort the data by salary. Remember that by default, the sorting is in increasing order.

# In[17]:


nba.sort('SALARY')


# These figures are somewhat difficult to compare as some of these players changed teams during the season and received salaries from more than one team; only the salary from the last team appears in the table.  
# 
# The CNN report is about the other end of the salary scale – the players who were among the highest paid in the world. To identify these players we can sort in descending order of salary and look at the top few rows.

# In[18]:


nba.sort('SALARY', descending=True)


# The late Kobe Bryant was the highest earning NBA player in 2015-2016.

# In[ ]:




