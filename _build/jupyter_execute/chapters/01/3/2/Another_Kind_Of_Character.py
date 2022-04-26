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
path_data = '../../../../data/'
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


# # Another Kind of Character
# 
# 状況によっては、量と量の関係から予測を立てることができます。このテキストでは、不完全な情報に基づいて正確な予測を行う方法を探り、複数の不確実な情報源を組み合わせて意思決定を行う方法を開発します。
# 
# 複数のソースから得られる情報を可視化する例として、まず、人手で取得するのが面倒な情報をコンピューターで取得する方法を考えてみましょう。小説の文脈では、"character" という言葉には、文字や数字、句読点などの印刷された記号という第二の意味があります。ここでは *Huckleberry Finn* と *Little Women* の各章の文字数とピリオドの数をコンピュータに数えてもらいます。

# In[4]:


# In each chapter, count the number of all characters;
# call this the "length" of the chapter.
# Also count the number of periods.

chars_periods_huck_finn = Table().with_columns([
        'Huck Finn Chapter Length', [len(s) for s in huck_finn_chapters],
        'Number of Periods', np.char.count(huck_finn_chapters, '.')
    ])
chars_periods_little_women = Table().with_columns([
        'Little Women Chapter Length', [len(s) for s in little_women_chapters],
        'Number of Periods', np.char.count(little_women_chapters, '.')
    ])


# In[ ]:





# In[ ]:





# *Huckleberry Finn* のデータです。 表の各行は小説の1章に対応し、その章の文字数とピリオドの数が表示されています。驚くには値しませんが、一般に、文字数の少ない章は、ピリオドも少ない傾向があります: 章が短いほど、文章も少なくなる傾向があり、その逆もまた然りです。しかし、文の長さは様々であり、クエスチョンマークなど他の句読点を含むこともあるため、この関係は完全に予測できるものではありません。

# In[5]:


chars_periods_huck_finn


# In[ ]:





# In[ ]:





# *Little Women* の同様なデータはこちらです。

# In[6]:


chars_periods_little_women


# In[ ]:





# In[ ]:





# *Little Women* の章は、*Huckleberry Finn* の章より全般的に長いことがおわかりいただけると思います。この2つの単純な変数、各章の長さとピリオドの数が、この2冊の本について何かもっと教えてくれるかどうか見てみましょう。これを行う1つの方法は、両方のデータを同じ軸にプロットすることです。
# 
# 下のプロットでは、各書籍の各章に点がついています。青い点は *Huckleberry Finn* 、金の点は *Little Women* に対応します。横軸は期間の数、縦軸は登場人物の数を表しています。

# In[7]:


plots.figure(figsize=(6, 6))
plots.scatter(chars_periods_huck_finn.column(1), 
              chars_periods_huck_finn.column(0), 
              color='darkblue')
plots.scatter(chars_periods_little_women.column(1), 
              chars_periods_little_women.column(0), 
              color='gold')
plots.xlabel('Number of periods in chapter')
plots.ylabel('Number of characters in chapter');


# In[ ]:





# In[ ]:





# このプロットは、私たちが数字を見ただけで観察していたように、 *Little Women* の多くの章が *Huckleberry Finn* の章より長いことを示しています。しかし、このプロットはそれ以上のことも示しています。青い点は、黄色い点と同じように、ほぼ直線の周りに集まっていることに注目してください。しかも、両方の色の点が *同じ* 直線の周りに集まっているように見えるのです。

# では、約100のピリオドが含まれる章をすべて見てみましょう。プロットを見ると、それらの章にはおよそ1万字から1万5千字の文字が含まれていることがわかります。これは1ピリオドあたり約100〜150文字です。
# 
# 実際、プロットを見ると、両書とも平均して、ごく大雑把に見積もって100字から150字の間でピリオドが打たれる傾向にあるようです。もしかしたら、この19世紀の二大小説は、今の私たちにとって非常に身近な存在であるTwitterの140字制限というものを示唆していたのかもしれません。

# ---

# In[15]:


chars_periods_huck_finn.column('Huck Finn Chapter Length')


# In[16]:


chars_periods_huck_finn.column('Number of Periods')


# In[17]:


chars_periods_huck_finn.column('Huck Finn Chapter Length') / chars_periods_huck_finn.column('Number of Periods')


# In[19]:


np.average(chars_periods_huck_finn.column('Huck Finn Chapter Length') 
           / chars_periods_huck_finn.column('Number of Periods'))


# In[26]:


chars_periods_huck_finn.where('Number of Periods', are.between(90,110))


# In[25]:


chars_periods_huck_finn.where('Number of Periods', are.between(90,110)).scatter('Huck Finn Chapter Length')


# In[28]:


np.average(chars_periods_huck_finn.where('Number of Periods', are.between(90,110)).column('Huck Finn Chapter Length')
           / chars_periods_huck_finn.where('Number of Periods', are.between(90,110)).column('Number of Periods'))


# In[27]:


chars_periods_huck_finn.scatter('Huck Finn Chapter Length')


# In[19]:


np.average(chars_periods_huck_finn.column('Huck Finn Chapter Length') 
           / chars_periods_huck_finn.column('Number of Periods'))


# In[ ]:




