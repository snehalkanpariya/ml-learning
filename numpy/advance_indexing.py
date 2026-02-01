import numpy as np

a=np.array([1,2,3,4,5,6])
idx=np.array([1,3,5])
print(a[idx])
c=a>3
print(a[c])
