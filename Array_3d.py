import numpy as np

a=np.array([[3,7,6,9],[1,5,2,4],[0,3,2,5]])
print(a)
b=a.reshape(2,6)
print(b)

print("Maximum along axis 0")
print(np.max(a,axis=0))