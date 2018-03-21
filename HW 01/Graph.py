# Graph


class Graph(object):
    def __init__(self, data):
        if isinstance(data, dict):
            self.__graph = data
        else:
            self.__graph = dict()
            print('ERROR!')

    def searchPath(self, start, end):
        self.__result = []
        self.__generatePath(self.__graph, [start], end, self.__result)
        self.__result.sort(key=lambda x: len(x))
        print('The Path From ', self.__result[0][0], ' to ',
              self.__result[0][-1], ' is: ')
        for path in self.__result:
            print(path)

    def __generatePath(self, graph, path, end, result):
        current = path[-1]
        if current == end:
            result.append(path)
        else:
            for n in graph[current]:
                if n not in path:
                    self.__generatePath(graph, path + [n], end, result)


if __name__ == '__main__':
    data = {
        'A': ['B', 'C', 'D'],
        'B': ['E'],
        'C': ['D', 'F'],
        'D': ['B', 'E', 'G'],
        'E': ['D'],
        'F': ['D', 'G'],
        'G': ['E']
    }

    graph = Graph(data)

    graph.searchPath('A', 'D')
