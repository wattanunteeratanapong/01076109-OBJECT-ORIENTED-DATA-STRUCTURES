# Chapter : 11 - item : 3 - shortest path

# รับ input เป็น list คู่อันดับ เพื่อนำไปสร้าง Directed Graph แบบมี weight จากนั้นให้แสดงผล shortest path โดยใช้ Dijkstra’s Shortest Path Algorithm
# เช่น A 3 B,B 1 C/A B,A C = สร้างกราฟที่ A ไปหา B ได้โดยมีweight=3 และ B ไปหา C ได้โดยมีweight=1 / แสดง shortest path จากA>BและA>C) 

# Test Case 1
# Enter : v0 1 v1,v1 1 v2,v2 1 v3,v0 1 v3/v0 v1,v0 v2,v0 v3
# v0 to v1 : v0->v1
# v0 to v2 : v0->v1->v2
# v0 to v3 : v0->v3

# Test Case 2
# Enter : A 1 B,A 2 C,B 1 C/A C
# A to C : A->C

# Test Case 3
# Enter : A 1 B,C 1 D/A C,B C
# Not have path : A to C
# Not have path : B to C

# Test Case 4
# Enter : v0 1 v1,v1 2 v2,v0 1 v2,v1 1 v3,v2 4 v3,v3 1 v4/v0 v3,v0 v4,v1 v4,v5 v6
# v0 to v3 : v0->v1->v3
# v0 to v4 : v0->v1->v3->v4
# v1 to v4 : v1->v3->v4
# Not have path : v5 to v6

# Test Case 5
# Enter : v0 2 v1,v0 1 v3,v1 3 v3,v1 10 v4,v2 4 v0,v2 5 v5,v3 2 v2,v3 2 v4,v3 8 v5,v3 4 v6,v4 6 v6, v6 1 v5/v0 v1,v0 v2,v0 v3,v0 v4,v0 v5,v0 v6
# v0 to v1 : v0->v1
# v0 to v2 : v0->v3->v2
# v0 to v3 : v0->v3
# v0 to v4 : v0->v3->v4
# v0 to v5 : v0->v3->v6->v5
# v0 to v6 : v0->v3->v6

def create_graph(pairs):
    graph = {}
    
    for pair in pairs.split(','):
        src, weight, dest = pair.split()
        if src not in graph:
            graph[src] = []
        if dest not in graph:
            graph[dest] = []
        graph[src].append((dest, int(weight)))

    return graph

def dijkstra(graph, start, end):
    if start not in graph or end not in graph:
        return None
    
    unvisited = set(graph.keys())
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    previous_nodes = {node: None for node in graph}
    
    while unvisited:
        current_node = min(unvisited, key=lambda node: distances[node])
        unvisited.remove(current_node)
        
        if distances[current_node] == float('inf'):
            break
        
        for neighbor, weight in graph[current_node]:
            tentative_distance = distances[current_node] + weight
            if tentative_distance < distances[neighbor]:
                distances[neighbor] = tentative_distance
                previous_nodes[neighbor] = current_node
    
    path = []
    current = end
    while previous_nodes[current] is not None:
        path.insert(0, current)
        current = previous_nodes[current]
    if path:
        path.insert(0, start)
    
    return path if path else None

def shortest_paths(graph, queries):
    for query in queries.split(','):
        start, end = query.split()
        path = dijkstra(graph, start, end)
        if path:
            print(f"{start} to {end} : {'->'.join(path)}")
        else:
            print(f"Not have path : {start} to {end}")

inp = input("Enter : ")
graph_data, query_data = inp.split('/')
graph = create_graph(graph_data)
shortest_paths(graph, query_data)
