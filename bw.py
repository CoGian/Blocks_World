import sys
import re
import search as s
from block_state import BlockState


# alter configs from plain text to coded list
# Values in config will be
# -1 = cube is clear OR
# j = cube i has the cube j over it
def create_config(objects, state_in_text):

    config = []

    # initialize all cubes with -1
    for i in range(len(objects)):
        config.append(-1)

    for text in state_in_text:
        tokens = re.split('[ ]', text)
        if tokens[0] == 'ON':
            index1, index2 = objects.index(tokens[1]), objects.index(tokens[2])
            config[index2] = index1

    return tuple(config)


def parse_file(file):
    # read objects till find the line with init

    while True:
        line = file.readline( )
        if "objects" in line:
            break

    objects = re.split("[ \n]", line)

    while True:
        line = file.readline( )
        if ":INIT" not in line:
            objects.extend(re.split("[ \n)]", line))
        else:
            break

    # trim objects
    objects.remove("(:objects")
    while '' in objects:
        objects.remove('')

    while ')' in objects:
        objects.remove(')')

    print(objects)
    # read initial state till find line with goal
    init = re.split('[()\n]', line)

    while True:
        line = file.readline( )
        if ":goal" not in line:
            init.extend(re.split('[()\n]', line))
        else:
            break

    # trim init
    while '' in init:
        init.remove('')

    for text in init:
        if text.isspace():
            init.remove(text)
    init.remove(":INIT ")
    init.remove('HANDEMPTY')
    print(init)

    # read goal state till find line with EOF
    goal = re.split('[()\n]', line)

    while True:
        line = file.readline( )
        if not line:
            break
        else:
            goal.extend(re.split('[()\n]', line))

    # trim goal
    goal.remove(':goal ')
    goal.remove('AND ')

    while '' in goal:
        goal.remove('')

    for text in goal:
        if text.isspace():
            goal.remove(text)
    print(goal)

    begin_config = create_config(objects, init)
    goal_config = create_config(objects, goal)

    return objects, begin_config, goal_config


def main():
    """
     sm = sys.argv[1].lower()

    file_name = sys.argv[2]

    """

    file = open('probBLOCKS-4-0.pddl.txt', 'r')

    objects, begin_config, goal_config = parse_file(file)

    print(objects)
    print(begin_config)
    print(goal_config)

    state = BlockState(begin_config, len(begin_config), objects)

    for child in state.children:
        print(child.config, child.action)
    state, nodes, max_depth = s.bfs_search(state, 'bfs', goal_config)
    print(state.config)
    print(s.calculate_path_to_goal(state))


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
