import sys
import re


def parse_file(file):
    # read objects till find the line with init

    while True:
        line = file.readline( )
        if "objects" in line:
            break

    objects = line.split(' ')

    objects.remove("(objects")

    while True:
        line = file.readline( )
        if "INIT" not in line:
            objects.extend(line.split(" "))
        else:
            break

    objects.remove(")\n")
    print(objects)

    # read initial state till find line with goal
    init = re.split('[()\n]', line)

    while True:
        line = file.readline( )
        if "goal" not in line:
            init.extend(re.split('[()\n]', line))
        else:
            break

    # trim init
    while '' in init:
        init.remove('')

    while ' ' in init:
        init.remove(' ')

    init.remove("INIT ")
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
    goal.remove('goal ')
    goal.remove('AND ')

    while '' in goal:
        goal.remove('')

    while ' ' in goal:
        goal.remove(' ')
    print(goal)


def main():
    """
     sm = sys.argv[1].lower()

    file_name = sys.argv[2]

    """

    file = open('probBLOCKS-4-0.pddl.txt', 'r')

    parse_file(file)

    # begin_state = tuple(map(int, begin_state))

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
