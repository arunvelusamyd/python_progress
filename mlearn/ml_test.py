import numpy
import numpy as np

z = np.array([-1, 0, 1, 2])
print(type(z))
print(isinstance(z,np.ndarray))
z_len = len(z)
range(z_len)
for x in z:
    print(x)
print("z.shape", z.shape,len(z))
g = []
g.append(1)
g.append(2)
g.append(3)
g.append(4)
#g = np.append(g,1)
#g = np.append(g,2)
#g = np.append(g,3)
#g = np.append(g,4)
print("g",g)
