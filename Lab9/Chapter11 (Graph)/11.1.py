# Chapter : 11 - item : 1 - ฝึกสร้าง graph

# รับ input เป็น list คู่อันดับ(เช่น A B,B C = A ไปหา B ได้ และ B ไปหา C ได้) ให้สร้าง Directed Graph จากนั้นให้แสดงผล adjacency metrix ของ graph 

# Test Case 1
# Enter : A B,A C,C D,D B
#     A  B  C  D
# A : 0, 1, 1, 0
# B : 0, 0, 0, 0
# C : 0, 0, 0, 1
# D : 0, 1, 0, 0

# Test Case 2
# Enter : A B,C D,E F,A C,A D,H G
#     A  B  C  D  E  F  G  H
# A : 0, 1, 1, 1, 0, 0, 0, 0
# B : 0, 0, 0, 0, 0, 0, 0, 0
# C : 0, 0, 0, 1, 0, 0, 0, 0
# D : 0, 0, 0, 0, 0, 0, 0, 0
# E : 0, 0, 0, 0, 0, 1, 0, 0
# F : 0, 0, 0, 0, 0, 0, 0, 0
# G : 0, 0, 0, 0, 0, 0, 0, 0
# H : 0, 0, 0, 0, 0, 0, 1, 0

# Test Case 3
# Enter : A B,1 2,C B,3 2
#     1  2  3  A  B  C
# 1 : 0, 1, 0, 0, 0, 0
# 2 : 0, 0, 0, 0, 0, 0
# 3 : 0, 1, 0, 0, 0, 0
# A : 0, 0, 0, 0, 1, 0
# B : 0, 0, 0, 0, 0, 0
# C : 0, 0, 0, 0, 1, 0

def create_graph(pairs):
    nodes = set()
    edges = []
    
    for pair in pairs.split(','):
        src, dest = pair.split()
        nodes.add(src)
        nodes.add(dest)
        edges.append((src, dest))
    
    nodes = sorted(nodes)
    
    node_index = {node: i for i, node in enumerate(nodes)}
    
    n = len(nodes)
    adj_matrix = [[0] * n for _ in range(n)]
    
    for src, dest in edges:
        i = node_index[src]
        j = node_index[dest]
        adj_matrix[i][j] = 1
    
    print("   ", "  ".join(nodes))
    for i, node in enumerate(nodes):
        row = ', '.join(map(str, adj_matrix[i]))
        print(f"{node} : {row}")

inp = input("Enter : ")
create_graph(inp)
