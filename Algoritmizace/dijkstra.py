# class Vertex:
#     def __init__(self,id,name):
#         self.id = id
#         self.name = name
#         self.minDistance = float('inf')
#         self.previousVertex = None
#         self.edges = []
#         self.visited = False
#
#
# class Edge:
#     def __init__(self,source,target,weight):
#         self.source = source
#         self.target = target
#         self.weight = weight
#
#
# class Dijkstra:
#     def __init__(self):
#         self.vertexes = []
#
#     def computePath(self,sourceId):
#         target = 0
#         for n in range(len(self.vertexes)):
#                 if self.vertexes[n].id == sourceId:
#                     cur = self.vertexes[n]
#                     break
#         self._computePath(None,cur,target)
#
#     def _computePath(self,prev,cur,target):
#         cur.visited = True
#         if target < cur.minDistance:
#             cur.minDistance = target
#             cur.previousVertex = prev
#             for edge in range(len(cur.edges)):
#                 next = cur.edges[edge]
#                 target += cur.weight[edge]
#                 self._computePath(cur,next,target)
#                 target -=cur.weight[edge]
#                 edge += 1
#         return
#
#
#
#
#
#
#
#         #Dijkstra.computePath(self,newSourceID)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#         # for n in self.vertexes:
#         #     if n.id == sourceId:
#         #         n.minDistance = 0
#         #         n.previousVertex = n.id
#         #         prev = n.previousVertex
#         #     for x in edges:
#         #         if x.source == prev and x.target == n.id:
#         #             if n.minDistance > x.weight:
#         #                 n.minDistance = x.weight
#         #                 print(n.minDistance)
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#     def getShortestPathTo(self,targenId):
#         pass
#
#
#
#
#     def createGraph(self, vertexes, edgesToVertexes):
#         self.vertexes = vertexes
#         self.edges = edgesToVertexes
#         for vertex in vertexes:
#             for edge in edgesToVertexes:
#                 if edge.source == vertex.id:
#                     vertex.edges.append(edge)
#
#     def resetDijkstra(self):
#         for n in self.vertexes:
#             n.minDistance = float('inf')
#             n.previousVertex = None
#             n.visited = False
#
#
#     def getVertexes(self):
#         return self.vertexes
#
#
#

class Vertex:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.edges = []
        self.weight = []
        self.minDistance = float('inf')
        self.visited = False
        self.previousVertex = None

class Edge:
    def __init__(self, source, target, weight):
        self.source = source
        self.target = target
        self.weight = weight

class Dijkstra:
    def __init__(self):
        self.vertexes = []

    def computePath(self, sourceId):
        target = 0
        for i in range(len(self.vertexes)):
            if self.vertexes[i].id == sourceId:
                curr = self.vertexes[i]
                break
        self._computePath( None, curr ,target)

    def _computePath(self,  previous,curr, target):
        curr.visited = True
        if curr.minDistance > target:
            curr.minDistance = target
            curr.previousVertex = previous
            for edge in range(len(curr.edges)):
                next = curr.edges[edge].vertex
                target += curr.weight[edge]
                self._computePath(curr, next ,target)
                target -= curr.weight[edge]
                edge += 1
        return

    def getShortestPathTo(self, targetId):
        shortPath = []
        for i in range(len(self.vertexes)):
            if self.vertexes[i].id == targetId:
                curr = self.vertexes[i]
                break

        while curr.previousVertex != None:
            shortPath.append(curr)
            curr = curr.previousVertex
        shortPath.append(curr)
        answer = shortPath[::-1]
        return answer

    def createGraph(self, vertexes, edgesToVertexes):
        self.vertexes.extend(vertexes)

        for i in range(len(vertexes)):
            for j in range(len(edgesToVertexes)):
                if edgesToVertexes[j].source == vertexes[i].id:
                    vertexes[i].edges.append(edgesToVertexes[j])
                    for x in range(len(vertexes)):
                        if vertexes[x].id == edgesToVertexes[j].target:
                            edgesToVertexes[j].vertex = vertexes[x]
                    vertexes[i].weight.append(edgesToVertexes[j].weight)

    def resetDijkstra(self):
        for vertex in self.vertexes:
            vertex.minDistance = float('inf')
            vertex.visited = False
            vertex.previousVertex = None

    def getVertexes(self):
        return self.vertexes

'''
#Test graph
vertexes = [
  Vertex(0, 'Redville'),
  Vertex(1, 'Blueville'),
  Vertex(2, 'Greenville'),
  Vertex(3, 'Orangeville'),
  Vertex(4, 'Purpleville')
]
edges = [
  Edge(0, 1, 5),
  Edge(0, 2, 10),
  Edge(0, 3, 8),
  Edge(1, 0, 5),
  Edge(1, 2, 3),
  Edge(1, 4, 7),
  Edge(2, 0, 10),
  Edge(2, 1, 3),
  Edge(3, 0, 8),
  Edge(3, 4, 2),
  Edge(4, 1, 7),
  Edge(4, 3, 2)
]
#New Dijkstra created
dijkstra = Dijkstra()
#Graph created
dijkstra.createGraph(vertexes,edges)

dijkstraVertexes = dijkstra.getVertexes()


for vertexToCompute in dijkstraVertexes:
    dijkstra.computePath(vertexToCompute.id)
    print('Printing min distance from vertex:'+str(vertexToCompute.name))
    #Print minDitance from current vertex to each other
    for vertex in dijkstraVertexes:
        print('Min distance to:'+str(vertex.name)+' is: '+str(vertex.minDistance))
    dijkstra.resetDijkstra()

for vertexToCompute in dijkstraVertexes:
    dijkstra.computePath(vertexToCompute.id)
    print('Printing min distance from vertex:'+str(vertexToCompute.name))
    #Print minDitance and path from current vertex to each other
    for vertex in dijkstraVertexes:
        print('Min distance to:'+str(vertex.name)+' is: '+str(vertex.minDistance))
        print('Path is:',end=" ")
        #Get shortest path to target vertex
        path = dijkstra.getShortestPathTo(vertex.id)
        for vertexInPath in path:
            print(str(vertexInPath.name),end=" ")
        print()
    #Reset Dijkstra between counting
    dijkstra.resetDijkstra() '''