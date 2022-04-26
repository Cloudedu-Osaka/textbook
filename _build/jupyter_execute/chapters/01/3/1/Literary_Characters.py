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

IPython.core.interactiveshell.InteractiveShell.showtraceback = showtraceback


# In[2]:


from datascience import *
import numpy as np
path_data = '../../../'
import matplotlib
matplotlib.use('Agg')
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plots
plots.style.use('fivethirtyeight')
import warnings
warnings.simplefilter(action="ignore", category=FutureWarning)

from urllib.request import urlopen 
import re
def read_url(url): 
    return re.sub('\\s+', ' ', urlopen(url).read().decode())


# In[3]:


# Read two books, fast (again)!

huck_finn_url = 'https://www.inferentialthinking.com/data/huck_finn.txt'
huck_finn_text = read_url(huck_finn_url)
huck_finn_chapters = huck_finn_text.split('CHAPTER ')[44:]

little_women_url = 'https://www.inferentialthinking.com/data/little_women.txt'
little_women_text = read_url(little_women_url)
little_women_chapters = little_women_text.split('CHAPTER ')[1:]


# # Literary Characters
# 
# *The Adventures of Huckleberry Finn* は、ハックとジムがミシシッピ川に沿って旅する様子を描いている。トム・ソーヤーも終盤に加わり、アクションがヒートアップしていきます。テキストを読み込むと、これらの登場人物が本のどの場面で何回出てきたかをすぐに視覚化することができます。

# In[7]:


# Count how many times the names Jim, Tom, and Huck appear in each chapter.

counts = Table().with_columns([
        'Jim', np.char.count(huck_finn_chapters, 'Jim'),
        'Tom', np.char.count(huck_finn_chapters, 'Tom'),
        'Huck', np.char.count(huck_finn_chapters, 'Huck')
    ])

# Plot the cumulative counts:
# how many times in Chapter 1, how many times in Chapters 1 and 2, and so on.

cum_counts = counts.cumsum().with_column('Chapter', np.arange(1, 44, 1))
cum_counts.plot(column_for_xticks=3)
plots.title('Cumulative Number of Times Each Name Appears', y=1.08);


# In[ ]:





# In[ ]:





# 上のプロットは、横軸が章番号、縦軸がその章までに各キャラクターが何回登場したかを示しています。 
# 
# ジムが中心人物であることは、彼の名前の登場回数の多さからもわかります。また、30 章以降にトムがやってきてハックとジムと合流するまで、トムがほとんど登場しないことに注目しましょう。この章では、トムがハックとジムのもとにやってきて合流するまで、トムはほとんど言及されず、ハックとジムの行動が激化するにつれて、トムとジムの曲線は急激に上昇します。また、ハックに関しては、語り手であるために、彼の名前はほとんど登場しません。 

# *Little Women* は、南北戦争中に4人の姉妹が共に成長する物語です。この本では、章番号が綴られ、章題はすべて大文字で書かれています。

# In[8]:


# The chapters of Little Women, in a table

Table().with_column('Chapters', little_women_chapters)


# In[ ]:





# In[ ]:





# 主要人物の言及を追跡することで、本書の筋も知ることができます。主人公のジョーは、一人でニューヨークに引っ越す27章までは、メグ、ベス、エイミーの3人の姉妹と定期的に交流しています。

# In[9]:


# Counts of names in the chapters of Little Women

counts = Table().with_columns([
        'Amy', np.char.count(little_women_chapters, 'Amy'),
        'Beth', np.char.count(little_women_chapters, 'Beth'),
        'Jo', np.char.count(little_women_chapters, 'Jo'),
        'Meg', np.char.count(little_women_chapters, 'Meg'),
        'Laurie', np.char.count(little_women_chapters, 'Laurie'),

    ])

# Plot the cumulative counts.

cum_counts = counts.cumsum().with_column('Chapter', np.arange(1, 48, 1))
cum_counts.plot(column_for_xticks=5)
plots.title('Cumulative Number of Times Each Name Appears', y=1.08);


# In[ ]:





# In[ ]:





# ローリーは、最後に女の子の一人と結婚する青年です。プロットをもとに、どの女性と結婚するのか当ててみてください。

# In[ ]:




