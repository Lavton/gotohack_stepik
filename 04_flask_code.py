
# coding: utf-8

# In[4]:
import pandas as pd
from flask import Flask

app = Flask(__name__)


# In[5]:
@app.route('/')
@app.route('/index')
def index():
    data = pd.DataFrame.from_csv('render_ready.csv')
    res = "<ul>"
    for f in data.itertuples():
        res += "<li>"+f.body+"<hr></li>"
        res += "</ul>"
    return res


# In[6]:

app.run(debug = True, port=5001)


# In[ ]:



