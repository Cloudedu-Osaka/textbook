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


# # Expressions
# 
# プログラミング言語は人間の言語に比べてはるかに単純です。とはいえ、どんな言語にも学ぶべき文法のルールがあるので、まずはそこから始めてみましょう。この教科書では、プログラミング言語「 [Python](https://www.python.org/) 」を使用します。文法ルールの学習は不可欠であり、最も基本的なプログラムで使用される同じルールは、より高度なプログラムでも中心的な役割を果たします。
# 
# プログラムは式 *expressions* で構成されており、データの組み合わせ方をコンピュータに記述します。例えば、掛け算の式は、2つの数値の間に `*` という記号を入れることで成り立っています。`3 * 4` のような式は、コンピュータによって評価 *evaluated* されます。各セルの最後の式（この場合は `12` ）の値（評価 *evaluation* の結果）が、セルの下に表示されます。

# In[1]:


3 * 4


# In[ ]:





# In[ ]:





# プログラミング言語の文法規則は厳格です。Pythonでは、`*` という記号は2回続けて使えません。コンピュータは、規定の式構造と異なる式を解釈しようとはしません。代わりに、`SyntaxError` というエラーを表示します。言語の構文 *Syntax* はその文法規則の集合であり、`SyntaxError` は式の構造が言語の規則のどれとも一致しないことを示します。

# In[2]:


3 * * 4


# In[ ]:





# In[ ]:





# 表現を少し変えるだけで、意味が全く変わってしまうことがあります。以下では、 `*` の間のスペースが削除されています。2 つの数値式の間に `**` が表示されているため、この式は正規の指数表現（最初の数値を 2 番目の数値のべき乗にしたもの: 3×3×3×3）であることがわかります。記号 `*` と `**` は演算子 *operators* と呼ばれ、それらが結合する値は被演算子 *operands* と呼ばれます。

# In[3]:


3 ** 4


# In[ ]:





# In[ ]:





# **一般的な演算子** データサイエンスでは数値を組み合わせることが多く、プログラミング言語の演算子群は、あらゆる演算を表現できるように設計されています。Pythonでは、以下の演算子が基本的なものです。
# 
# | Expression Type | Operator | Example    | Value     |
# |-----------------|----------|------------|-----------|
# | Addition        | `+`      | `2 + 3`    | `5`       |
# | Subtraction     | `-`      | `2 - 3`    | `-1`      |
# | Multiplication  | `*`      | `2 * 3`    | `6`       |
# | Division        | `/`      | `7 / 3`    | `2.66667` |
# | Remainder       | `%`      | `7 % 3`    | `1`       |
# | Exponentiation  | `**`     | `2 ** 0.5` | `1.41421` |

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# Pythonの式は、代数学でおなじみの優先順位 *precedence* のルールに従います: 乗算と除算は、加算と減算の前に行われます。括弧は、より大きな式の中でより小さな式をグループ化するために使用することができます。

# In[4]:


1 + 2 * 3 * 4 * 5 / 6 ** 3 + 7 + 8 - 9 + 10


# In[5]:


1 + 2 * (3 * 4 * 5 / 6) ** 3 + 7 + 8 - 9 + 10


# In[ ]:





# In[ ]:





# この章では、多くの種類の式を紹介します。プログラミングを学ぶには、学んだことをすべて組み合わせて試し、コンピュータの動作を調べることが必要です。ゼロで割るとどうなるか? 2回続けて割ったらどうなるのか? これらの詳細は、必ずしも専門家（あるいはインターネット）に聞く必要はなく、自分で試してみることで発見できることが多いのです。

# In[ ]:





# In[ ]:




