import numpy
import math
from matplotlib import pyplot as plt

if __name__ == "__main__":
    u = numpy.random.uniform(0.0,1.0,10000)
    plt.hist(u,bins=[1,2,3,4],weights =u,facecolor='g',alpha=0.75)
    plt.grid(True)
    plt.show()
