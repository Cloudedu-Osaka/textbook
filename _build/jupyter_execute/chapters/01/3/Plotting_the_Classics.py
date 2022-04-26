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
from datascience.predicates import are
path_data = '../../../../data/'
import numpy as np
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


# # Plotting the classics
# 
# この例では、Mark Twain の *The Adventures of Huckleberry Finn* と Louisa May Alcott の *Little Women* という2つの古典的な小説の統計を調べます。どのような本でも、そのテキストはコンピュータで高速に読み取ることができます。1923年以前に出版された書籍は、現在*パブリックドメイン*となっており、誰もがテキストをコピーし、どのようにでも利用する権利があります。[Project Gutenberg](http://www.gutenberg.org/) は、パブリックドメインの書籍をオンラインで公開しているウェブサイトです。Pythonを使って、これらの書籍のテキストをウェブから直接読み込むことができます。
# 
# この例は、このテキストの大まかなテーマのいくつかを説明するためのものです。プログラムの詳細がまだ理解できなくても気にしないでください。それよりも、下に表示される画像を理解することに集中しましょう。この後、このテキストで使用されているプログラミング言語Pythonのほとんどの機能を説明します。
# 
# まず、両方の本のテキストを `huck_finn_chapters` と `little_women_chapters` という章のリストに読み込みます。Pythonでは、名前にスペースを含めることができないので、しばしばアンダースコア `_` をスペースの代わりに使用します。以下の行の `=` は、左側の名前に右側で記述された計算の結果を与えています。統一的資源位置指定子（URL: Uniform Resource Locator）は、インターネット上のあるコンテンツのアドレスで、この場合は本のテキストです。`#` 記号はコメントの開始を表し、コンピュータには無視されますがコードを読む人には役に立ちます。

# In[4]:


# Read two books, fast!

huck_finn_url = 'https://www.inferentialthinking.com/data/huck_finn.txt'
huck_finn_text = read_url(huck_finn_url)
huck_finn_chapters = huck_finn_text.split('CHAPTER ')[44:]

little_women_url = 'https://www.inferentialthinking.com/data/little_women.txt'
little_women_text = read_url(little_women_url)
little_women_chapters = little_women_text.split('CHAPTER ')[1:]


# In[ ]:





# In[ ]:





# コンピュータは本の本文を理解することはできませんが、本文の構造をある程度理解することはできます `huck_finn_chapters` という名前は、現在、本の中のすべての章のリストと結びついています。それらをテーブルに配置して、各章がどのように始まるかを見ることができます。  

# In[5]:


# Display the chapters of Huckleberry Finn in a table.

Table().with_column('Chapters', huck_finn_chapters)


# In[ ]:





# In[ ]:





# 各章は、ローマ数字による章番号で始まり、その章の最初の文が続きます。Project Gutenbergは、各章の最初の単語を大文字で表示しています。

# In[ ]:




