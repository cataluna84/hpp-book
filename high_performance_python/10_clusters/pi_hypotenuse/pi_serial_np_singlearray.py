import time
import numpy as np


def y_is_in_circle(xsys):
    """Test if x,y coordinate lives within the radius of the unit circle"""
    return xsys[0] * xsys[0] + xsys[1] * xsys[1] <= 1.0


nbr_samples = int(1e7)
xsys = np.random.uniform(size=nbr_samples * 2).reshape(2, nbr_samples)
t1 = time.time()
nbr_in_circle = y_is_in_circle(xsys)
print "Took {}s".format(time.time() - t1)
nbr_in_circle = float(np.sum(nbr_in_circle))
print nbr_in_circle

pi_estimate = nbr_in_circle / nbr_samples * 4
print pi_estimate
print np.pi
