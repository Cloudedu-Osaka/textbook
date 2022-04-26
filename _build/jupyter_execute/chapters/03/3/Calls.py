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


# # Call Expressions
# 
# 呼び出し式 *call expressions* は、名前付き操作である関数を呼び出します。関数名が最初に、その後に括弧で囲まれた式が続きます。

# In[1]:


abs(-12)


# In[2]:


round(5 - 1.3)


# In[3]:


max(2, 2 + 3, 4)


# In[ ]:





# In[ ]:





# この最後の例では、2, 5, 4の三つの引数 *arguments*で `max` 関数が呼び出されています *called*。括弧内の各式の値が関数に渡され、関数は完全な呼び出し式の最終値を返します *returns*。 `max` 関数は、任意の数の引数を取ることができ、最大値を返します。
# 
# `abs` and `round`, など、デフォルトで利用できる関数もいくつかありますが、Python言語に組み込まれているほとんどの関数は、モジュール *module* と呼ばれる関数の集合体に格納されています。import文 *import statement* は、 `math` or `operator` などのモジュールへのアクセスを提供するために使用されます。

# In[1]:


import math
import operator
math.sqrt(operator.add(4, 5))


# 代わりに `+` and `**` 演算子を使って同等の式を表現することができます。

# In[5]:


(4 + 5) ** 0.5


# In[ ]:





# In[ ]:





# 演算子と呼び出し式は、式の中で一緒に使うことができます。2つの値の百分率の差は、どちらも明らかに初期値や変化していない値を比較するために使用されます。例えば、2014年にフロリダの農場は27億2000万個の卵を生産したのに対し、アイオワの農場は162億5000万個の卵を生産しました (http://quickstats.nass.usda.gov/ )。百分率の差は、値の差の絶対値を100倍し、その平均値で割ったものです。この場合、差は平均値より大きいので、差のパーセントは100より大きくなります。

# In[6]:


florida = 2.72
iowa = 16.25
100*abs(florida-iowa)/((florida+iowa)/2)


# In[ ]:





# In[ ]:





# プログラミング言語を学ぶ上で、様々な関数の振る舞いを学ぶことは重要なことです。Jupyterノートブックは、さまざまな関数の名前と効果を覚えるのに役立ちます。コードセルを編集する際、名前の先頭を入力した後に *tab* キーを押すと、その名前を補完する方法のリストが表示されます。例えば、`math.` の後に *tab* キーを押すと、 `math` モジュールで利用可能なすべての関数が表示されます。入力を続けると、候補が絞り込まれます。関数について詳しく知るには、その名前の後に `?` を付けます。例えば、 `math.log?` と入力すると、 `math` モジュールの `log` 関数の説明が表示されます。

# In[ ]:





# In[ ]:





# In[7]:


get_ipython().run_line_magic('pinfo', 'math.log')


#     log(x[, base])
# 
#     Return the logarithm of x to the given base.
#     If the base not specified, returns the natural logarithm (base e) of x.

# In[ ]:





# In[ ]:





# 呼び出しの例の角括弧は、引数がオプションであることを示します。つまり、 `log` は1つまたは2つの引数で呼び出すことができます。

# In[8]:


math.log(16, 2)


# In[9]:


math.log(16)/math.log(2)


# In[ ]:





# In[ ]:





# [Python's built-in functions](https://docs.python.org/3/library/functions.html) のリストは非常に長く、データサイエンス用途では決して必要とされない関数も多く含まれています。 [mathematical functions in the `math` module](https://docs.python.org/3/library/math.html) も同様に長いです。この教科書では、読者がこれらのリストを記憶したり理解したりすることを期待するのではなく、文脈の中で最も重要な関数を紹介しています。

# In[ ]:




