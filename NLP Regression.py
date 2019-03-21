
# coding: utf-8

# In[1]:


import os # operating system operations like check files existance
import datetime # time and date operations
import gc # garbage collector
import pandas as pd # data frames wrangling
import numpy as np # math functions
import feather # read feather file
import matplotlib.pyplot as plt # plot
from scipy import stats # linear regression data
import scipy # cal skew
from IPython.core.interactiveshell import InteractiveShell
import statsmodels.api as sm
import xlrd # read excel date value
import math
InteractiveShell.ast_node_interactivity = "all"  # multiple output per jupyter notebook code block


# In[2]:


os.chdir(r'D:\Dropbox\Dropbox\3. PK & SK\3.6 HKU MFIN\Course\4. MFIN 7036 Natural Language Processing\Presentation\Report'+os.sep)
msf = pd.read_excel('signal_20190319_consolidated.xlsx')
msf['Date'] = pd.to_datetime(msf['Date'])
msf.columns = ['Date','tfidf','bow','omx index','china 50 index']
#msf.set_index('Date',inplace = True)


# In[3]:


msf.head()


# In[4]:


#create lag signal 1 3 7 days ago 
msf['bow_lag1'] = msf['bow'].shift(1)
msf['bow_lag3'] = msf['bow'].shift(3)
msf['bow_lag7'] = msf['bow'].shift(7)
msf['tfidf_lag1'] = msf['tfidf'].shift(1)
msf['tfidf_lag3'] = msf['tfidf'].shift(3)
msf['tfidf_lag7'] = msf['tfidf'].shift(7)


# In[5]:


msf.head()


# In[26]:



def reg_model(df,price,score):
    df = df.dropna(subset = [score])
    y = df[price]
    x = df[score]
    model = sm.OLS(y, sm.add_constant(x)).fit()
    print(model.summary())
    
def print_lag_model(df):
    index_name = ['omx index','china 50 index']
    text_score = ['bow','tfidf']
    lag_list = ['','_lag1','_lag3','_lag7']
    for i in index_name:
        for j in text_score:
            for k in lag_list:
                print('regression of '+i+' and '+j+k,)
                reg_model(df,i,j+k)
                


# In[27]:


print_lag_model(msf)
 

