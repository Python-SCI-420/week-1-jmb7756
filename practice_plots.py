from matplotlib import pyplot as plt
import numpy as np

# Scatter and Line Plot Info
x = np.array(range(0,20))  #number of mustangs you own
y = np.exp(x*-1)

fig, (sub1, sub2) = plt.subplots(2,1) #Creates a blank subplot of 2 rows 1 column

plt.figure(1) #Figure 1
sub1.plot(x,y)     # Plots x and y on the first row of subplot with regular line graph
sub2.scatter(x,y)  # Plots x and y on second rows of subplot with scatter plot
sub2.set_xlabel('Number of Mustangs You Own')     # Setting x and y labels of plots
sub1.set_ylabel('How Cool You Are')
sub2.set_ylabel('How Cool You Are')
sub1.set_title('# of Mustangs vs. Being Cool')

plt.figure(2)   # Creates separate figure
moms = ['Isaacs Mom','Sams Mom','Zachs Mom','Nicks Mom']
hotness = [0,0,100,1]
x_pos = [0,1,2,3]     # x positions for bars

plt.bar(x_pos,hotness)
plt.title('Amount of times Ive had intercourse with each mom')
plt.ylabel('Total amount of times')
plt.xticks(x_pos,moms)    # replaces x positions (0 through 3) with the names of each mom

plt.show()   # Shows the plots





