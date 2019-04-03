from frontier_and_explored import Frontier, Explored
from block_state import BlockState
import heapq


# TODO : ADD MORE COMMENTS FOR GOD'S SHAKE
def bfs_search(initial_state: BlockState, goal_config):
    """BFS search"""

    # initialize frontier and explored
    frontier = Frontier()
    frontier.queue.append(initial_state)

    # frontier_configs is used just to search
    frontier_configs = set()
    frontier_configs.add(initial_state.config)
    explored = Explored()

    max_depth = 0
    nodes = 0
    while frontier.queue:
        state = frontier.queue.popleft()
        frontier_configs.remove(state.config)
        explored.set.add(state.config)

        # check if this state is goal state
        if state.config == goal_config:
            print("SUCCESS")
            return state, nodes, max_depth

        "expand the node"
        state.expand()
        nodes = nodes + 1
        print(nodes)
        for child in state.children:
            "check for duplicates in frontier and explored"
            if max_depth < child.cost:
                max_depth += 1
            if child.config not in explored.set and child.config not in frontier_configs:
                frontier.queue.append(child)
                frontier_configs.add(child.config)
    print('FAILURE')
    exit()


def dfs_search(initial_state: BlockState, goal_config):
    """DFS search"""

    # initialize frontier and explored
    frontier = Frontier()
    frontier.stack.append(initial_state)
    frontier_configs = set()
    frontier_configs.add(initial_state.config)
    explored = Explored()

    max_depth = 0
    nodes = 0
    while frontier.stack:
        state = frontier.stack.pop()
        frontier_configs.remove(state.config)

        if state.config not in explored.set:
            explored.set.add(state.config)

            if max_depth < state.cost:
                max_depth += 1

            # check if this state is goal state
            if state.config == goal_config:
                print("SUCCESS")
                return state, nodes, max_depth

            "expand the node"

            state.expand( )

            # reverse children to put it in frontier with the same priority as bfs
            state.children = state.children[::-1]
            nodes = nodes + 1
            print(nodes)
            for child in state.children:
                "check for duplicates in frontier and explored"
                if max_depth < child.cost:
                    max_depth += 1

                if child.config not in frontier_configs :
                    frontier.stack.append(child)
                    frontier_configs.add(child.config)
    print('FAILURE')
    exit()


def a_star_search(initial_state, goal_config):
    """A * search"""

    frontier = Frontier()  # list of entries arranged in a heap
    entry_finder = {}  # mapping of states to entries

    initial_state.f = h(initial_state.config, goal_config)
    entry = (initial_state.f, initial_state)
    entry_finder[initial_state.config] = entry
    heapq.heappush(frontier.heap, entry)

    explored = Explored()

    max_depth = 0
    nodes = 0

    while frontier.heap:

        state = heapq.heappop(frontier.heap)
        del entry_finder[state[1].config]
        explored.set.add(state[1].config)

        if state[1].config == goal_config:
            print("SUCCESS")
            return state[1], nodes, max_depth

        "expand the node"

        state[1].expand()

        nodes = nodes + 1
        print(nodes)
        for child in state[1].children:
            "check for duplicates in frontier and explored"
            child.f = child.cost + h(child.config, goal_config)
            if max_depth < child.cost:
                max_depth += 1

            entry = (child.f, child)
            if child.config not in explored.set and child.config not in entry_finder:

                entry_finder[child.config] = entry
                heapq.heappush(frontier.heap, entry)

            elif child.config in entry_finder and child.f < entry_finder[child.config][0]:

                index = frontier.heap.index((entry_finder[child.config][1].f, entry_finder[child.config][1]))

                frontier.heap[int(index)] = entry

                entry_finder[child.config] = entry

                heapq.heapify(frontier.heap)
    print('FAILURE')
    exit()


def h(config, goal_config):
    cost = 0
    index = 0
    for cube in config :

        if cube[0] != goal_config[index][0] :
            cost += 1
        if cube[1] != goal_config[index][1] :
            cost += 1
        index += 1
    return cost


def calculate_path_to_goal(state):
    """calculate the path to goal"""
    moves = list()

    while state.parent is not None:
        moves.append(state.action)
        state = state.parent

    moves = moves[::-1]

    return str(moves) , len(moves)
