# Computational and Inferential Thinking: The Foundations of Data Science

2nd Edition by [Ani Adhikari](http://statistics.berkeley.edu/people/ani-adhikari), [John DeNero](http://denero.org), [David Wagner](https://www.cs.berkeley.edu/~daw/).

This text was originally developed for the UC Berkeley course [Data 8: Foundations of Data Science][data8].

You can [view this text online][ghpages] or [view the source][source].

[data8]: http://data8.org/
[ghpages]: https://inferentialthinking.com
[source]: https://github.com/data-8/textbook

The contents of this book are licensed for free consumption under the following license:
[Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International (CC BY-NC-ND 4.0)](https://creativecommons.org/licenses/by-nc-nd/4.0/).


```{attention}
この講義では、受講者の操作を記録し、授業進行の指標とします。
そのためノートブックの最初に次のセルを追加しています。
ノートブックを読み込んだときに、これらのセルが自動実行されるように付加情報を埋め込んでいますが、
それが機能するように、もう一つの手順が必要です。

ノートブックを最初に読み込んだときに、右肩に "Not Trusted" と表示されています。
今回の授業で配信するノートブックを予め信頼し "Trusted" 状態にする必要があります。
```

```python
import os
path='/srv'
if os.path.isdir(path) and os.access(path, os.W_OK):
    path+=('/'+(os.environ.get('JUPYTERHUB_USER') or 'jovyan'))
    if not os.path.isdir(path):
        os.makedirs(path)
    path+='/'
else:
    path='./'

from datetime import datetime as dt
path+=dt.now().strftime('%Y%m%d')+'.log'
%logstop
%logstart -otq $path 
```

```{attention}
この記録を次のようにグラフ化します。
```

```python
import pandas as pd
import numpy as np

import matplotlib
import seaborn

ds = np.empty(0)
with open(path, 'r') as f:
    for line in f:
        try:
            d = dt.strptime(line, "# %a, %d %b %Y %H:%M:%S ")
            ds = np.append(ds,pd.Timestamp(d))
        except:
            pass

ts = pd.Series(np.ones(len(ds)), ds)
```

```python
seaborn.set(rc={"figure.figsize":(10,1)})
ax = seaborn.scatterplot(data = ts, alpha=0.2, s=1000, edgecolor='none')
ax.set_yticklabels([]);
ax.set(ylim=(0,2))
ax.set_ylabel(os.environ.get('JUPYTERHUB_USER') or 'jovyan', rotation=0, ha="right", va="center")
ax.plot();
```

```{attention}
この講義では、受講者の操作を記録し、授業進行の指標とします。
そのためノートブックの最初に次のセルを追加しています。
ノートブックを読み込んだときに、これらのセルが自動実行されるように付加情報を埋め込んでいますが、
それが機能するように、もう一つの手順が必要です。
```


[Security in the Jupyter notebook server — Jupyter Notebook 6.4.10 documentation](https://jupyter-notebook.readthedocs.io/en/stable/security.html#security-in-notebook-documents)

```python
!find textbook/chapters -name \*.ipynb -not -path '*/.*' -exec jupyter trust {} \;
```

```python

```
