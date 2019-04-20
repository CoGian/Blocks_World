import sys
import os
import search as s
from block_state import BlockState
from utils import parse_file, write_in_file

"""Usage : python bw.py <method> <problem file> <solution file>"""


def main():
    try:
        sm = sys.argv[1].lower()
        file_to_read = sys.argv[2]
        file_to_write = sys.argv[3]
    except IndexError:
        print("Enter valid command arguments !Usage : python bw.py <method> <problem file> <solution file>")
        exit(0)

    data_folder = os.path.join("input_files")

    file_to_open = os.path.join(data_folder, file_to_read)
    try:
        with open(file_to_open, 'r') as f:

            objects, begin_config, goal_config = parse_file(f)

            initial_state = BlockState(begin_config, len(begin_config), objects)
            if sm == "breadth":
                state, nodes, max_depth, running_time = s.bfs_search(initial_state, goal_config)
            elif sm == "depth":
                state, nodes, max_depth, running_time = s.dfs_search(initial_state, goal_config)
            elif sm == "best":
                state, nodes, max_depth, running_time = s.best_first_search(initial_state, goal_config)
            elif sm == "astar":
                state, nodes, max_depth, running_time = s.a_star_search(initial_state, goal_config)
            else:
                print("Enter valid command arguments !Usage : python bw.py <method> <problem file> <solution file>")
                exit(0)

            moves = s.calculate_path_to_goal(state)
            write_in_file(moves, file_to_write)

            print("cost_of_path:", state.cost)
            print("nodes_expanded:", nodes)
            print("max_search_depth:", max_depth)
            print("running_time:", running_time)

            valid = s.is_valid(initial_state, moves, goal_config)
            if valid:
                print('valid_solution: true')
            else:
                print('valid_solution: false')
    except EnvironmentError:
        print("File not found!")


if __name__ == '__main__':
    main()
