from collections import deque

#广度优先算法
class BFS:
    graph = {}
    def __init__(self):
        self.graph["you"] = ["alice", "bob", "claire"]

        self.graph["alice"] = ["peggy"]
        self.graph["bob"] = ["anuj", "peggy"]
        self.graph["claire"] = ["thom", "jonny"]

        self.graph["peggy"] = []
        self.graph["anuj"] = []
        self.graph["thom"] = []
        self.graph["jonny"] = []

    def findSeller(self):
        searched = []
        search_queue = deque()
        search_queue += self.graph["you"]
        while search_queue:
            person = search_queue.popleft()
            if person not in search_queue:
                if self.__person_is_seller__(person):
                    return person
                else:
                    search_queue += self.graph[person]
                    searched.append(person)
        return None

    def __person_is_seller__(self,name):
        return name[-1] == 'm'

#狄克斯特拉算法算法
class Dijkstraalgorithm:
    #需要实现的图，定义图的散列表
    graph = {}
    #定义一个散列表用来存储每个节点的开销
    infinity = float("inf")
    costs={}
    #定义一个散列表用来存储父节点
    parents={}
    #定义一个数组用于记录处理过的节点
    processed=[]

    def __init__(self):
        #初始化定义加权图
        self.graph["start"]={}

        self.graph["start"]["A"]=6
        self.graph["start"]["B"]=2

        self.graph["A"]={}
        self.graph["A"]["fin"]=1

        self.graph["B"]={}
        self.graph["B"]["A"]=3
        self.graph["B"]["fin"]=5

        self.graph["fin"]={}
        #初始化定义节点开销
        self.costs["A"]=6
        self.costs["B"]=2
        self.costs["fin"]=self.infinity
        #初始化定义父节点
        self.parents["A"] = "start"
        self.parents["B"] = "start"
        self.parents["fin"] = None

    def __find_lowest_cost_node__(self):
        lowest_cost=float("inf")
        lowest_cost_node = None
        for node in self.costs:
            cost =self.costs[node]
            if cost < lowest_cost and node not in self.processed:
                lowest_cost=cost
                lowest_cost_node= node
        return lowest_cost_node

    def findResoult(self):
        node=self.__find_lowest_cost_node__()
        while node is not None:
            cost=self.costs[node]
            neighbors=self.graph[node]
            for n in  neighbors.keys():
                new_cost = cost+neighbors[n]
                if self.costs[n] > new_cost:
                    self.costs[n]=new_cost
                    self.parents[n]=node
            self.processed.append(node)
            node=self.__find_lowest_cost_node__()
    def dumpFormatData(self):
        node="fin"
        route=[]
        while node is not None:
            route.append(node)
            if node in self.parents.keys():
                node=self.parents[node]
            else:
                node = None
        stringroute=""
        while 0 != len(route):
            stringroute+=route.pop()
            if 0 != len(route):
                stringroute+="--->"
        print("从起点到终点的路径为:",stringroute)

        for node in self.costs.keys():
            print("从起点到",node,"点的最低花费为：",self.costs[node])

#近似算法
class ApproximationAlgorithm:
    states_needed = set(['陕西','广东','湖南','北京','上海','新疆','江苏','湖北'])#set 传入一个数组，它被转换为一个集合，集合不能包含重复元素，
    final_stations = set()
    stations={}

    def __init__(self):
        self.stations["爷爷电视台"]=set(['北京','上海','新疆'])
        self.stations["奶奶电视台"]=set(['广东','北京','陕西'])
        self.stations["帅帅电视台"]=set(['湖南','上海','江苏'])
        self.stations["俊俊电视台"]=set(['上海','新疆'])
        self.stations["蛋蛋电视台"]=set(['江苏','湖北'])

    def FindBestSoultion(self):
        while self.states_needed:
            beststation = None
            states_covered = set()  # 一个集合，包含该广播电台覆盖的所有未覆盖的省市地区
            for station, states_for_station in self.stations.items():
                covered = self.states_needed & states_for_station #这个语法是计算两个集合的交集
                if len(covered) > len(states_covered):
                    beststation=station
                    states_covered=covered

            self.states_needed -= states_covered
            self.final_stations.add(beststation)
        print (self.final_stations)