edgeLinks =dict()
size =0
stack = []

def addEdge(a,b):
    global edgeLinks
    if a not in edgeLinks:
        edgeLinks[a] = set()
    if b not in edgeLinks:
        edgeLinks[b] = set()
def check(graph,s,e,path = []):
    path = path+[s]
    if s==e:
        return [path]
    path = []
    for node in graph[s]:
        if node not in path:
            ns = check(graph,node,e,path)
            for n in ns:
                path.append(n)
    return path

if __name__ == '__main__':
    f = open("tu", "r")
    # n = int(sys.stdin.readline().strip())
    n= int(f.readline().strip())
    for i in range(n):
        # size,edgeCount = map(int,sys.stdin.readline().strip())
        size, edgeCount = map(int,f.readline().split())
        for j in range(edgeCount):
            # a,b = sys.stdin.readline().strip()
            a, b = f.readline().split()
            addEdge(a,b)
            allpath = check(edgeLinks,a,b)
        for m in range(1,len(allpath)):
            while allpath[m] and allpath[m-1]:
                while allpath[m][i] < allpath[m][i]:
                    continue
                continue
            print(allpath(m))








