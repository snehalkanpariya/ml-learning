import numpy as np

dtype=[('name','S10'),('year',int),('cgpa',float)]

val=[('Snehal',2005,9.6),
     ('Krishiv',2005,6.5),
     ('Richa',2004,7.6)]

a=np.array(val,dtype=dtype)

print(np.sort(a,order='name'))
print(np.sort(a,order=['year','cgpa']))

#s10 is used for storing  the string values
#it is provide the faster access of array than strng
#if name is longer than 10 character then it will cut off first 10 char
