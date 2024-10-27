# Chapter : 11 - item : 5 - หาลูปในกราฟ

# ให้เขียนฟังก์ชั่นหา loop ใน directed กราฟ และแสดงผลตามตัวอย่าง

# Test Case 1
# Enter : 0 1,1 2,2 3
# Graph has no cycle

# Test Case 2
# Enter : 0 1,1 2,2 0
# Graph has a cycle

# Test Case 3
# Enter : 0 1,1 2,2 3,3 4,4 5,5 6,6 7,7 8,8 9,9 8
# Graph has a cycle

def create_graph(pairs):
    graph = {}
    
    for pair in pairs.split(','):
        src, dest = pair.split()
        if src not in graph:
            graph[src] = []
        graph[src].append(dest)

    return graph

def dfs_cycle(graph, node, visited, rec_stack):
    visited.add(node)
    rec_stack.add(node)

    if node in graph:
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs_cycle(graph, neighbor, visited, rec_stack):
                    return True
            elif neighbor in rec_stack:
                return True

    rec_stack.remove(node)
    return False

def has_cycle(graph):
    visited = set()
    rec_stack = set()

    for node in graph:
        if node not in visited:
            if dfs_cycle(graph, node, visited, rec_stack):
                return True

    return False

inp = input("Enter : ")
graph = create_graph(inp)

if has_cycle(graph):
    print("Graph has a cycle")
else:
    print("Graph has no cycle")

