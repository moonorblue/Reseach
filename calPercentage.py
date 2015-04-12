from os import listdir
import operator
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot
import json
import re
import math
import numpy as np


def calPercentage(dataset, day):
    dic = {}
    f = open('/home/moonorblue/analysis/data/' +
             dataset + '/' + str(day) + '/routeLenV2')
    j = json.load(f)
    for i in j:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    w = open('/home/moonorblue/analysis/data/' +
             dataset + '/' + str(day) + '/routeLenPerV2.csv', 'w')
    for d in dic:
        w.write(str(d)+','+str(dic[d])+'\n')
    w.close()


if __name__ == '__main__':
    # dsName = ['FB', 'CA', 'GWL']
    dsName = ['FS']
    splitDays = [1]
    for d in dsName:
        for s in splitDays:
            print d, str(s)
            calPercentage(d, s)
