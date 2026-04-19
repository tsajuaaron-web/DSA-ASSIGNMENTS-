from collections import deque # Unit 2: Queue for BFS
from sorting import merge_sort

def bfs_shortest_path(graph, start, end):
    if start not in graph or end not in graph: return []
    queue = deque([[start]])
    visited = {start}
    
    while queue:
        path = queue.popleft()
        node = path[-1]
        if node == end: return path
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
    return []

def dfs_depth_limited(graph, start, depth, visited=None):
    if visited is None: visited = set()
    if depth < 0 or start not in graph: return set()
    
    results = {start}
    visited.add(start)
    if depth > 0:
        for neighbor in graph[start]:
            if neighbor not in visited:
                # Recursive discovery
                results.update(dfs_depth_limited(graph, neighbor, depth - 1, visited.copy()))
    return results

def suggest_friends(user_id, pm, fn):
    user = pm.get_user(user_id)
    if not user: return []
    
    friends = set(fn.get_friends(user_id))
    candidates = []
    
    for other_id, other_user in pm.profiles.items():
        if other_id != user_id and other_id not in friends:
            # Score = number of common interests
            score = len(set(user.interests) & set(other_user.interests))
            if score > 0:
                candidates.append((other_id, score))
    
    # Unit 3: Use custom Merge Sort
    sorted_candidates = merge_sort(candidates)
    return sorted_candidates[:5]