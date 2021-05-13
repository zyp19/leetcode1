import networkx as nx
def dfs(graph,node_start,max_step =10):
    assert max_step>=0 and node_start in graph.nodes()
    res_graph = nx.DiGraph()
    cur_step = 0
    stack_list = []
    visited = {}
    print(node_start)
    visited[node_start] ='1'
    