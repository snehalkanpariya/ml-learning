import numpy as np

a1=np.array([12,43,34,23,45,56])
r=a1.reshape(2,3)
print(r)

a2=np.array([45,34,23,45,65,45,34,54])
r=a2.reshape(2,2,2)
print(r)

r=a2.reshape(3,-1)
print(r)
