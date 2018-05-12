#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat May 12 14:22:41 2018

@author: lilhack110
"""
import numpy as np
import pandas as pd
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
from scipy.stats import norm

def get_png(filename,col,name,t_interval,iterations):
   d =pd.read_csv(filename)
   d.index=d.Date
   d=d.drop(columns="Date")
   d=d.drop(columns="Volume") 
   
   log_return= np.log(1+d[col].pct_change())
   u= log_return.mean()
   var= log_return.var()
   stdev= log_return.std()
   drift= u-(0.5*var)
   z=norm.ppf(np.random.rand(10,2))
   daily_return=np.exp(drift+stdev*norm.ppf(np.random.rand(t_interval,iterations)))
   s0= d[col].iloc[-1]
   price_list= np.zeros_like(daily_return)
   price_list[0]=s0
   for i in range(1,t_interval):
    price_list[i]=price_list[i-1]*daily_return[i]
   plt.plot(price_list)
   plt.savefig(name)
