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
    path = '/home/moonorblue/routes/' + dataset + '/' + str(day) + '/'
    routesTotal = 0
    placesTotal = 0
    alldata = listdir(path)
    for data in alldata:
        f = open(path + data)
        j = json.load(f)
        uid = str(j['uid'])
        routesCount = len(j['route'])
        placesCount = 0
        for p in j['route']:
            placesCount += len(j['route'][p])

        routesTotal += routesCount
        placesTotal += placesCount

    return (len(alldata), routesTotal, placesTotal)


if __name__ == '__main__':
    # dsName = ['FB', 'CA', 'GWL']
    dsName = ['FS']
    splitDays = [1, 7]
    for d in dsName:
        for s in splitDays:
            print d, str(s), str(getcounts(d, s))
