#!/usr/bin/python2.7
import matplotlib.pyplot as plt
import numpy as np
import urllib
import datetime as dt
import time

example = time.time()
print example
print dt.datetime.fromtimestamp(example)

def graph_data(stock):
    # clump same logic together
    # part 1
    fig = plt.figure()
    ax1 = plt.subplot2grid([1, 1], [0, 0])

    # part 2
    stock_price_url = 'http://chartapi.finance.yahoo.com/instrument/1.0/'\
        +stock+ '/chartdata;type=quote;range=10d/csv'

    source_code = urllib.urlopen(stock_price_url).read().decode()
    stock_data = []
    split_source = source_code.split('\n')

    for line in split_source:
        split_line = line.split(',')
        if len(split_line) == 6:
            if 'values' not in line:
                stock_data.append(line)

#    date, closep, highp, lowp, openp, volume = np.loadtxt(stock_data,
#            delimiter=',', unpack=True,
#            converters={0:strpdate2num('%Y%m%d')})

    date, closep, highp, lowp, openp, volume = np.loadtxt(stock_data,
            delimiter=',', unpack=True)

    dateconv = np.vectorize(dt.datetime.fromtimestamp)
    date = dateconv(date)

    ax1.plot_date(date, closep, '-')
    ax1.grid(True, color='g', linestyle='-', linewidth=2)

    # part 3
    plt.xlabel('date')
    plt.ylabel('price')
    plt.title('Interesting Graph')
    plt.legend()
    plt.subplots_adjust(left=0.09, bottom=0.18, right=0.94, top=0.93,
            wspace=0.2, hspace=0)
    plt.show()

graph_data('TSLA')
