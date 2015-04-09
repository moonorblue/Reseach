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

g = Graph()




#id:"string"

def getAllUser(user_l):
	query = 'MATCH (n:' + user_l + ') RETURN DISTINCT n.id;'
	request = g.cypher.execute(query)
	return request

def getCheckinsFromUser(user_l,uid,place_l):
	query = 'MATCH (n:' + user_l + '{id:{uid}}-[r:VISITED]->(p:'+place_l+') RETURN r.atTime,p ORDER BY r.atTime'
	queryDic = {"uid":uid}
	request = g.cypher.execute(query,queryDic)
	return request

def splitCheckinIntoRouteByDay(checkin_d,days):
	RouteDic = {}
	firstDay = float(checkin[0]['r.atTime'].encode())
	for checkin in checkin_d:
		timestamp = float(checkin['r.atTime'].encode()) - firstDay
		day = int(timestamp/(86400 * days))
		if day in RouteDic:
			RouteDic[day].add(checkin['p'])
		else:
			RouteDic[day] = SortedList([])

	return RouteDic




if __name__ == '__main__':
	datasetLabel = ''
	datasetName = sys.argv[0]

	if datasetName == 'FB':
		datasetLabel = ('User','Place')
	elif datasetName == 'FS':
		datasetLabel = ('FSUser','FSPlace')
	elif datasetName == 'GWL':
		datasetLabel = ('GWLUser','GWLPlace')
	elif datasetName == 'CA':
		datasetLabel = ('CAUser','CAPlace')



