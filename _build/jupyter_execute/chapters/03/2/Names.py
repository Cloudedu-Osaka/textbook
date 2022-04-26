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


# # Names
# 
# Pythonでは、代入文 *assignment* を使って値に名前を付けます。代入文では、名前の後に `=` が続き、その後に任意の式が続きます。`=` の右側の式の値が名前に代入 *assigned* されます。一旦、名前に値が割り当てられると、以降の式ではその値がその名前に置き換えられます。

# In[1]:


a = 10
b = 20
a + b


# In[ ]:





# In[ ]:





# あらかじめ割り当てられた名前は、 `=` の右側の式で使用することができます。

# In[2]:


quarter = 1/4
half = 2 * quarter
half


# In[ ]:





# In[ ]:





# ただし、名前に割り当てられるのは、式の現在の値のみです。その値が後で変更されても、その値で定義された名前は自動的に変更されません。

# In[3]:


quarter = 4
half


# In[ ]:





# In[ ]:





# 名前は文字で始めなければなりませんが、文字と数字の両方を含むことができます。名前にスペースを含めることはできません。スペースの代わりにアンダースコア文字 `_` を使用することが一般的です。プログラマーは、 `a` や `b` よりも解釈しやすい名前を選択する必要があります。たとえば、カリフォルニア州バークレーで5ドルの買い物をしたときの消費税を表すには、次のような名前をつけると、さまざまな数量の意味が明確になります。

# In[4]:


purchase_price = 5
state_tax_rate = 0.075
county_tax_rate = 0.02
city_tax_rate = 0
sales_tax_rate = state_tax_rate + county_tax_rate + city_tax_rate
sales_tax = purchase_price * sales_tax_rate
sales_tax


# In[ ]:





# In[ ]:




