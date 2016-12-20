import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1) # gird 1*1 and plot no.1

def animate(i): # i is for interval
	graph_data = open('data.csv','r').read()
	lines = graph_data.split('\n')
	xs = []
	ys = []
	for line in lines:
		if len(line)>1: # skip empty lines
			x,y = line.split(',')
			xs.append(x)
			ys.append(y)
	ax1.clear()
	ax1.plot(xs,ys)

# takes where to animate, and which function should we use, interval in millisec
ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()



