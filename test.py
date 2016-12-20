import matplotlib.pyplot as plt

# ### simple plotting graphs
# x1 = [1,2,3]
# y1 = [5,7,4]

# x2 = [1,2,3]
# y2 = [10,14,12]

# plt.plot(x1,y1, label='First graph')
# plt.plot(x2,y2, label='Second graph')

# plt.xlabel('Plot number')
# plt.ylabel('Main variable')

# plt.title('Multiple garphs in same figure')

# # which color belongs to what
# plt.legend() 

# plt.show()


# ### simple bar graphs
# plt.bar([1,3,5,7,9],[1,6,10,5,3], label='Supports Trump')
# plt.bar([2,4,6,8,10],[4,3,5,3,4], label='Supports Hillary',color='g')

# plt.xlabel('various states')
# plt.ylabel('population in million')

# plt.title('Distribution of political support')

# plt.legend()
# plt.show()


# ### simple histogams plotting
# age = [10,23,35,64,46,35,90,38,65,45]     # actual ages
# age_groups = [0,10,20,30,40,50,60,70,80,90,100]   # age-groups

# plt.hist(age,age_groups,histtype='bar',rwidth=0.8)

# plt.xlabel('Age-groups of size 10')
# plt.ylabel('No. of people in that age-group')
# plt.title('Histogram with no. of ppl. lying in the age group')
# plt.legend()
# plt.show()


### simple scattered plots
x = [1,2,3,4,5,6,7,8]
y = [5,2,4,2,1,4,5,2]

plt.scatter(x,y, label='cities to be investigated', color='g', s=25, marker="*")
# marker is for type of marker.. * or o ..
# s is for marker size.. 

plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend()
plt.show()






