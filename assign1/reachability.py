#python2

import sys

'read from stdin when submitting'
class Reachability:
    ################### DFS algorithm #############################
    def do_explore_one(self, i, adj, comps, visit, comp_id):
        visit[i] = True
        comps[i] = comp_id
        neigbours = adj[i]
        for j in neigbours:
            if visit[j] == False:
                self.do_explore_one(j, adj, comps, visit, comp_id)

    def do_explore_all(self, adj, comps, visit):
        comp_id = 1
        for i in range(len(adj)):
            if visit[i] == False:
                self.do_explore_one(i, adj, comps, visit, comp_id)
                comp_id = comp_id + 1

    def explore(self, adj):
        comps = [0 for _ in range(len(adj))]
        visit = [False for _ in range(len(adj))]
        self.do_explore_all(adj, comps, visit)
        return comps

    def reach(self, adj, x, y):
        #write your code here
        components = self.explore(adj)
        return 0 if components[x] != components[y] else 1

    ################# build an adjaency list from the input ######
    def load_input_from_file(self):
        f = open('./reach.txt')
        return f.readlines()

    def load_input_from_stdin(self):
        'reads several lines of input and returns it as one string'

        # reading several lines of input
        # at the end of last line press enter
        # then press cmd+d (in Intellij) or ctrl+d (in shell)
        list_input = sys.stdin.readlines()
        return list_input

    def read_input(self):
        list_input = self.load_input_from_stdin()
        input = " ".join(list_input)
        data = list(map(int, input.split()))
        return data

    def make_adj_list(self, data):
        'builds a graph adjency list from the data. data is a list of ints'

        n, m = data[0:2]
        data = data[2:]

        if (2 * m) > len(data):
            raise Exception(
                'Wrong input format. Specified %d edges but there are actually % d' % (m, len(data) / 2))
        edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))

        if len(data) != (2 * m + 2):
            raise Exception('Did not specify the nodes pair that need to be checked for connection. It should be the last line')

        x, y = data[2 * m:]
        adj = [[] for _ in range(n)]
        x, y = x - 1, y - 1
        for (a, b) in edges:
            adj[a - 1].append(b - 1)
            adj[b - 1].append(a - 1)

        return adj, x, y

    def do(self):
        data_str = self.read_input()
        adj, x, y = self.make_adj_list(data_str)
        print(self.reach(adj, x, y))

if __name__ == '__main__':
    try:
        rich = Reachability()
        rich.do()
    except Exception, e:
        print e.message
