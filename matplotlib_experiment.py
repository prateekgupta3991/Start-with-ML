import numpy as np
import matplotlib.pyplot as plt

total_dogs = 1000
greyhounds = 500
labradors = 500

# random series generation
grey_hieght = 24 + 4 + np.random.randn(greyhounds)
lab_hieght = 24 + 4 + np.random.randn(labradors)

for x in range(len(grey_hieght)) :
    print ("value at idx %d is %s" % (x, grey_hieght[x]))

# lets plot
plt.hist([grey_hieght, lab_hieght], stacked = False, color = ['r', 'b'])
plt.show()