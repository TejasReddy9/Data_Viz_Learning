import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker
from matplotlib.finance import candlestick_ohlc
#candlestick for open high low close price values
from matplotlib import style
import numpy as np
import urllib
import datetime as dt
# sometimes we use import datetime.datetime as datetime, then use datetime.somefuntion
# if you did import datetime as dt, then use dt.datetime.somefunction

#style.use('ggplot')
style.use('fivethirtyeight')
#print(plt.style.available)

#print(plt.__file__)  #prints the location of plt

#function to override date conversion 
#fmt - format 
def bytespdate2num(fmt, encoding='utf-8'):
	strconverter = mdates.strpdate2num(fmt)
	def bytesconverter(b):
		s = b.decode(encoding)
		return strconverter(s)
	return bytesconverter

#function for plotting data in a graph
def graph_data(stock):

	#modification with building subplots and figures
	fig = plt.figure()
	#plotting ax1 subplot2grid( dimensions m*n , starting point , rowspan , colspan  )
	ax1 = plt.subplot2grid((1,1),(0,0))

	#stock_price_url = 'http://chartapi.finance.yahoo.com/instrument/1.0/'+stock+'/chartdata;type=quote;range=10y/csv'
	stock_price_url = 'http://chartapi.finance.yahoo.com/instrument/1.0/'+stock+'/chartdata;type=quote;range=1m/csv'
	#stock_price_url = 'http://chartapi.finance.yahoo.com/instrument/1.0/'+stock+'/chartdata;type=quote;range=10d/csv'
	source_code = urllib.urlopen(stock_price_url).read().decode()

	stock_data = []
	split_source = source_code.split('\n')
	for line in split_source:
		split_line = line.split(',')
		if len(split_line)==6 :
			if 'values' not in line and 'labels' not in line :
				stock_data.append(line)
	date, closep, highp, lowp, openp, volume = np.loadtxt(stock_data,
															delimiter=',',
															unpack=True,
															converters={0: bytespdate2num('%Y%m%d')})

	
	x=0;
	y=len(date)
	ohlc = []

	while x < y:
		append_me = date[x], openp[x], highp[x], lowp[x], closep[x], volume[x]
		# check the order ohlc...
		ohlc.append(append_me)
		x+=1

	#candlestick_ohlc(ax1, ohlc, width=0.4, colorup='g', colordown='r', alpha=0.5)
	ax1.plot(date, openp)
	ax1.plot(date, closep)

	# #for 10 days stock market prices
	# date, closep, highp, lowp, openp, volume = np.loadtxt(stock_data,
	# 														delimiter=',',
	# 														unpack=True)
	# #convert unix timestamp to date
	# dateconv = np.vectorize(dt.datetime.fromtimestamp)
	# date = dateconv(date)
	# # "candle stick graphs" can be use to remove the long lines corresponding to sales between non-selling days

	# replace plt with subplot ax1
	# ax1.plot_date(date, closep,'-', label='Tesla Stock Prices')
	ax1.plot([],[],label='Gain',color='g',alpha=0.3)
	ax1.plot([],[],label='Loss',color='r',alpha=0.3)
	# ax1.axhline(closep[0],color='k',linewidth=2)
	# ax1.fill_between(date,closep[0],closep,where= closep>closep[0], color='g',alpha=0.3)   # alpha is for opaqueness
	# ax1.fill_between(date,closep[0],closep,where= closep<closep[0], color='r',alpha=0.3)   
	# # it is a polygon, so facecolor and edgecolor exists... for now we can also say color

	# #modifications
	# ax1.grid(True)
	# # ax1.xaxis.label.set_color('m')
	# # ax1.yaxis.label.set_color('k')
	# ax1.set_yticks( [0,12,24,36] )
	# #edges of the graph
	# ax1.spines['left'].set_color('c')
	# ax1.spines['right'].set_visible(False)
	# ax1.spines['top'].set_visible(False)
	# ax1.spines['left'].set_linewidth(2)
	# rotating the labels in x axis perfect slant
	for label in ax1.xaxis.get_ticklabels():
		label.set_rotation(45)

	ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
	ax1.xaxis.set_major_locator(mticker.MaxNLocator(10))    # no. of divisions to display on x axis

	plt.xlabel('Date')
	plt.ylabel('Price')
	plt.title(stock) #stock name -- TESLA/EBAY/twitter
	plt.legend()
	plt.subplots_adjust(left=0.09,bottom=0.20,right=0.94,top=0.90,wspace=0.2,hspace=0)
	plt.show()


#graph_data('TSLA')  ----- Tesla
#graph_data('twtr')  ----- Twitter
graph_data('EBAY')