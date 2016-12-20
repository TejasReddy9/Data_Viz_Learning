# import matplotlib.pyplot as plt
# import csv

# x = []
# y = []

# with open('data.csv','r') as csvfile:
# 	vals = csv.reader(csvfile, delimiter=',')
# 	for row in vals:
# 		x.append( int(row[0]) )
# 		y.append( int(row[1]) )

# plt.plot(x,y,label='Data from CSV file')

# plt.xlabel('departments in a store')
# plt.xlabel('no. of items sold in that department')
# plt.title('Sales in a store')

# plt.legend()
# plt.show()


### using NumPy
import matplotlib.pyplot as plt
import numpy as np

x, y = np.loadtxt('data.csv',delimiter=',',unpack=True)
#unpacks the two data elements seperated by comma in a single line into x and y
#if only one var x is typed, too many values to unpack .. error
#if x,y,z, then less values.. error messages appear

plt.plot(x,y,label='Data from CSV file')

plt.xlabel('departments in a store')
plt.xlabel('no. of items sold in that department')
plt.title('Sales in a store')

plt.legend()
plt.show()