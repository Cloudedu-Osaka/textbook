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


# # String Methods
# 
# 既存の文字列から、関連する文字列を作成するには、文字列を操作する関数である文字列メソッドを使用します。これらのメソッドを呼び出すには、文字列の後にドットを置き、その後に関数を呼び出します。
# 
# 例えば、次のメソッドは、文字列を大文字に変換して生成します。

# In[1]:


"loud".upper()


# In[ ]:





# In[ ]:





# おそらく最も重要なメソッドは `replace`で、文字列内の部分文字列のすべてのインスタンスを置き換えます。 `replace` メソッドは、置換する文字列とその置換後の文字列の2つの引数を取ります。

# In[2]:


'hitchhiker'.replace('hi', 'ma')


# In[ ]:





# In[ ]:





# 文字列メソッドは、変数名が文字列に束縛されている限り、変数名を使って呼び出すこともできます。つまり、例えば以下の2段階の処理では、まず「ingrain」を生成し、2回目の置換を施すことで、「train」から「degrade」という単語を生成しています。

# In[3]:


s = "train"
t = s.replace('t', 'ing')
u = t.replace('in', 'de')
u


# In[ ]:





# In[ ]:





# `t = s.replace('t', 'ing')` という行は、文字列 `s`を変更しないので、"train "のままであることに注意してください。 `s.replace('t', 'ing')` というメソッド呼び出しは値を持つだけで、それは文字列 "ingrain" なのです。

# In[4]:


s


# In[ ]:





# In[ ]:





# この教科書ではメソッドを見るのが初めてですが、メソッドは文字列に限ったものではありません。まもなく見るように、他の種類のオブジェクトもメソッドを持つことができます。

# In[ ]:




