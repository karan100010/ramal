import pandas,sys,numpy,os
sys.path.append("/home/arjun/dev/mpl_finance")

from mpl_finance import candlestick_ohlc
import matplotlib.pyplot as plt
from matplotlib.finance import candlestick_ohlc
import matplotlib.dates as mdates


icici=pandas.read_csv("ICICIBANK.NS.csv")
icici['Date']=pandas.to_datetime(icici['Date'])
icici['Date']=icici['Date'].apply(mdates.date2num)

f1 = plt.subplot2grid((6, 4), (1, 0), rowspan=6, colspan=4, axisbg='#07000d')
f1 = plt.subplot2grid((6, 4), (1, 0), rowspan=6, colspan=4, facecolor='#07000d')

candlestick_ohlc(f1,icici.values, width=.6, colorup='#53c156', colordown='#ff1717')

f1.xaxis_date()
f1.xaxis.set_major_formatter(mdates.DateFormatter('%y-%m-%d %H:%M:%S'))
plt.xticks(rotation=45)
plt.ylabel('Stock Price')
plt.xlabel('Date Hours:Minutes')
plt.show()
