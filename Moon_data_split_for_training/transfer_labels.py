import numpy as np
import matplotlib.pyplot as plt
data = np.loadtxt('data/A416/A_0_0.txt',delimiter=',')
w = data[:,0]-data[:,2]
h = data[:,1]-data[:,3]
size = np.sqrt(w*h)
plt.hist(size, 100, density = 1,color ='green',alpha = 0.7)
plt.show()