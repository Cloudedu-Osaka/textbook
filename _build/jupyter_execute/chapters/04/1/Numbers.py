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


# # Numbers
# 
# コンピュータは数値計算を行うために設計されていますが、数値を扱う上で、定量的なデータを扱うプログラマーが知っておくべき重要な内容がいくつかあります。Pythonは（他の多くのプログラミング言語と同様に）2つの異なるタイプの数を区別します:
# 
# * Python言語では、整数を `int` 値と呼びます。小数点を含まない整数（負、0、正）のみを表現することができます。
# * 実数は、Python言語では `float` 値 (または浮動小数点値 *floating point values*）と呼ばれています。整数や分数を表現することができますが、いくつかの制限があります。
# 
# 数字の種類は、表示の仕方でわかります: `int` 値には小数点がなく、 `float` 値には常に小数点があります。

# In[1]:


# Some int values
2


# In[2]:


1 + 3


# In[3]:


-1234567890000000000


# In[4]:


# Some float values
1.2


# In[5]:


3.0


# In[ ]:





# In[ ]:





# In[ ]:





# `float` 値と `int` 値を何らかの算術演算子で結合すると、その結果は常に `float` 値になります。ほとんどの場合、2つの整数が組み合わさって別の整数になりますが、どんな数値 (`int` or `float`) も別の数値で割ると `float` 値になります。非常に大きな値や非常に小さな値の `float` は、科学的記数法で表示されます。

# In[6]:


1.5 + 2


# In[7]:


3 / 1


# In[8]:


-12345678900000000000.0


# In[ ]:





# In[ ]:





# In[ ]:





# `type` 関数は、任意の数値の型を求めることができます。

# In[9]:


type(3)


# In[10]:


type(3 / 1)


# In[ ]:





# In[ ]:





# In[ ]:





# 式の `type` は、その最終的な値の型です。つまり、式が名前であることを `type` 関数が示すことはありません。なぜなら、名前は常に代入された値で評価されるからです。

# In[11]:


x = 3
type(x) # The type of x is an int, not a name


# In[12]:


type(x + 2.5)


# In[ ]:





# In[ ]:





# In[ ]:





# ## More About Float Values
# 
# フロート値は非常に自由度が高いが、制限もあります。 
# 
# 1. `float` は極端に大きな数字も極端に小さな数字も表すことができます。限界はありますが、それに遭遇することはほとんどありません。
# 2. `float` はどんな数でも15桁か16桁の有効数字しか表せず、残りの精度は失われてしまいます。大部分のアプリケーションでは、この限られた精度で十分です。
# 3. `float` の値を算術で結合した後、最後の数桁が不正確になることがあります。小さな丸め誤差は、最初に遭遇したときにはしばしば混乱させられます。
# 
# 最初の制限は2つの方法で観察することができます。計算結果が非常に大きな数である場合、無限大と表現されます。計算結果が非常に小さな数であれば、0として表現されます。

# In[13]:


2e306 * 10


# In[14]:


2e306 * 100


# In[15]:


2e-322 / 10


# In[16]:


2e-322 / 100


# In[ ]:





# In[ ]:





# In[ ]:





# 第二の制限は、有効数字が15桁を超えるような式で観察することができます。これらの余分な桁は、演算を実行する前に破棄されます。

# In[17]:


0.6666666666666666 - 0.6666666666666666123456789


# In[ ]:





# In[ ]:





# In[ ]:





# 3つ目の限界は、等価であるはずの2つの式の差を取るときに見られます。例えば、 `2 ** 0.5` という式は2の平方根を計算しますが、この値を2乗しても正確には2にはなりません。

# In[18]:


2 ** 0.5


# In[19]:


(2 ** 0.5) * (2 ** 0.5)


# In[20]:


(2 ** 0.5) * (2 ** 0.5) - 2


# In[ ]:





# In[ ]:





# In[ ]:





# 上の最終結果は `0.0000000000000004440892098500626`となり、0に非常に近い数字になります。この算術式の正解は0ですが、最後の有効桁に小さな誤差があるため、科学的記数法では全く違って表示されます。このような動作はほとんどのプログラミング言語で見られますが、これはコンピュータで算術演算を行う際の標準的な方法の結果だからです。
# 
# `float` は必ずしも正確ではありませんが、信頼性が高く、あらゆる種類のコンピュータやプログラミング言語で同じように機能します。

# In[ ]:





# In[ ]:





# In[ ]:




