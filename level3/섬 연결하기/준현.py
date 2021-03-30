

parent = {}
rank = {}

def make_set(v):
    parent[v] = v
    rank[v] = 0
def find(v):
    if parent[v] == v:
        return v
    parent[v] = find(parent[v])            
    return parent[v]
def union(v, u):
    root1 = find(v)
    root2 = find(u)
    
    if root1 != root2:

        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            
            if rank[root1] == rank[root2]:
                rank[root2] += 1

def solution(n, costs):
    for v in range(n):
        make_set(v)
    answer=0
    costs=sorted(costs,key=lambda x:x[2])
    
    for edge in costs:
        v, u, weight = edge
                
        if find(v) != find(u):
            union(v, u)
            answer+=weight
    
    return answer


n=4
costs=[[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]
print(solution(n,costs))
