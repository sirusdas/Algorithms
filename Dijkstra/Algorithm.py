import heapq

class Algorithm(object):
    def __init__(self):
         pass

    def calculateShortestPath(self, vertexList, startVertex):

        queue = []
        startVertex.minDistance = 0
        heapq.heappush(queue, startVertex)

        while len(queue) > 0:
            actualVertex = heapq.heappop(queue)
            print("Actual Vertex:{}, min:{}\
                  ".format(actualVertex.name, actualVertex.minDistance))

            for edge in actualVertex.adjacenciesList:
                u = edge.startVertex
                v = edge.targetVertex
                print("Edge.SV.minDistance:{},SV.name:{}, Edge.TV.minDistance:{}\
                      TV.name:{}, Edge.weight:{}\
                      ".format(u.minDistance, u.name, v.minDistance, v.name, edge.weight))
                newDistance = u.minDistance + edge.weight

                if newDistance < v.minDistance:
                    print(".......................in.......................")
                    v.predecessor = u
                    v.minDistance = newDistance
                    heapq.heappush(queue, v)

    def getShortestPathTo(self, targetVertex):
        print("Shortest path to target is:", targetVertex.minDistance)
        node = targetVertex

        while node is not None:
            print("{} -> ".format(node.name))
            node = node.predecessor
