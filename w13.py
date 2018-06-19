import heapq

# ### A Number maze ###

class Graph:

    def __init__(self, matrix):
        with open(matrix) as f:
            self.matrix = [[int(digit) for digit in line.split()] for line in f]

    def make_graph(self):
        # assume square matrix
        size = len(self.matrix)
        graph = [[] for i in range(size * size)]
        vertices = 0
        edges = 0

        posx = 1
        for x in range(size):
            posy = 1
            for y in range(size):
                vertices += 1
                # graph[vertex's number] = [(it's position), [connected
                # vertex's number, (edge's position between vertices), distance to vertex]]

                # vertex's number
                v = x * size + y

                # append vertex's position
                graph[v].append((posx, posy))

                if not x < 1:
                    graph[v].append([v - size, (posx - 1, posy), self.matrix[x][y]])
                    edges += 1
                if x + 1 < size:
                    graph[v].append([v + size, (posx + 1, posy), self.matrix[x][y]])
                    edges += 1
                if not y < 1:
                    graph[v].append([v - 1, (posx, posy - 1), self.matrix[x][y]])
                    edges += 1
                if y + 1 < size:
                    graph[v].append([v + 1, (posx, posy + 1), self.matrix[x][y]])
                    edges += 1
                posy += 1
            posx += 1

        return graph

    def dijkstra(self, graph):

        entrance = 0
        exit = 48
        path = []

        visited = [False for i in range(len(graph))]
        distance = [999999 for i in range(len(graph))]
        distance[entrance] = 0
        previous = [0 for i in range(len(graph))]

        # priority queue
        pqueue = []
        heapq.heappush(pqueue, (0, entrance))

        while pqueue:
            # distance and vertex
            d, v = heapq.heappop(pqueue)
            # dirty hack - in first iteration, v is int, in all others, list
            if type(v) != int:
                v = v[0]
            # print

            if v == exit:
                v = previous[exit]
                while not v == entrance:
                    path.append(graph[v][0])
                    v = previous[v]
                return path

            if not visited[v]:
                # loop over node's neighbours
                for i in range(1, len(graph[v])):
                    # from node list, get list containing info about the current neighbour
                    get_neigh = graph[v][i]
                    # print get_dist[2]
                    if d + get_neigh[2] < distance[get_neigh[0]]:
                        distance[get_neigh[0]] = get_neigh[2] + d
                        heapq.heappush(pqueue, (d + get_neigh[2], graph[v][i]))

                        previous[get_neigh[0]] = v

                    visited[v] = True
        return path

g = Graph('blud.txt')
# g.generate_graph()
print 'Path from end to start: '
print g.dijkstra(g.make_graph())
