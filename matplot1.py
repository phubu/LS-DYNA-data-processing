#import numpy as np
import matplotlib.pyplot as plt

with open("accel_time_data.txt","r") as f:
    lines = f.readlines()
    lines = [line for line in lines if line != '\t\n']

x = [line.split()[0] for line in lines]
y = [line.split()[1] for line in lines]

for i in range(len(x)):
    try:
        float(x[i])
        count = i
    except:
        countfinal = i+1
for j in range(countfinal):
    x.pop(j)
    y.pop(j)

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x,y, c='r')
plt.show()