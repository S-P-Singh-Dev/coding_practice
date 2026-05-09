# Course Schedule II
# Difficulty: Medium
# Topic: Graph
# Time: O(V + E) where V is the number of courses and E is the number of prerequisites. | Space: O(V + E) for the graph representation and the indegree array.
#
# Approach:
# Use topological sorting to determine the order of courses. Utilize BFS or DFS to explore dependencies and track courses. Maintain an indegree array to process nodes with zero dependencies first.
#
# Solution:

from collections import defaultdict, deque

def findOrder(numCourses, prerequisites):
    graph = defaultdict(list)
    indegree = [0] * numCourses
    
    for course, prereq in prerequisites:
        graph[prereq].append(course)
        indegree[course] += 1
    
    queue = deque([i for i in range(numCourses) if indegree[i] == 0])
    order = []
    
    while queue:
        course = queue.popleft()
        order.append(course)
        
        for neighbor in graph[course]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    
    return order if len(order) == numCourses else []
