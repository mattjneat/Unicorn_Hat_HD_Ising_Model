#%matplotlib inline
# Simulating the Ising model
#!/usr/bin/env python
from __future__ import division
import unicornhathd
import time
import signal
import numpy as np
from numpy.random import rand
import matplotlib.pyplot as plt

unicornhathd.rotation(0)

class Ising():
    ''' Simulating the Ising model '''    
    ## monte carlo moves
    def mcmove(self, config, N, beta):
        ''' This is to execute the monte carlo moves using 
        Metropolis algorithm such that detailed
        balance condition is satisified'''
        for i in range(N):
            for j in range(N):            
                    a = np.random.randint(0, N)
                    b = np.random.randint(0, N)
                    s =  config[a, b]
                    nb = config[(a+1)%N,b] + config[a,(b+1)%N] + config[(a-1)%N,b] + config[a,(b-1)%N]
                    cost = 2*s*nb
                    if cost < 0:	
                        s *= -1
                    elif rand() < np.exp(-cost*beta):
                        s *= -1
                    config[a, b] = s
        return config
    
    def simulate(self):   
        ''' This module simulates the Ising model'''
        N, temp     = 16, 2.5       # Initialse the lattice
        config = 2*np.random.randint(2, size=(N,N))-1
        f = plt.figure(figsize=(15, 15), dpi=80);    
        self.configPlot(f, config, 0, N, 1);
        
        msrmnt = 1001
        for i in range(msrmnt):
            self.mcmove(config, N, 1.0/temp)
            rm.UnicornDisp(config)
            if i == 1:
                self.configPlot(f, config, i, N, 2)
                
            if i == 4:       self.configPlot(f, config, i, N, 3);
            if i == 32:      self.configPlot(f, config, i, N, 4);
            if i == 100:     self.configPlot(f, config, i, N, 5);
            if i == 1000:    self.configPlot(f, config, i, N, 6);
                 
        #rm.UnicornDisp(config)
        #print(config)
                    
    def configPlot(self, f, config, i, N, n_):
        ''' This modules plts the configuration once passed to it along with time etc '''
        X, Y = np.meshgrid(range(N), range(N))
        sp =  f.add_subplot(3, 3, n_ )  
        plt.setp(sp.get_yticklabels(), visible=False)
        plt.setp(sp.get_xticklabels(), visible=False)      
        plt.pcolormesh(X, Y, config, cmap=plt.cm.RdBu);
        plt.title('Time=%d'%i); plt.axis('tight')    
    plt.show()

    def UnicornDisp(self, config):
        '''This module converst the confif matrix to a pi LED friendly form'''
        N = config.shape[0]
        
        M = np.zeros((N, N, 3))
        for i in range(0, N):
            
            for j in range(0,N):
                if config[i,j] == 1:
                    M[i,j,0] = 120
                if config[i,j] == -1:
                    M[i,j,2] = 120
            

        for x in range(unicornhathd.WIDTH):
            for y in range(unicornhathd.HEIGHT):
                r, g, b = M[x][y]
                unicornhathd.set_pixel(x, y, r, g, b)

        unicornhathd.show()
        time.sleep(0.3)
        #print("\nShowing: Ising Model!\nPress Ctrl+C to exit!")

        #signal.pause()

rm = Ising()
rm.simulate()
#plt.show()


