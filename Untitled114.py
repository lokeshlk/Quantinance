#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import data as wb


# In[67]:


my_data = ['AAPL','^GSPC']
data = pd.DataFrame()
for t in my_data:
    data[t] = wb.DataReader(t,data_source = 'yahoo',start ='2017-05-11')['Adj Close']


# In[68]:


log_returns = np.log(data/data.shift(1))


# In[69]:


log_returns.plot()


# In[70]:


cov=log_returns.cov()*250


# In[71]:


market_var = log_returns['^GSPC'].var()*250


# In[72]:


market_var


# In[73]:


p_var=log_returns['AAPL'].var()*250


# In[74]:


cov_var = cov.iloc[0,1]


# In[75]:


cov_var


# In[76]:


beta = cov_var/market_var


# In[77]:


beta


# In[ ]:





# In[ ]:




