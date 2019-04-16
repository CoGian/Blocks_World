import re


'''
Alter configs from plain text to coded list
values in config will be
-1 = cube is clear OR
or  j = cube over it
AND  x = cube  under it
or -1 = cube is on table
'''


def create_config(objects, state_in_text):

    config = list()

    # initialize all cubes with -1
    for i in range(len(objects)):
        config.append([-1, -1])

    for text in state_in_text:
        tokens = re.split('[ ]', text)
        if tokens[0] == 'ON':
            index1, index2 = objects.index(tokens[1]), objects.index(tokens[2])
            config[index2][0] = index1
            config[index1][1] = index2

    return tuple(map(tuple, config))


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