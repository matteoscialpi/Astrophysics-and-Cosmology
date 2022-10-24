import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams.update({'font.size': 10})

joint=np.zeros([26,26],float)
for i in range(len(joint)):
    j=2*i+1
    joint[i]=np.genfromtxt('alphabet.txt',dtype=float,usecols=(j))
joint=np.transpose(joint)
plt.imshow(joint)
plt.title('P(xy)')
plt.show()
joint/=100.

#%%

### P(x|y) ###
P_y=np.zeros(26,float)
P_x_y=np.zeros([26,26],float)
for l in range(len(joint)):
    P_y[l]=np.sum(joint[l])
    for m in range(len(joint)):
        P_x_y[l][m]=joint[l][m]/P_y[l]
P_x_y*=100.
plt.imshow(P_x_y)
plt.title('P(x|y)')
plt.show()

P_x_y=pd.DataFrame(P_x_y)

#%%

### P(y|x) ###
P_x=np.zeros(26,float)
P_y_x=np.zeros([26,26],float)
joint2=np.transpose(joint)
for k in range(len(joint)):
    P_x[k]=np.sum(joint2[k])

for w in range(len(joint)):
    for n in range(len(joint)):
        P_y_x[w][n]=joint[w][n]/P_x[n]
P_y_x*=100.
plt.imshow(P_y_x)
plt.title('P(y|x)')
plt.show()
