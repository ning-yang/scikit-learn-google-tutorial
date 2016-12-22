'''
- choose many useful feature
- avoid useless feature
- avoid related feature
- easy to understand
'''

import numpy 
import matplotlib.pyplot as plt

greyhounds = 500
labs = 500

grey_height = 28 + 4 * numpy.random.randn(greyhounds)
lab_hieight = 24 + 4 * np.random.randn(labs)

plt.hist([grey_height, lab_hieight], stacked=True, color=['r','b'])
plt.show()