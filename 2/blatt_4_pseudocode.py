#! /usr/bin/python3

import sys
from copy import deepcopy

graph = [[[ 1],[   10, 2]],
         [[ 2],[ 1,10, 3]],
         [[ 3],[ 2,10, 4]],
         [[ 4],[ 3,10, 5]],
         [[ 5],[ 4,10, 6]],
         [[ 6],[ 5,10, 7]],
         [[ 7],[ 6,10, 8]],
         [[ 8],[ 7,10, 9]],
         [[ 9],[ 8,10]],
         [[ 10],[ 1, 2, 3, 4, 5, 6, 7, 8, 9]]]

k = 4

def getVertexpPos(graph, vertex):
  i = 0
  while i < len(graph):
    if graph[i][0][0] == vertex:
      return i
    # if
    i += 1
  # while

  return -1
# end def

def checkElementExistAmount(mainNode, vertexes1, vertexes2, size):
  count = 0
  print("mainNode = "+str(mainNode))
  print("vertexes1 = "+str(vertexes1))
  print("vertexes2 = "+str(vertexes2))
  print("size = "+str(size))
  for v2 in vertexes2:
    found = False

    if mainNode == v2:
      #print("mainNode="+str(mainNode)+"  v2="+str(v2))
      found = True
    
    if not found:
      for v1 in vertexes1:
        if v1 == v2:
          #print("v1="+str(v1)+"  v2="+str(v2))
          found = True
          break
        # end if
      # end for
    # end if

    if found:
      count += 1
    # end if
  # end for

  if count >= size:
    print("count = " + str(count) + "\n")
    return True

  return False
# end def

def findClique(graph, size):
  index = 0
  while index < len(graph):
    found = 0
    mainNode = graph[index][0][0]
    pos = 0
    while pos < len(graph[index][1]):
      secondNode = getVertexpPos(graph, graph[index][1][pos])
      index2 = 0
      while index2 < len(graph[secondNode][1]):
        if checkElementExistAmount(mainNode, \
                                   graph[index][1], \
                                   graph[secondNode][1], \
                                   size - 1):
          found += 1
        index2 += 1
      # end while
      pos += 1
    # end while

    if found >= size - 1:
      print("found = "+str(found))
      print("found a clique with node " + str(graph[index][0][0]))
    # end if
    print("end reached")    
    index += 1
  # end while
# end def

if __name__ == "__main__":
  findClique(graph, k)
  print("Hello World!")
# end if
