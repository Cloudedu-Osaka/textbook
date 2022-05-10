#!/usr/bin/env python
# coding: utf-8

# In[ ]:


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


# # Strings
# 
# 世界のデータの多くはテキストであり、コンピュータの中で表現されるテキストの断片は文字列と呼ばれます。文字列は、単語や文章、あるいは図書館にあるすべての本の内容を表すことができます。文字列には数字（5）や真理値（True）を含めることができるので、それらを記述することもできます。
# 
# 式の意味は、式の構造と組み合わされる値の種類に依存します。例えば、2つの文字列を足すと、もう1つの文字列が生成されます。この式も加算式であることに変わりはありませんが、異なる種類の値を組み合わせています。

# In[1]:


"data" + "science"


# In[ ]:





# In[ ]:





# 加算は完全にリテラル literal (ありのまま) で、2つの文字列の内容を無視して結合されます。異なる単語だからといって、スペースを追加することはありません。

# In[2]:


"data" + " " + "science"


# In[ ]:





# In[ ]:





# 文字列の作成には、一重引用符と二重引用符の両方が使用できます: `'hi'` と `"hi"` は同じ表現です。 二重引用符は、文字列の中にアポストロフィーを含めることができるため、しばしば好まれます。

# In[3]:


"This won't work with a single-quoted string!"


# In[ ]:





# In[ ]:





# Why not? Try it out.

# `str` 関数は、任意の値の文字列表現を返します。この関数を使うと、値を埋め込んだ文字列を作成することができます。

# In[4]:


"That's " + str(1 + 1) + ' ' + str(True)


# In[ ]:





# In[ ]:




