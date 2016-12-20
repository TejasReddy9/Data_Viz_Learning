## Stack plotting 

import matplotlib.pyplot as plt

days = [1,2,3,4,5,6,7]

sleeping =  [10,5 ,6 ,8 ,7 ,5,9]
working  =  [2 ,3 ,5 ,3 ,2 ,7,3]
eating   =  [2 ,4 ,2 ,3 ,2 ,3,4]
playing  =  [10,12,11,10,13,9,8]

plt.plot([],[],label='Sleeping',color='g',linewidth=5)
plt.plot([],[],label='Working',color='r',linewidth=5)
plt.plot([],[],label='Eating',color='b',linewidth=5)
plt.plot([],[],label='Playing',color='y',linewidth=5)

plt.stackplot(days,sleeping,working,eating,playing, colors=['g','r','b','y'],linewidth=5)

plt.xlabel('Days in a week')
plt.ylabel('Tasks done in 24 hours')
plt.title('Daily Tasks and their Distribution\n')

plt.legend()
plt.show()
