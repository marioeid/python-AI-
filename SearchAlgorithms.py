import math
from queue import PriorityQueue

class Node:
    id = None  # Unique value for each node.
    up = None  # Represents value of neighbors (up, down, left, right).
    down = None
    left = None
    right = None
    previousNode = None  # Represents value of neighbors.
    edgeCost = None  # Represents the cost on the edge from any parent to this node.
    gOfN = None  # Represents the total edge cost
    hOfN = None  # Represents the heuristic value
    heuristicFn = None  # Represents the value of heuristic function

    def __init__(self, value):
        self.value = value


class SearchAlgorithms:
    ''' * DON'T change Class, Function or Parameters Names and Order
        * You can add ANY extra functions,
          classes you need as long as the main
          structure is left as is '''
    path = []  # Represents the correct path from start node to the goal node.
    fullPath = []  # Represents all visited nodes from the start node to the goal node.
    totalCost = -1  # Represents the total cost in case using UCS, AStar (Euclidean or Manhattan)

    def eculidiandis(self,nodeidf,nodeids,rowlen):
        a=int(nodeidf/rowlen)
        b=nodeidf%rowlen

        c=int(nodeids/rowlen)
        d=nodeids%rowlen
        return math.sqrt((a - c)**2+(b - d)** 2)

    def manhatandis(self,nodeidf,nodeids,rowlen):
        a=int(nodeidf/rowlen)
        b=nodeidf%rowlen
        c=int(nodeids/rowlen)
        d=nodeids%rowlen
        return abs(a-c)+abs(b-d)

    def __init__(self, mazeStr, edgeCost=None):
        ''' mazeStr contains the full board
         The board is read row wise,
        the nodes are numbered 0-based starting
        the leftmost node'''
        self.s=mazeStr
        self.ecost=edgeCost
        pass



    def DFS(self):
        # Fill the correct path in self.path
        # self.fullPath should contain the order of visited nodes
        self.path = []
        self.fullPath = []
        s1 = self.s
        s2 = []
        s3 = []
        for i in range(len(s1)):
            if s1[i] == ' ':
                s2.append(s3)
                s3 = []
            elif s1[i] != ',':
                s3.append(s1[i])

        s2.append(s3)

        cnt = 0
        nodes = []
        stnode = Node(0)
        ennode = Node(0)
        for i in range(len(s2)):
            for j in range(len(s2[i])):

                node = Node(s2[i][j])
                node.id = cnt
                node.value = s2[i][j]
                if i > 0:
                    node.up = cnt - len(s2[i])
                if i + 1 < len(s2):
                    node.down = cnt + len(s2[i])
                if j > 0:
                    node.left = cnt - 1

                if j + 1 < len(s2[i]):
                    node.right = cnt + 1
                if s2[i][j] == 'S':
                    stnode = node
                if s2[i][j] == 'E':
                    ennode = node
                cnt = cnt + 1
                nodes.append(node)
       # 0 1 2 3 4 5
       # 6 7 8 9 10 11
        stack=[]
        vis=[False]*cnt
        stack.append(stnode.id)
        parent=[-1]*cnt
        while stack:

            pid = stack.pop()
            curnode = nodes[pid]
            if vis[pid]==False:
                self.fullPath.append(pid)
            if pid==ennode.id:
                break
            vis[pid]=True

            if curnode.right != None and nodes[curnode.right].value != '#' and vis[curnode.right] == False:
                stack.append(curnode.right)
                parent[curnode.right] = curnode.id

            if curnode.left != None and nodes[curnode.left].value != '#' and vis[curnode.left] == False:
                stack.append(curnode.left)
                parent[curnode.left] = curnode.id

            if curnode.down != None and nodes[curnode.down].value != '#' and vis[curnode.down] == False:
                stack.append(curnode.down)
                parent[curnode.down] = curnode.id

            if curnode.up != None and nodes[curnode.up].value != '#' and vis[curnode.up] == False:
                stack.append(curnode.up)
                parent[curnode.up] = curnode.id






        nowid = ennode.id
        self.path.append(ennode.id)

        while parent[nowid] !=-1:
              nowid =parent[nowid]
              self.path.append(nowid)
        self.path.reverse()
        self.path=[]
        return  self.path, self.fullPath


    def BFS(self):
        # Fill the correct path in self.path
        # self.fullPath should contain the order of visited nodes
        self.path = []
        self.fullPath = []
        s1 = self.s
        s2 = []
        s3 = []
        for i in range(len(s1)):
            if s1[i] == ' ':
                s2.append(s3)
                s3 = []
            elif s1[i] != ',':
                s3.append(s1[i])

        s2.append(s3)

        cnt = 0
        nodes =[None] * cnt

        stnode = Node(0)
        ennode = Node(0)
        for i in range(len(s2)):
            for j in range(len(s2[i])):

                node = Node(s2[i][j])
                node.id = cnt
                node.value = s2[i][j]
                if i > 0:
                    node.up = cnt - len(s2[i])
                if i + 1 < len(s2):
                    node.down = cnt + len(s2[i])
                if j > 0:
                    node.left = cnt - 1

                if j + 1 < len(s2[i]):
                    node.right = cnt + 1
                if s2[i][j] == 'S':
                    stnode = node
                if s2[i][j] == 'E':
                    ennode = node
                cnt = cnt + 1
                nodes.append(node)

        que=[]
        vis=[False]*cnt
        que.append(stnode.id)
        vis[stnode.id]=True
        parent=[-1]*cnt
        self.fullPath.append(stnode.id)
        while que:

            pid=que.pop(0)
            curnode=nodes[pid]
            if vis[pid]==False:
               self.fullPath.append(pid)

            vis[pid]=True

            if pid==ennode.id:
                break

            if curnode.up!=None and nodes[curnode.up].value!='#' and vis[curnode.up]==False:
                 que.append(curnode.up)
                 parent[curnode.up]=curnode.id

            if curnode.down != None and nodes[curnode.down].value != '#' and vis[curnode.down]==False:
                 que.append(curnode.down)
                 parent[curnode.down] = curnode.id

            if    curnode.left!=None and nodes[curnode.left].value!='#' and vis[curnode.left]==False:
                    que.append(curnode.left)
                    parent[curnode.left] = curnode.id

            if    curnode.right!=None and nodes[curnode.right].value!='#' and vis[curnode.right]==False:
                        que.append(curnode.right)
                        parent[curnode.right] = curnode.id

        nowid = ennode.id
        self.path.append(ennode.id)

        while parent[nowid]!=-1:
              nowid =parent[nowid]
              self.path.append(nowid)
        self.path.reverse()

        self.path=[]

        return self.path, self.fullPath

    def UCS(self):
        # Fill the correct path in self.path
        # self.fullPath should contain the order of visited nodes
        self.path = []
        self.fullPath = []
        s1 = self.s
        s2 = []
        s3 = []
        for i in range(len(s1)):
            if s1[i] == ' ':
                s2.append(s3)
                s3 = []
            elif s1[i] != ',':
                s3.append(s1[i])

        s2.append(s3)

        cnt = 0
        nodes = []
        stnode = Node(0)
        ennode = Node(0)

        for i in range(len(s2)):
            for j in range(len(s2[i])):

                node = Node(s2[i][j])
                node.id = cnt
                node.gOfN=math.inf
                node.heuristicFn = math.inf
                node.value = s2[i][j]
                if i > 0:
                    node.up = cnt - len(s2[i])
                if i + 1 < len(s2):
                    node.down = cnt + len(s2[i])
                if j > 0:
                    node.left = cnt - 1

                if j + 1 < len(s2[i]):
                    node.right = cnt + 1
                if s2[i][j] == 'S':
                    stnode = node
                if s2[i][j] == 'E':
                    ennode = node
                cnt = cnt + 1
                nodes.append(node)

        cost = self.ecost
        pq = PriorityQueue()
        stnode.gOfN = 0
        nodes[stnode.id]=stnode
        pq.put((stnode.gOfN, stnode.id))
        while pq:

            pair= pq.get()
            curnode=nodes[pair[1]]
            self.fullPath.append(curnode.id)

            if curnode.id == ennode.id:
                break
            if curnode.up != None and nodes[curnode.up].value != '#' and nodes[curnode.up].gOfN > curnode.gOfN + cost[curnode.up]:
                nodes[curnode.up].gOfN = curnode.gOfN + cost[curnode.up]
                pq.put((nodes[curnode.up].gOfN, curnode.up))
                nodes[curnode.up].previousNode = curnode.id

            if curnode.down != None and nodes[curnode.down].value != '#' and nodes[curnode.down].gOfN > curnode.gOfN +cost[curnode.down]:
                nodes[curnode.down].gOfN = curnode.gOfN + cost[curnode.down]
                pq.put((nodes[curnode.down].gOfN, curnode.down))
                nodes[curnode.down].previousNode = curnode.id

            if curnode.left != None and nodes[curnode.left].value != '#' and nodes[curnode.left].gOfN > curnode.gOfN + cost[curnode.left]:
                nodes[curnode.left].gOfN = curnode.gOfN + cost[curnode.left]
                pq.put((nodes[curnode.left].gOfN, curnode.left))
                nodes[curnode.left].previousNode = curnode.id

            if curnode.right != None and nodes[curnode.right].value != '#' and nodes[curnode.right].gOfN > curnode.gOfN + cost[curnode.right]:
                nodes[curnode.right].gOfN = curnode.gOfN + cost[curnode.right]
                pq.put((nodes[curnode.right].gOfN, curnode.right))
                nodes[curnode.right].previousNode = curnode.id



        self.totalCost=nodes[ennode.id].gOfN
        return self.path, self.fullPath, self.totalCost

    def AStarEuclideanHeuristic(self):
        # Cost for a step is calculated based on edge cost of node
        # and use Euclidean Heuristic for evaluating the heuristic value
        # Fill the correct path in self.path
        # self.fullPath should contain the order of visited nodes
        self.path = []
        self.fullPath = []
        s1 = self.s
        s2 = []
        s3 = []
        for i in range(len(s1)):
            if s1[i] == ' ':
                s2.append(s3)
                s3 = []
            elif s1[i] != ',':
                s3.append(s1[i])

        s2.append(s3)

        cnt = 0
        nodes = []
        stnode = Node(0)
        ennode = Node(0)
        for i in range(len(s2)):
            for j in range(len(s2[i])):

                node = Node(s2[i][j])
                node.id = cnt
                node.gOfN = math.inf
                node.heuristicFn=math.inf
                node.value = s2[i][j]
                if i > 0:
                    node.up = cnt - len(s2[i])
                if i + 1 < len(s2):
                    node.down = cnt + len(s2[i])
                if j > 0:
                    node.left = cnt - 1

                if j + 1 < len(s2[i]):
                    node.right = cnt + 1
                if s2[i][j] == 'S':
                    stnode = node
                if s2[i][j] == 'E':
                    ennode = node
                cnt = cnt + 1
                nodes.append(node)

        row=len(s2[0])

        for i in range(len(nodes)):
            nodes[i].hOfN = self.eculidiandis(i, ennode.id, row)
        stnode = nodes[stnode.id]

        cost = self.ecost
        pq = PriorityQueue()
        stnode.heuristicFn = 0
        stnode.gOfN=0
        nodes[stnode.id]=stnode
        pq.put((stnode.heuristicFn, stnode.id))
        while pq:

            curnode = pq.get()
            curnode=nodes[curnode[1]]
            self.fullPath.append(curnode.id)
            if curnode.id == ennode.id:
                break
            if curnode.up != None and nodes[curnode.up].value != '#' and nodes[curnode.up].heuristicFn > curnode.gOfN+ cost[curnode.up]+ nodes[curnode.up].hOfN:
                nodes[curnode.up].heuristicFn = curnode.gOfN + nodes[curnode.up].hOfN+cost[curnode.up]
                nodes[curnode.up].gOfN = curnode.gOfN + cost[curnode.up]
                pq.put((nodes[curnode.up].heuristicFn, curnode.up))
                nodes[curnode.up].previousNode = curnode.id

            if curnode.down!= None and nodes[curnode.down].value != '#' and nodes[curnode.down].heuristicFn > curnode.gOfN + nodes[curnode.down].hOfN+cost[curnode.down]:
                nodes[curnode.down].heuristicFn = curnode.gOfN + nodes[curnode.down].hOfN+cost[curnode.down]
                nodes[curnode.down].gOfN = curnode.gOfN + cost[curnode.down]
                pq.put((nodes[curnode.down].heuristicFn, curnode.down))
                nodes[curnode.down].previousNode = curnode.id

            if curnode.left != None and nodes[curnode.left].value != '#' and nodes[curnode.left].heuristicFn > curnode.gOfN + nodes[curnode.left].hOfN+cost[curnode.left]:
                nodes[curnode.left].heuristicFn = curnode.gOfN + nodes[curnode.left].hOfN+cost[curnode.left]
                nodes[curnode.left].gOfN = curnode.gOfN + cost[curnode.left]
                pq.put((nodes[curnode.left].heuristicFn, curnode.left))
                nodes[curnode.left].previousNode = curnode.id

            if curnode.right != None and nodes[curnode.right].value != '#' and nodes[curnode.right].heuristicFn > curnode.gOfN +nodes[curnode.right].hOfN+cost[curnode.right]:
                nodes[curnode.right].heuristicFn = curnode.gOfN + nodes[curnode.right].hOfN+cost[curnode.right]
                nodes[curnode.right].gOfN = curnode.gOfN + cost[curnode.right]
                pq.put((nodes[curnode.right].heuristicFn, curnode.right))
                nodes[curnode.right].previousNode = curnode.id

        self.totalCost=nodes[ennode.id].heuristicFn
        return self.path, self.fullPath, self.totalCost

    def AStarManhattanHeuristic(self):
        # Cost for a step is 1
        # and use ManhattanHeuristic for evaluating the heuristic value
        # Fill the correct path in self.path
        # self.fullPath should contain the order of visited nodes
        self.path = []
        self.fullPath = []
        s1 = self.s
        s2 = []
        s3 = []
        for i in range(len(s1)):
            if s1[i] == ' ':
                s2.append(s3)
                s3 = []
            elif s1[i] != ',':
                s3.append(s1[i])

        s2.append(s3)

        cnt = 0
        nodes = []
        stnode = Node(0)
        ennode = Node(0)
        for i in range(len(s2)):
            for j in range(len(s2[i])):

                node = Node(s2[i][j])
                node.id = cnt
                node.gOfN = math.inf
                node.hOfN=math.inf
                node.heuristicFn=math.inf
                node.value = s2[i][j]
                if i > 0:
                    node.up = cnt - len(s2[i])
                if i + 1 < len(s2):
                    node.down = cnt + len(s2[i])
                if j > 0:
                    node.left = cnt - 1

                if j + 1 < len(s2[i]):
                    node.right = cnt + 1
                if s2[i][j] == 'S':
                    stnode = node
                if s2[i][j] == 'E':
                    ennode = node
                cnt = cnt + 1
                nodes.append(node)

        row=len(s2[0])

        for i in range(len(nodes)):
            nodes[i].hOfN = self.manhatandis(i, ennode.id, row)


        cost = self.ecost
        pq =[]
        stnode.heuristicFn = 0
        stnode.gOfN=0
        nodes[stnode.id]=stnode
        pq.append((stnode.heuristicFn, stnode.id))
        while pq:

            curnode =Node(0)
            mini=math.inf
            cnt=0
            id=-1
            for a,b in pq:

                if a<mini:
                    mini=a
                    curnode=nodes[b]
                    id=cnt
                cnt=cnt+1

            self.fullPath.append(curnode.id)
            pq.pop(id)

            if curnode.id == ennode.id:
                break
            if curnode.up != None and nodes[curnode.up].value != '#' and nodes[curnode.up].heuristicFn > curnode.gOfN+  nodes[curnode.up].hOfN+1:
                nodes[curnode.up].heuristicFn = curnode.gOfN + nodes[curnode.up].hOfN+1
                nodes[curnode.up].gOfN = curnode.gOfN + 1
                pq.append((nodes[curnode.up].heuristicFn, curnode.up))
                nodes[curnode.up].previousNode = curnode.id

            if curnode.down!= None and nodes[curnode.down].value != '#' and nodes[curnode.down].heuristicFn > curnode.gOfN + nodes[curnode.down].hOfN+1:
                nodes[curnode.down].heuristicFn = curnode.gOfN + nodes[curnode.down].hOfN+1
                nodes[curnode.down].gOfN = curnode.gOfN + 1
                pq.append((nodes[curnode.down].heuristicFn, curnode.down))
                nodes[curnode.down].previousNode = curnode.id

            if curnode.left != None and nodes[curnode.left].value != '#' and nodes[curnode.left].heuristicFn > curnode.gOfN + nodes[curnode.left].hOfN+1:
                nodes[curnode.left].heuristicFn = curnode.gOfN + nodes[curnode.left].hOfN+1
                nodes[curnode.left].gOfN = curnode.gOfN + 1
                pq.append((nodes[curnode.left].heuristicFn, curnode.left))
                nodes[curnode.left].previousNode = curnode.id

            if curnode.right != None and nodes[curnode.right].value != '#' and nodes[curnode.right].heuristicFn > curnode.gOfN +nodes[curnode.right].hOfN+1:
                nodes[curnode.right].heuristicFn = curnode.gOfN + nodes[curnode.right].hOfN+1
                nodes[curnode.right].gOfN = curnode.gOfN + 1
                pq.append((nodes[curnode.right].heuristicFn, curnode.right))
                nodes[curnode.right].previousNode = curnode.id

        self.totalCost=nodes[ennode.id].heuristicFn
        return self.path, self.fullPath, self.totalCost

def main():
    searchAlgo = SearchAlgorithms('S,.,.,#,.,.,. .,#,.,.,.,#,. .,#,.,.,.,.,. .,.,#,#,.,.,. #,.,#,E,.,#,.')
    path, fullPath = searchAlgo.DFS()
    print('**DFS**\nPath is: ' + str(path) + '\nFull Path is: ' + str(fullPath) + '\n\n')

                #######################################################################################

    searchAlgo = SearchAlgorithms('S,.,.,#,.,.,. .,#,.,.,.,#,. .,#,.,.,.,.,. .,.,#,#,.,.,. #,.,#,E,.,#,.')
    path, fullPath = searchAlgo.BFS()
    print('**BFS**\nPath is: ' + str(path) + '\nFull Path is: ' + str(fullPath) + '\n\n')
                #######################################################################################

    searchAlgo = SearchAlgorithms('S,.,.,#,.,.,. .,#,.,.,.,#,. .,#,.,.,.,.,. .,.,#,#,.,.,. #,.,#,E,.,#,.', [0, 15, 2, 100, 60, 35, 30, 3
                                                                                                             , 100, 2, 15, 60, 100, 30, 2
                                                                                                             , 100, 2, 2, 2, 40, 30, 2, 2
                                                                                                             , 100, 100, 3, 15, 30, 100, 2
                                                                                                             , 100, 0, 2, 100, 30])
    path, fullPath, TotalCost = searchAlgo.UCS()
    print('** UCS **\nPath is: ' + str(path) + '\nFull Path is: ' + str(fullPath) + '\nTotal Cost: ' + str(
        TotalCost) + '\n\n')
               #######################################################################################

    searchAlgo = SearchAlgorithms('S,.,.,#,.,.,. .,#,.,.,.,#,. .,#,.,.,.,.,. .,.,#,#,.,.,. #,.,#,E,.,#,.', [0, 15, 2, 100, 60, 35, 30, 3
                                                                                                             , 100, 2, 15, 60, 100, 30, 2
                                                                                                             , 100, 2, 2, 2, 40, 30, 2, 2
                                                                                                             , 100, 100, 3, 15, 30, 100, 2
                                                                                                             , 100, 0, 2, 100, 30])
    path, fullPath, TotalCost = searchAlgo.AStarEuclideanHeuristic()
    print('**ASTAR with Euclidean Heuristic **\nPath is: ' + str(path) + '\nFull Path is: ' + str(
        fullPath) + '\nTotal Cost: ' + str(TotalCost) + '\n\n')

            #######################################################################################

    searchAlgo = SearchAlgorithms('S,.,.,#,.,.,. .,#,.,.,.,#,. .,#,.,.,.,.,. .,.,#,#,.,.,. #,.,#,E,.,#,.')
    path, fullPath, TotalCost = searchAlgo.AStarManhattanHeuristic()
    print('**ASTAR with Manhattan Heuristic **\nPath is: ' + str(path) + '\nFull Path is: ' + str(
        fullPath) + '\nTotal Cost: ' + str(TotalCost) + '\n\n')


main()
