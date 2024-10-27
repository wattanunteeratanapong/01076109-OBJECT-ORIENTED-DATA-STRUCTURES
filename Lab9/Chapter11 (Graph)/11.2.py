# Chapter : 11 - item : 2 - Traversals

# รับ input เป็น list คู่ตัวเลข(เช่น A B.B C = A ไปหา B ได้ และ B ไปหา C ได้) ให้สร้าง Undirected Graph จากนั้นให้แสดงผล  graph  แบบ Depth First Traversals และ Bredth First Traversals โดยเริ่มต้นที่ vertex ที่น้อยที่สุด
# **หมายเหตุ**เนื่องจาก Depth First Traversal อาจมี solutions ที่แตกต่างกันเพื่อให้ได้ solution ที่เหมือนกัน จะกําหนดว่าถ้า traverse ไปได้หลาย node ให่ไป node ที่มีค่าน้อยที่สุดเสมอ
# *หากใครงงลองวาดรูปกราฟดูนะครับ*

# Test Case 1
# Enter : A B,B C,A D
# Depth First Traversals : A B C D
# Bredth First Traversals : A B D C

# Test Case 2
# Enter : A B,A D,A G,B E,B F,C F,C H,D F,E G
# Depth First Traversals : A B E G F C H D
# Bredth First Traversals : A B D G E F C H

# Test Case 3
# Enter : A B,A C,C D,D B
# Depth First Traversals : A B D C
# Bredth First Traversals : A B C D

# Test Case 4
# Enter : A B,D C
# Depth First Traversals : A B C D
# Bredth First Traversals : A B C D

def create_graph(pairs):
    graph = {}
    
    for pair in pairs.split(','):
        src, dest = pair.split()
        if src not in graph:
            graph[src] = []
        if dest not in graph:
            graph[dest] = []
        graph[src].append(dest)
        graph[dest].append(src)
    
    for node in graph:
        graph[node].sort()

    return graph

def dfs(graph, start):
    visited = []
    stack = [start]
    
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(sorted(graph[node], reverse=True))
    
    for node in sorted(graph.keys()):
        if node not in visited:
            visited.append(node)
            stack.extend(sorted(graph[node], reverse=True))
    
    return visited

def bfs(graph, start):
    visited = [start]
    queue = [start]
    
    while queue:
        node = queue.pop(0)
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)
    
    for node in sorted(graph.keys()):
        if node not in visited:
            visited.append(node)
            queue.append(node)
    
    return visited

inp = input("Enter : ")
graph = create_graph(inp)
start_node = min(graph.keys())

print("Depth First Traversals :", ' '.join(dfs(graph, start_node)))
print("Bredth First Traversals :", ' '.join(bfs(graph, start_node)))
