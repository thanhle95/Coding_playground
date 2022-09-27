"""
A supply chain manager at Amazon Logistics wants to determine the number of connetions between warehouses,
represented as nodes on a grid. A grid with m rows and n columns is used to form a cluster nodes. 
If a point in the grid has a value of 1, then it represent a node.

Each node in the cluster has a level associated with it. Anode located in the ith row of the grid is a level in node.

Here are the rules for creating a cluster:
    - Every node at a level connects to the next level that contains at least 1 node
    (i.e, every node at level i connects to all the nodes at level k where k > i 
    and k is the first level after level i than contains at least one node).
    - When i reaches the last level in the grid, no more connections are possible.

Given such a grid, please help the supply chain manager by finding the number of connections present in the cluster
"""


## Input
#   grid: the nodes grid

## Output:
#   the total number of connetion 

"""
Example 1:
Input : grid = [[1,1,1],
                [0,1,0],
                [0,0,0],
                [1,1,0]]

Output : 5

"""

def gridOfNode(intervals: list[list[int]]) -> int:
    connection = 0
    pre_node = 1
    for i in range(len(intervals)):
        curr_node_count = 0
        for j in range(len(intervals[0])):
            if intervals[i][j] == 1:
                curr_node_count += 1
        if i == 0:
            pre_node = curr_node_count
            continue
        elif curr_node_count >= 1:
            connection += curr_node_count * pre_node
            pre_node = curr_node_count
    return connection


print(gridOfNode([[1,1,1,1],
                [0,0,0,1],
                [1,1,0,1],
                [0,0,1,0]]))