import matplotlib.pyplot as plt
import numpy as np 

#t = np.linspace(0,2,100)
#x = np.sin(2*np.pi*t)
#y = np.cos(2*np.pi*t)

#plt.plot(t,x)
#plt.plot(t,y)



#plot monte carlo linear regression dataset
def montecarlo(num_samples):
    x = np.linspace(0,2,num_samples)
    z = np.random.normal(loc=1.0,scale=0.4,size= 100) + 1
    m = 1.3
    
    return x, (m*(x*z))
x, y = montecarlo(100)
print(x.shape)
print(y.shape)
plt.scatter(x,y)
plt.show()