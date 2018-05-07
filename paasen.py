#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun May  6 18:22:52 2018

@author: lilhack110
"""

import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
from scipy.stats import norm
ax=pd.read_csv("/home/lilhack110/banks/AXISBANK.NS.csv")
axdf= pd.DataFrame()
axdf= pd.DataFrame(ax)
log_return= np.log(1+axdf.Close.pct_change())
log_return.plot(figsize=(10,6))
plt.show()
price_list= np.zeros_like(daily_return)
u= log_return.mean()
var= log_return.var()
stdev= log_return.std()
drift= u-(0.5*var)
z=norm.ppf(np.random.rand(10,2))
i_interval=1232
iterations=10
daily_return=np.exp(drift+stdev*norm.ppf(np.random.rand(i_interval,iterations)))
s0= axdf.iloc[-1]
price_list= np.zeros_like(daily_return)
price_list[0]=s0
price_list= np.zeros_like(daily_return)
price_list[0]
log_return.plot(figsize=(10,6))
price_list
sO
s0
s0=s0.Close
s0
price_list[0]=s0
for i in range(1,i_interval):
    price_list[i]=price_list[i-1]*daily_return[i]
axdf.Close.plot(figsize=(10,6))
plt.plot(price_list)
plt.show()
