from os import listdir
import operator
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot
import json
import re
import math
import numpy as np


def plotHistogram(dataset, day):
    plt = pyplot
    f = open('/home/moonorblue/analysis/data/' +
             dataset + '/' + str(day) + '/routeLen')
    j = json.load(f)
    N = max(j)
    data = np.array(j)
    # n, bins, patches = plt.hist(
    #     data, N, facecolor='green', normed=True, alpha=0.5, cumulative=True)
    n, bins, patches = plt.hist(
        data, N, facecolor='green', normed=False, alpha=0.5, cumulative=False)
    plt.xlabel('Route Length')
    plt.ylabel('Counts')
    plt.xticks(range(1, N + 1))
    plt.savefig('/home/moonorblue/analysis/data/' + dataset +
                '/' + str(day) + '/histogram_routeLength.png')
    plt.close()

if __name__ == '__main__':
    dsName = ['FB', 'CA', 'GWL']
    splitDays = [1, 7]
    for d in dsName:
        for s in splitDays:
            print d, str(s)
            plotHistogram(d, s)
