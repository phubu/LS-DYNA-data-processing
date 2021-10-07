import numpy as np
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
#print(countfinal)
removeX = []
removeY = []
for j in range(countfinal):
    removeX.append(x[j])
    removeY.append(y[j])
for xr in removeX:
    x.remove(xr)
for yr in removeY:
    y.remove(yr)
x_new = list(map(float,x))
y_new = list(map(float,y))

print(x_new)
#------------------------------------------------------------------
# phải lay khoang HIC 3,15,36 max trong khoang thoi gian va cham 
t1 = 10
t2 = 27
def a_average(t1 = float, t2 = float):

    index1 = x_new.index(t1)
    index2 = x_new.index(t2)
    max_t = max(t1,t2)
    print(y_new[index1:index2])
    print(x_new[index1:index2])
    #return (np.trapz(y_new[index1:index2], x_new[index1:index2],dx = 1 ))
    return ((((np.trapz(y_new[index1:index2], x_new[index1:index2]))/(t2-t1-2))**2.5)*(t2-t1-2))

print(a_average(t1,t2))

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(x_new,y_new, c='r')
plt.xlabel('Time (ms)')
plt.ylabel('acceleration (g)')
plt.show()