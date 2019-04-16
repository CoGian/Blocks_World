import sys
import os
import time
import search as s
from block_state import BlockState
from utils import parse_file


def main():
    """
     sm = sys.argv[1].lower()

    file_name = sys.argv[2]

    """
    data_folder = os.path.join("input_files")

    file_to_open = os.path.join(data_folder, "probBLOCKS-8-0.pddl.txt")
    with open(file_to_open, 'r') as f:

        objects, begin_config, goal_config = parse_file(f)

        print(objects)
        print(begin_config)
        print("goal" , goal_config)

        state = BlockState(begin_config, len(begin_config), objects)
        start_time = time.time( )

        state, nodes, max_depth = s.a_star_search(state, goal_config)
        print(state.config)
        moves, intmoves, valid = s.calculate_path_to_goal(state)
        print(moves )
        print( intmoves , nodes)
        print(time.time()-start_time)
        if valid:
            print('valid')



    '''
    if sm == "bfs":

      pass

    elif sm == "dfs":

        pass

    elif sm == "ast":

        pass
    else:

        print("Enter valid command arguments !")
    '''


if __name__ == '__main__':
    main( )
