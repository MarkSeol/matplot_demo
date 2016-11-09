#!/usr/bin/python2.7

import matplotlib.pyplot as plt
import numpy as np
import urllib
from matplotlib.dates import strpdate2num

def graph_data(stock):
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
            converters={0:strpdate2num('%Y%m%d')})

    plt.plot_date(date, closep, '-')

    plt.xlabel('date')
    plt.ylabel('price')
    plt.title('Interesting Graph')
    plt.legend()
    plt.show()

graph_data('TSLA')
