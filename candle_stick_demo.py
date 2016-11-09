#!/usr/bin/python2.7

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from matplotlib.finance import candlestick_ohlc
from matplotlib import style
import numpy as np
import urllib

# style.use('ggplot')
style.use('fivethirtyeight')

MA1 = 10
MA2 = 30

def moving_average(values, window):
    weights = np.repeat(1.0, window) / window
    smas = np.convolve(values, weights, 'valid')
    return smas

def high_minus_low(highs, lows):
    return highs - lows

highs = [11, 12 ,13, 14, 15]
lows = [1, 2 ,3 ,4 ,5 ]
h_l = list(map(high_minus_low, highs, lows))

print h_l

def graph_data(stock):
    # clump same logic together
    # part 1
    # Title and label should be placed at the edit location
    fig = plt.figure()
    ax1 = plt.subplot2grid([6, 1], [0, 0], rowspan=1, colspan=1)
    plt.title('Interesting Graph')
    ax2 = plt.subplot2grid([6, 1], [1, 0], rowspan=4, colspan=1)
    plt.xlabel('date')
    plt.ylabel('price')
    ax3 = plt.subplot2grid([6, 1], [5, 0], rowspan=1, colspan=1)

    # part 2
    stock_price_url = 'http://chartapi.finance.yahoo.com/instrument/1.0/'\
        +stock+ '/chartdata;type=quote;range=1y/csv'

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

    x = 0
    y = len(date)
    ohlc = []

    while x < y:
        data_join = date[x], openp[x], highp[x], lowp[x], closep[x], volume[x]
        ohlc.append(data_join)
        x += 1

    h_l = list(map(high_minus_low, highp, lowp))
    ax1.plot_date(date, h_l, '-')

    ma1 = moving_average(closep, MA1)
    ma2 = moving_average(closep, MA2)
    start = len(date[MA2-1:])

    candlestick_ohlc(ax2, ohlc, width=0.4, colorup='g', colordown='r')

    ax3.plot(date[-start:], ma1[MA2-MA1:])
    ax3.plot(date[-start:], ma2)


    for label in ax2.xaxis.get_ticklabels():
        label.set_rotation(45)

    ax2.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    ax2.xaxis.set_major_locator(mticker.MaxNLocator(12))
    ax2.grid(True)

    # Annotation example
    # bbox_props = dict(boxstyle='round', fc='w', ec='k', lw=1)
    bbox_props = dict(boxstyle='larrow', fc='w', ec='k', lw=1)
    ax1.annotate(str(closep[-1]), (date[-1], closep[-1]),
            xytext=(date[-1]+100,  closep[-1]), bbox=bbox_props)

    # part 3
    plt.legend()
    plt.subplots_adjust(left=0.09, bottom=0.18, right=0.94, top=0.93,
            wspace=0.2, hspace=0)
    plt.show()

graph_data('EBAY')

