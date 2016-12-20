import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from matplotlib.finance import candlestick_ohlc
from matplotlib import style

import numpy as np
import urllib
import datetime as dt

style.use('fivethirtyeight')
# print(plt.style.available)

# print(plt.__file__)

MA1 = 10
MA2 = 30

## at that point,. what is the average till that point values
def moving_average(values, window):
    weights = np.repeat(1.0,window)/window
    smas = np.convolve(values,weights,'valid')
    return smas

## for high-low
def high_minus_low(highs,lows):
    return highs-lows

#quick verification
# highs =[11,12,15,14,13]
# lows = [5,6,2,6,7]
# h_l = list(map(high_minus_low,highs,lows))
# print(h_l)

def bytespdate2num(fmt, encoding='utf-8'):
    strconverter = mdates.strpdate2num(fmt)
    def bytesconverter(b):
        s = b.decode(encoding)
        return strconverter(s)
    return bytesconverter
    

def graph_data(stock):

    fig = plt.figure(facecolor='#f0f0f0')
    #adding more subplots...
    ax1 = plt.subplot2grid((6,1), (0,0),rowspan=1,colspan=1)
    plt.title(stock)  # just after ax1 is declared so it belongs to ax1 subplot
    plt.ylabel('H-L')
    ax2 = plt.subplot2grid((6,1), (1,0),rowspan=4,colspan=1,sharex = ax1)   # sharing axis using sharex
    #plt.xlabel('Date')
    plt.ylabel('Price')
    #multiple y axis  for volume data
    ax2v =ax2.twinx()

    ax3 = plt.subplot2grid((6,1), (5,0),rowspan=1,colspan=1,sharex = ax1)
    plt.ylabel('MAvgs')

    
    stock_price_url = 'http://chartapi.finance.yahoo.com/instrument/1.0/'+stock+'/chartdata;type=quote;range=6m/csv'
    source_code = urllib.urlopen(stock_price_url).read().decode()
    stock_data = []
    split_source = source_code.split('\n')
    for line in split_source:
        split_line = line.split(',')
        if len(split_line) == 6:
            if 'values' not in line and 'labels' not in line:
                stock_data.append(line)

    
    #actual data calculations part.....
    date, closep, highp, lowp, openp, volume = np.loadtxt(stock_data,
                                                          delimiter=',',
                                                          unpack=True,
                                                          converters={0: bytespdate2num('%Y%m%d')})

    x = 0
    y = len(date)
    ohlc = []

    while x < y:
        append_me = date[x], openp[x], highp[x], lowp[x], closep[x], volume[x]
        ohlc.append(append_me)
        x+=1

    ma1 = moving_average(closep,MA1)
    ma2 = moving_average(closep,MA2)
    start = len(date[MA2-1:])

    h_l = list(map(high_minus_low,highp,lowp))

    ax1.plot_date(date[-start:],h_l[-start:],'-',label='H-L')
    ax1.yaxis.set_major_locator(mticker.MaxNLocator(4,prune='lower'))
    #removed overlapping using prune.. removes value of graph below

    candlestick_ohlc(ax2, ohlc[-start:], width=0.4, colorup='#77d879', colordown='#db3f3f')
        

        # cut and paste to bottom for
    # for label in ax2.xaxis.get_ticklabels():
    #     label.set_rotation(45)    
    # ax2.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    # ax2.xaxis.set_major_locator(mticker.MaxNLocator(10))
    
    #prune ax2
    ax2.yaxis.set_major_locator(mticker.MaxNLocator(7,prune='upper'))
    ax2.grid(True)
    
    bbox_props = dict(boxstyle='larrow',facecolor='w',edgecolor='k',linewidth=1)
    # annotate last stock price, dynamically moving at the end of right spine
    ax2.annotate(str(closep[-1]),(date[-1],closep[-1]),
    			xytext= (date[-1]+4 , closep[-1]), 
    			bbox=bbox_props )

    #adding annotation with arrow
    # ax2.annotate('Big News!!',(date[16],highp[16]),
    # 					xytext=(0.5,0.9),textcoords='axes fraction',
    # 					arrowprops = dict(color='grey'))
    # # xytext coords is where to put the text Big News!!
    # # we have say textcoords='axes fraction' to give that fraction coords a meaning
    # # second coordinates is the one which arrow points to  
    # # best position  ---- xytext=(0.8,0.9)


    # font_dict = {'family':'serif',
    # 			'color':'darkred',
    # 			'size':15}
    # ax2.text(date[6],closep[13],'. (7thdate,14thclosep) ',fontdict=font_dict)

    # plt.xlabel('Date')   # belongs to ax2 so put it above
    # plt.ylabel('Price')
    #plt.title(stock) # added to ending subplot usually, ax3
    #plt.legend()


    ax2v.fill_between(date[-start:],0,volume[-start:],
                    color='c',alpha=0.3)
    #can't add label to polygon data ... add fale data
    ax2v.plot([],[],color='c',label='Volume',alpha=0.3)
    ax2v.axes.yaxis.set_ticklabels([])
    ax2v.grid(False)
    ax2v.set_ylim(0,3*volume.max())

    for label in ax3 .xaxis.get_ticklabels():
        label.set_rotation(45)

    ax3.yaxis.set_major_locator(mticker.MaxNLocator(4,prune='upper'))
    ax3.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    ax3.xaxis.set_major_locator(mticker.MaxNLocator(10))


    ax3.plot(date[-start:],ma1[-start:],linewidth=1,label=str(MA1)+'MA')
    ax3.plot(date[-start:],ma2[-start:],linewidth=1,label=str(MA2)+'MA')  
    ax3.fill_between(date[-start:],ma2[-start:],ma1[-start:],
        where=(ma1[-start:]<ma2[-start:]),color='r',alpha=0.5)
    ax3.fill_between(date[-start:],ma2[-start:],ma1[-start:],
        where=(ma1[-start:]>ma2[-start:]),color='g',alpha=0.5)
    
    plt.setp(ax1.get_xticklabels(),visible=False)
    plt.setp(ax2.get_xticklabels(),visible=False)
    plt.subplots_adjust(left=0.09, bottom=0.20, right=0.85, top=0.90, wspace=0.2, hspace=0)
    
    ## legendizing
    ax1.legend()
    leg = ax1.legend(loc=9, ncol=2,prop={'size':11})
    leg.get_frame().set_alpha(0.4)
    
    ax2v.legend()
    leg = ax2v.legend(loc=9, ncol=2,prop={'size':11})
    leg.get_frame().set_alpha(0.4)
    
    ax3.legend()
    leg = ax3.legend(loc=9, ncol=2,prop={'size':11})
    leg.get_frame().set_alpha(0.4)
    

    plt.show()
    fig.savefig('google.png',facecolor=fig.get_facecolor())

graph_data('GOOG')
# for google

