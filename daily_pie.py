import matplotlib.pyplot as plt

days = [1,2,3,4,5,6,7]

# sleeping =  [10,5 ,6 ,8 ,7 ,5,9]
# working  =  [2 ,3 ,5 ,3 ,2 ,7,3]
# eating   =  [2 ,4 ,2 ,3 ,2 ,3,4]
# playing  =  [10,12,11,10,13,9,8]

slices = [9,3,4,8]
tasks = ['sleeping','working','eating','playing']
cols = ['g','r','b','y']

plt.pie(slices,labels=tasks,colors=cols,
		startangle=90,
		autopct='%1.1f%%',
		shadow=True,explode=[0,0.1,0,0])


plt.title('Daily task distribution\n')

plt.show()
