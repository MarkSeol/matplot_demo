#!/usr/bin/python2.7
#

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from matplotlib.finance import candlestick_ohlc
from matplotlib import style
import numpy as np
import urllib

# style.use('ggplot')
style.use('fivethirtyeight')
print style.available

def graph_data(stock):
    # clump same logic together
    # part 1
    fig = plt.figure()
    ax1 = plt.subplot2grid([1, 1], [0, 0])

    # part 2
    stock_price_url = 'http://chartapi.finance.yahoo.com/instrument/1.0/'\
        +stock+ '/chartdata;type=quote;range=10y/csv'

    source_code = urllib.urlopen(stock_price_url).read().decode()
    stock_data = []
    split_source = source_code.split('\n')

    for line in split_source:
        split_line = line.split(',')
        if len(split_line) == 6:
            if 'values' not in line:
                stock_data.append(line)

    date, closep, highp, lowp, openp, volume = np.loadtxt(stock_data,
            delimiter=',', unpack=True,
            converters={0:mdates.strpdate2num('%Y%m%d')})
    ax1.plot(date, closep)
    ax1.plot(date, openp)
    x = 0
    y = len(date)
    ohlc = []

    while x < y:
        data_join = date[x], openp[x], highp[x], lowp[x], closep[x], volume[x]
        ohlc.append(data_join)
        x += 1

    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)

    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    ax1.xaxis.set_major_locator(mticker.MaxNLocator(12))
    ax1.grid(True)

    # Annotation example
    # bbox_props = dict(boxstyle='round', fc='w', ec='k', lw=1)
    bbox_props = dict(boxstyle='larrow', fc='w', ec='k', lw=1)
    ax1.annotate(str(closep[-1]), (date[-1], closep[-1]),
            xytext=(date[-1]+100,  closep[-1]), bbox=bbox_props)

    # part 3
    plt.xlabel('date')
    plt.ylabel('price')
    plt.title('Interesting Graph')
    plt.legend()
    plt.subplots_adjust(left=0.09, bottom=0.18, right=0.94, top=0.93,
            wspace=0.2, hspace=0)
    plt.show()

graph_data('EBAY')

