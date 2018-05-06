import networkx as nx
from collections import deque
def BFS_visit(i,G = nx.Graph(),visit_time = [],pre = []):
    global time #定义计时的全局变量
    visit_list = deque() #双端队列
    visit_list.append(i) #将图中的一个节点i放入双端队列中
    while visit_list:
        visit = visit_list.popleft()
        
