from collections import defaultdict


#function to check whether a graph is a clique(complete)
def is_Clique(graph):
    v = len(graph.keys())               #no_of_vertices
    count = 0
    for x in graph:
        if isinstance(graph[x],list):
            count += len(graph[x])
    e = count // 2                      #no_of_edges
    a = (v * (v - 1)) / 2
    if e == a:
        return 1
    else:
        return 0

#function that inputs a graph and returns a list of strict corners
def strict_corners(graph):
    sC = []
    for i in graph.keys():
        for j in graph.keys():
            if len(graph[j]) > len(graph[i]) and i not in sC:       #strict_corner condition
                if all(x in graph[j] for x in graph[i]):            #checking whether it is a subset
                    sC.append(i)
    return sC

#function to calculate neighbourhood of a graph
def neigh(graph):
    graph1 = {}
    for i in graph.keys():
        graph1[i] = graph[i].copy()
    for i in graph1.keys():
        graph1[i].append(i)
    return graph1

def addEdge(graph,u,v):
    graph[u].append(v)

def main():
    graph = defaultdict(list)
    neighbourhood = {}
    graph1 = {}
    cr = {}

    #change the path corresponding to your system

    filename = "D:\DAA\Package\sample1.txt"
    #filename = "D:\DAA\Package\sample2.txt"
    
    with open(filename) as inFile:
        n = inFile.readline()
        for i in range(int(n)*2):
            e = inFile.readline().rstrip()
            e = e.split(" ")
            addEdge(graph,e[0],e[1])
    inFile.close()
        
    

    for i in graph.keys():
        graph1[i] = graph[i].copy()


    #corenr-ranking procedure
    k = 1
    while 1:
        neighbourhood = neigh(graph1)
        s = strict_corners(neighbourhood)
        if is_Clique(graph1):
            for i in graph1:
                cr[i] = k
            break
        elif is_Clique(graph1) == 0 and s == []:
            for i in graph1:
                cr[i] = -1
            break
        else:
            for i in s:
                cr[i] = k
                del graph1[i]
            for j in graph1.keys():                   #removing the strict corners from the graph
                difference = set(graph1[j]) - set(s)
                graph1[j] = list(difference)
            k = k + 1

    print("Corner Rank of vertices:")
    for i in cr.keys():
        print(i,": ",cr[i])
    print("\n\n")
    

    #corner rank of the graph
    c = 0
    for i in cr.keys():
        if(c==0):
            maxi = cr[i]
            c = c + 1
        if(cr[i]==-1):
            maxi = -1
            break
        if(cr[i] > maxi):
            maxi = cr[i]

    #deciding if the graph is cop-win or not         
    if(maxi > 0):
        print("Graph is COP-WIN!!!")
        min_cops = list(cr.values())
        print("Minimum no. of cops needed to win : ",min(min_cops))
    else:
        print("Graph is NON COP-WIN")

    
    

main()


