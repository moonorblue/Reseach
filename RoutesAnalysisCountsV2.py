from py2neo import Graph
from py2neo import Node, Relationship
import os
import itertools
from os import listdir
import json
import time
import cPickle as pickle
from copy import deepcopy
import sys
import re
import operator
import math
from py2neo.packages.httpstream import http
http.socket_timeout = 9999
from sortedcontainers import SortedList


def getcounts(dataset, day):
    path = '/home/moonorblue/routesV2/' + dataset + '/' + str(day) + '/'
    alldata = listdir(path)
    routeLen = []
    for data in alldata:
        f = open(path + data)
        j = json.load(f)
        uid = str(j['uid'])
        for p in j['route']:
            routeLen.append(len(j['route'][p]))
    f = open('/home/moonorblue/analysis/data/' +
             dataset + '/' + str(day) + '/routeLenV2', 'w')
    f.write(json.dumps(routeLen))
    f.close()

if __name__ == '__main__':
    # dsName = ['FB', 'CA', 'GWL']
    dsName = ['FS']
    splitDays = [1]
    for d in dsName:
        for s in splitDays:
            print d, str(s), str(getcounts(d, s))
