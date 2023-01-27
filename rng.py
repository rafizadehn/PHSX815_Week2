#! /usr/bin/env python

# imports of external packages to use in our code
import sys
import numpy as np
import matplotlib.pyplot as plt
from Random import Random

# main function for this Python code
if __name__ == "__main__":
    # if the user includes the flag -h or --help print the options
    if '-h' in sys.argv or '--help' in sys.argv:
        print ("Usage: %s [-seed number]" % sys.argv[0])
        print
        sys.exit(1)

    # default seed
    seed = 5555

    # read the user-provided seed from the command line (if there)
    if '-seed' in sys.argv:
        p = sys.argv.index('-seed')
        seed = sys.argv[p+1]

    # set random seed for numpy
    np.random.seed(seed)

    # class instance of our Random class using seed
    random = Random(seed)

    # create some random data
    N = 10000

    # an array of random numbers from numpy
    x = np.random.rand(N)

    # an array of random numbers using our Random class
    myx = []
    for i in range(0,N):
        myx.append(random.Categorical())

    # export to a created file
    with open(r'dicerolls.txt', 'w') as fp:
        for item in myx:
            fp.write("%s\n" % item)


