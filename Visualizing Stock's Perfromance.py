#!/usr/bin/env python
# coding: utf-8

# In[1]:


#importing the data manipulation packages
import pandas as pd
import numpy as np


# In[8]:


#importing the financial data retreiving packages
import pandas_datareader as web
import datetime as dt


# In[3]:


#Importing the visualization package 
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline   #this will allow the visualizations to appear below the code that generatedd them')


# In[181]:


from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()

#Defining Stocks 
y_symbols = [ 'ITC.NS','MCDOWELL-N.NS','RTNINDIA.NS', 'SCHAND.NS', 'TATAPOWER.NS', 'YESBANK.NS']

#Creating Dates
from datetime import datetime
startdate = datetime(2022,1,1)
enddate = datetime(2022,7,1)

#Retreiving Data from Yahoo finance 
stockdata = pdr.get_data_yahoo(y_symbols, start=startdate, end=enddate)

#Viewing the data that is retreived
y_symbols
stockdata


# In[182]:


stockdata ['Adj Close']


# In[183]:


#Plotting the graph of the retreived data to visualize 
adj_date = stockdata["Adj Close"]
adj_date.plot()
plt.title("Stock's Adjusted Price")           #Settign of the title of the graph 
plt.xlabel("Date")                            #setting the X-axis of the graph 
plt.ylabel("Adjusted Closing Price Over Time")  #Setting the Y-axis of teh graph
plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))  #adjusting the attributes
plt.show()


# In[184]:


daily_return = adj_date.pct_change()

daily_return.plot()
plt.title("Daily Simple Rate of Return")
plt.xlabel("Date")
plt.ylabel("Rate of Return")
plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
plt.show()


# In[185]:


daily_return.head()


# In[186]:


fig = plt.figure(figsize=(20, 10))


#ITC.NS
ax1 = plt.subplot(2, 3, 1)
plt.plot(daily_return['ITC.NS'], color='green')
plt.title('ITC')
plt.xlabel('Date')
plt.ylabel('Daily Return')

#SCHAND.NS
ax2 = plt.subplot(2, 3, 2)
plt.plot(daily_return['SCHAND.NS'], color='green')
plt.title('SCHAND')
plt.xlabel('Date')
plt.ylabel('Daily Return')

#TATAPOWER.NS
ax3 = plt.subplot(2, 3, 3)
plt.plot(daily_return['TATAPOWER.NS'], color='green')
plt.title('TATA POWER')
plt.xlabel('Date')
plt.ylabel('Daily Return')

#MCDOWELL-N.NS
ax7 = plt.subplot(2, 3, 4)
plt.plot(daily_return['MCDOWELL-N.NS'], color='green')
plt.title('MCDOWELL-N.NS')
plt.xlabel('Date')
plt.ylabel('Daily Return')
plt.subplots_adjust(wspace=0.3, bottom=0.1)

#RTNINDIA.NS
ax8 = plt.subplot(2, 3, 5)
plt.plot(daily_return['RTNINDIA.NS'], color='green')
plt.title('RTNINDIA.NS')
plt.xlabel('Date')
plt.ylabel('Daily Return')
plt.subplots_adjust(wspace=0.3, bottom=0.1)

#YESBANK.NS
ax9 = plt.subplot(2, 3, 6)
plt.plot(daily_return['YESBANK.NS'], color='green')
plt.title('YESBANK.NS')
plt.xlabel('Date')
plt.ylabel('Daily Return')
plt.subplots_adjust(wspace=0.3, bottom=0.1)

plt.show()


# In[176]:


#Calculating the mean rate of return

mean_daily_return = daily_return.mean()
mean_daily_return

#print(min(mean_daily_return))


# In[171]:


print(f'stock with max return is: {mean_daily_return.idxmax()}')   #check the readme file for justification


# In[187]:


#Plotting bar chart

ax4 = plt.subplot()
ax4.set_xticks(range(len(y_symbols)))
ax4.set_xticklabels(y_symbols)


plt.bar(range(len(y_symbols)), mean_daily_return, color = 'green')

plt.xlabel('Stocks')
plt.ylabel('Mean Daily')
plt.title('Mean Rate of Return x Stocks')
plt.xticks(rotation=90)
plt.show()


# In[162]:


#Calculating the variance

variance_daily_return = daily_return.var()
variance_daily_return


# In[155]:


#Plotting bar chart
ax5 = plt.subplot()
ax5.set_xticks(range(len(y_symbols)))
ax5.set_xticklabels(y_symbols)

plt.bar(range(len(y_symbols)), variance_daily_return, color = 'green')

plt.xlabel('Stocks')
plt.ylabel('Variance')
plt.title('Variance x Stocks')
plt.xticks(rotation=90)
plt.show()


# In[161]:


#Calculating Standard Deviation

sd_daily_return = daily_return.std()
sd_daily_return


# In[158]:


#Plotting bar chart
ax6 = plt.subplot()
ax6.set_xticks(range(len(y_symbols)))
ax6.set_xticklabels(y_symbols)

plt.bar(range(len(y_symbols)), sd_daily_return, color = 'green')

plt.xlabel('Stocks')
plt.ylabel('Standard Deviation')
plt.title('Standard Deviation x Stocks')
plt.xticks(rotation=90)

plt.show()


# In[160]:


#Calculating Correlation

correlation= daily_return.corr()
correlation

