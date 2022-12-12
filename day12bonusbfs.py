# making the graph
# dictionary, every node has a key, and the value is a list of every node that you can travel to from your current node
graph = {
        0:[1,3],
        1:[2,0],
        2:[1],
        3:[0,7,4],
        4:[3,7,6,5],
        5:[4,5],
        6:[7,4,5],
        7:[3,4,6]
}

# import double ended queue
from collections import deque

# define start and ending nodes
start = 0
end = 7

# create the deque with the initial starting state
# current-node , steps-taken
q = deque(  [ (start, 0) ]  )

# create visited set to save checking the same node more than once
visited = set()


# while there are states to check
while q:
    # pop the leftmost state 
    pos, steps = q.popleft()

    # check if you've reached the goal
    if pos == end:
        print(steps)
        break

    # check you've not visisted this node before
    if pos in visited:
        continue

    visited.add(pos)

    # add every possible state based off my current state to the queue
    for node in graph[pos]:
        q.append( (node, steps + 1) )

























