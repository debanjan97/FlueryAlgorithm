'''Takes filename as a command line input containing the graph with total vertices'''
import sys
import pandas as pd
import numpy as np
import copy


def read_graph():
    graph = pd.read_csv(sys.argv[1])
    '''List which will contain all the edges'''
    #print(graph) ''' uncomment this to print the edge list'''
    graph = np.asarray(graph)
    '''transforming the graph into numpy array'''

    adj_list = {}
    '''dictionary to store the adjacency list'''

    '''creating the adjacency list'''
    for edge in graph:
        if edge[0] not in adj_list:
            adj_list[edge[0]] = []
            adj_list[edge[0]].append(edge[1])
        else:
            adj_list[edge[0]].append(edge[1])
        if edge[1] not in adj_list:
            adj_list[edge[1]] = []
            adj_list[edge[1]].append(edge[0])
        else:
            adj_list[edge[1]].append(edge[0])

    return adj_list,graph
    ''' returning adjacency list as well as edge list '''

def DFS(a_list,n,visited,start):
#    print("Visited = "+repr(visited))
    visited.append(start)
    for v in a_list[start]:
        if v not in visited:
            l = DFS(a_list,n,visited,v)
    return len(visited) #returns the no of nodes traversed

''' To get the bridges '''
def get_bridges(adj_list,graph,n):
    bridge = []
    temp_list = {}
    for edge in graph:
        visited = []
        temp_list = copy.deepcopy(adj_list)
        temp_list[edge[0]].remove(edge[1])
        temp_list[edge[1]].remove(edge[0])
        '''removing the edge from the graph'''
#        print("DFS for edge"+repr(edge)+"\n")
#        print(temp_list)
        l = DFS(temp_list,n,visited,edge[0])
#        print(l)
        '''checking if dfs covers all the nodes '''
        if l != n:
            bridge.append(edge.tolist())
            '''If all the nodes arent visited, check is True, thus making the edge a bridge'''
    return bridge

def findEulerTour(adj_list,n,bridge,u):
    for v in adj_list[u]:
        target = [u,v] #edge we want to check
        if target not in bridge or len(adj_list[u]) == 1: #condition for elligibility
            print("%d --- %d "%(u,v))
            adj_list[u].remove(v)
            adj_list[v].remove(u)
            findEulerTour(adj_list,n,bridge,v)


def EulerTour(adj_list,n,bridge,start = 1):
    for i in adj_list:
        if len(adj_list[i]) % 2 == 1:
            ''' getting a starting point '''
            start = i
            break
#    print("Start=%d"%start)
    findEulerTour(adj_list,n,bridge,start)

def main():
    no_of_edges = int(sys.argv[2])
    print("Total Number of edges = %d"%no_of_edges)
    adj_list,graph = read_graph()
    print("Adjacency List of the Given Graph =>\n"+repr(adj_list)+"\n")
#    print(graph)
    bridge = get_bridges(adj_list,graph,no_of_edges)
    '''list which will contain all the bridges'''
    print("List of Bridges =>\n"+repr(bridge)+"\n")
    EulerTour(adj_list,no_of_edges,bridge)

main()
