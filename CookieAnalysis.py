#! /usr/bin/env python

# imports of external packages to use in our code
import sys
import math
import numpy as np
import matplotlib.pyplot as plt

# import our Random class from python/Random.py file
sys.path.append(".")
from MySort import MySort

# main function for our CookieAnalysis Python code
if __name__ == "__main__":
   
    haveInput = False

    for i in range(1,len(sys.argv)):
        if sys.argv[i] == '-h' or sys.argv[i] == '--help':
            continue

        InputFile = sys.argv[i]
        haveInput = True
    
    if '-h' in sys.argv or '--help' in sys.argv or not haveInput:
        print ("Usage: %s [options] [input file]" % sys.argv[0])
        print ("  options:")
        print ("   --help(-h)          print options")
        print
        sys.exit(1)
    
    Nmeas = 1
    times = []
    times_avg = []

    need_rate = True
    
    with open(InputFile) as ifile:
        for line in ifile:
            if need_rate:
                need_rate = False
                rate = float(line)
                continue
            
            lineVals = line.split()
            Nmeas = len(lineVals)
            t_avg = 0
            for v in lineVals:
                t_avg += float(v)
                times.append(float(v))

            t_avg /= Nmeas
            times_avg.append(t_avg)

    Sorter = MySort()

    times = Sorter.InsertionSort(times)
    times_avg = Sorter.BubbleSort(times_avg)

    print(times_avg)

    # try some other methods! see how long they take
    # times_avg = Sorter.BubbleSort(times_avg)
    # times_avg = Sorter.InsertionSort(times_avg)
    # times_avg = Sorter.QuickSort(times_avg)

    # ADD YOUR CODE TO PLOT times AND times_avg HERE

    # calculate quantiles of data
     

    times1 = np.array(times)
    
    q68 = np.quantile(times1, 0.68) # 68th percentile
    q95 = np.quantile(times1, 0.95) # 95th percentile
    q997 = np.quantile(times1, 0.997) #99.7th percentile
    q10 = np.quantile (times1, 0.1) # 10th percentile

    # create histogram of our data
    n, bins, patches = plt.hist(times, 16,edgecolor = 'black', linewidth = 3, density=True, facecolor='orange', alpha=0.75)
    plt.yticks(fontsize = 13)
    # plot line at mean
    plt.axvline(times_avg, color='blue', linestyle = 'dashed', linewidth = 3, label = 'Mean')
  
    # plot line at quantiles
    
    plt.axvline(q10, color='red', linestyle = 'dashed', linewidth = 3, label = 'Quartile: 0.10') # 0.10
     
    plt.axvline(q68, color='green', linestyle = 'dashed', linewidth = 3, label = 'Quartile: 0.68') # 0.68
     
    plt.axvline(q95, color='cyan', linestyle = 'dashed', linewidth = 3, label = 'Quartile: 0.95') # 0.95
    
    plt.axvline(q997, color='m', linestyle = 'dashed', linewidth = 3, label = 'Quartile: 0.997') # 0.997
    

    # plot formating options
    plt.xlabel('Time to Next Missing Cookie (days)', fontsize = 15)
    plt.ylabel('Probability', fontsize = 15)
    plt.title('Probability of Missing Cookie Time Intervals', fontsize = 20)
    plt.legend(fontsize = 15)

# show figure (program only ends once closed
    plt.show()

