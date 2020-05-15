import numpy as np
adj = np.random.randint(0,2,(100,100))
np.savetxt('text.txt',adj,fmt='%.2f')
