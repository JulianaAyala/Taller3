import numpy as np
import matplotlib.pyplot as plt
import sys 

n = int(sys.argv[1])
r = np.random.random(n)
r2= r*2*np.pi
x = np.cos(r2)
y = np.sin(r2)
d = np.zeros(n)
paso = np.arange(n)

for i in range(n):
	x[0]=0
	y[0]=0
	x[i]= x[i-1] + np.cos(r2[i])
	y[i]= y[i-1] + np.sin(r2[i])
	d[i] = np.sqrt((x[i]**2)+(y[i]**2))

plt.scatter(d,paso)
plt.xlabel('distancia')
plt.ylabel('numero de pasos')
plt.savefig('taller3.pdf')
plt.show()



