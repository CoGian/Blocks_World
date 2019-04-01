from frontier_and_explored import Frontier, Explored
from block_state import BlockState

# TODO : ADD MORE COMMENTS FOR GOD'S SHAKE
def bfs_search(initial_state: BlockState, method, goal_config):
    """BFS search"""

    frontier = Frontier(method)
    frontier.queue.append(initial_state)

    explored = Explored()

    max_depth = 0
    nodes = 0
    while frontier.queue:
        state = frontier.queue.popleft()
        explored.set.add(state.config)
        if state.config == goal_config:
            print("SUCCESS")
            return state, nodes, max_depth

        "expand the node"
        state.expand()
        children = state.children
        nodes = nodes + 1

        for child in children:
            "check for duplicates in frontier and explored"
            if max_depth < child.cost:
                max_depth += 1
            if child.config not in explored.set and child not in frontier:
                frontier.queue.append(child)
    print('FAILURE')
    exit()

# TODO : SEE HOW CHILDREN ARE EXPANDED
def dfs_search(initial_state: BlockState, method, goal_config):
    """DFS search"""

    frontier = Frontier(method)
    frontier.stack.append(initial_state)

    explored = Explored()

    max_depth = 0
    nodes = 0
    while frontier.stack:
        state = frontier.stack.pop()
        explored.set.add(state.config)

        if max_depth < state.cost:
            max_depth += 1
        if state.config == goal_config:
            print("SUCCESS")
            return state, nodes, max_depth

        "expand the node"

        children = state.expand()
        children = children[::-1]
        nodes = nodes + 1

        for child in children:
            "check for duplicates in frontier and explored"
            if max_depth < child.cost:
                max_depth += 1
            if child.config not in explored.set and child not in frontier:
                frontier.stack.append(child)
    print('FAILURE')
    exit()


def calculate_path_to_goal(state):
    """calculate the path to goal"""
    moves = list()

    while state.parent is not None:
        moves.append(state.action)
        state = state.parent

    moves = moves[::-1]

    return str(moves)
