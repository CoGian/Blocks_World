from frontier_and_explored import Frontier, Explored
from block_state import BlockState
import heapq
import re


# TODO : ADD MORE COMMENTS FOR GOD'S SHAKE
def bfs_search(initial_state: BlockState, goal_config):
    """BFS search"""

    # initialize frontier and explored
    frontier = Frontier().queue
    frontier.append(initial_state)

    # frontier_configs is used just to search
    frontier_configs = set()
    frontier_configs.add(initial_state.config)
    explored = Explored().set

    max_depth = 0
    nodes = 0
    while frontier:
        state = frontier.popleft()
        frontier_configs.remove(state.config)
        explored.add(state.config)

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
            if child.config not in explored and child.config not in frontier_configs:
                frontier.append(child)
                frontier_configs.add(child.config)
    print('FAILURE')
    exit()


def dfs_search(initial_state: BlockState, goal_config):
    """DFS search"""

    # initialize frontier and explored
    frontier = Frontier().stack
    frontier.append(initial_state)
    frontier_configs = set()
    frontier_configs.add(initial_state.config)
    explored = Explored().set

    max_depth = 0
    nodes = 0
    while frontier:
        state = frontier.pop()
        frontier_configs.remove(state.config)

        if state.config not in explored:
            explored.add(state.config)

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
                    frontier.append(child)
                    frontier_configs.add(child.config)
    print('FAILURE')
    exit()


def a_star_search(initial_state, goal_config):
    """A * search"""

    frontier = Frontier().heap  # list of entries arranged in a heap
    entry_finder = {}  # mapping of states to entries

    initial_state.f = h(initial_state.config, goal_config)
    add_state(initial_state, entry_finder, frontier)

    explored = Explored().set

    max_depth = 0
    nodes = 0

    while frontier:

        state = pop_state(frontier, entry_finder)

        if state.config not in explored:
            explored.add(state.config)

            if state.config == goal_config:
                print("SUCCESS")
                return state, nodes, max_depth

            "expand the node"

            state.expand()

            nodes = nodes + 1
            print(nodes)
            for child in state.children:
                "check for duplicates in frontier and explored"
                child.f = child.cost + h(child.config, goal_config)
                if max_depth < child.cost:
                    max_depth += 1

                if child.config not in entry_finder:

                    add_state(child, entry_finder, frontier)

                elif child.f < entry_finder[child.config][0]:

                    remove_state(child.config, entry_finder)
                    add_state(child, entry_finder, frontier)

    print('FAILURE')
    exit()


def add_state(state, entry_finder, frontier):
    'Add a new task or update the priority of an existing task'
    if state.config in entry_finder:
        remove_state(state.config)
    entry = [state.f, state]
    entry_finder[state.config] = entry
    heapq.heappush(frontier, entry)


def remove_state(config, entry_finder):
    'Mark an existing task as REMOVED.  Raise KeyError if not found.'
    entry = entry_finder.pop(config)
    entry[-1] = '<removed-task>'


def pop_state(frontier,entry_finder):
    'Remove and return the lowest priority task. Raise KeyError if empty.'
    while frontier:
        state = heapq.heappop(frontier)
        if state[1] != '<removed-task>':
            del entry_finder[state[1].config]
            return state[1]


def h(config, goal_config):
    cost = 0
    index = 0
    for cube in config :

        if cube[0] != goal_config[index][0]:
            cost += 1
        index += 1
    return cost


def calculate_path_to_goal(state):
    """calculate the path to goal and check if solution is valid"""
    moves = list()
    config = list(map(list,state.config))
    objects = state.objects
    while state.parent is not None:
        moves.append(state.action)

        action = re.split("[(,)]", state.action)
        # initialize
        movedcube = objects.index(action[1])
        prevplace = action[2]
        currplace = action[3]

        # if previous place is table change the state of current place to clear (-1) and the state of moved cube to
        # on table(-1)
        if prevplace == 'table':
            config[objects.index(currplace)][0] = -1
            config[movedcube][1] = -1
        # if else  current place is table change the state of previous place to bellow of moved cube
        # and the state of moved cube to above previous place
        elif currplace == 'table':
            config[objects.index(prevplace)][0] = movedcube
            config[movedcube][1] = objects.index(prevplace)
        # else change the state of current place to clear(-1) , the state of previous place to bellow moved cube
        # and the state of moved cube to above previous place
        else:
            config[objects.index(currplace)][0] = -1
            config[objects.index(prevplace)][0] = movedcube
            config[movedcube][1] = objects.index(prevplace)
        state = state.parent

    moves = moves[::-1]

    return str(moves), len(moves), config == list(map(list, state.config))
