

# check if cube1 is on table
def is_on_table(cube1):
    return cube1[1] == -1


# The Class that Represents the state of Cubes

class BlockState(object):

    def __init__(self, config, n, objects, parent=None, action="Initial", cost=0, f=0, ):

        self.n = n

        self.cost = cost  # int g cost

        self.parent = parent  # BlockState

        self.action = action  # string

        self.config = config
        '''config is a tuple of tuples :
        Tuples in config will be : -1 if cube is clear  or index of cube over it
        AND   -1 if cube is on table or index of  cube under it .
        eg. : (-1,3) this cube is clear and has the cube with index 3 under it'''

        self.children = []  # list

        self.f = f  # f cost

        self.objects = objects  # a string array which indicates in which place in config is every cube

    def expand(self):

        index_of_cube1 = 0
        for cube1 in self.config:
            # if cube1 is clear and free to move
            if cube1[0] == -1:
                # if cube1 is not on table move cube1 on table  and create a child(new configuration of cubes)

                if not is_on_table(cube1):

                    new_config = list(map(list, self.config))

                    # update config
                    new_config[cube1[1]][0] = -1
                    new_config[index_of_cube1][1] = -1

                    if not self.is_same_with_predecessor(new_config):
                        action = 'Move(' + self.objects[index_of_cube1] + ',' + self.objects[cube1[1]] + ',table)'

                        # create child
                        child = BlockState(tuple(map(tuple, new_config)), self.n, self.objects, parent=self,
                                           action=action,
                                           cost=self.cost + 1)

                        # update child
                        self.children.append(child)

                # find others free cubes and save their indexes
                clear_cubes_indexes = self.find_others_free_cubes(index_of_cube1)

                # if there are free cubes move cube1 over other free cube and create a child(new configuration of cubes)
                for index_of_cube2 in clear_cubes_indexes:

                    new_config = list(map(list, self.config))

                    # update config
                    new_config[index_of_cube2][0] = index_of_cube1
                    new_config[index_of_cube1][1] = index_of_cube2

                    if not is_on_table(cube1):
                        new_config[cube1[1]][0] = -1

                    if not self.is_same_with_predecessor(new_config):

                        if is_on_table(cube1):
                            action = 'Move(' + self.objects[index_of_cube1] + ',' + 'table' + ',' + self.objects[
                                index_of_cube2] + ')'
                        else:

                            action = 'Move(' + self.objects[index_of_cube1] + ',' + self.objects[cube1[1]] \
                                     + ',' + self.objects[index_of_cube2] + ')'
                        # create child
                        child = BlockState(tuple(map(tuple, new_config)), self.n, self.objects, parent=self,
                                           action=action,
                                           cost=self.cost + 1)
                        # append on children's list
                        self.children.append(child)

            index_of_cube1 += 1

    # find and return indexes of free cubes except cube1's index
    def find_others_free_cubes(self, index_of_cube1):
        clear_cubes_indexes = []
        index_of_cube2 = 0
        for cube2 in self.config:
            if cube2[0] == -1 and index_of_cube2 != index_of_cube1:
                clear_cubes_indexes.append(index_of_cube2)
            index_of_cube2 += 1
        return clear_cubes_indexes

    def is_same_with_predecessor(self, new_config):

        state = self
        if state.parent is not None:
            if list(map(list, state.parent.config)) == new_config:
                return True
        return False

    def __eq__(self, other):
        if type(other) is str:
            return False
        return self.config == tuple(map(tuple, other.config))

    def __lt__(self, other):
        if type(other) is str:
            return False
        return self.config < tuple(map(tuple, other.config))

    def __gt__(self, other):
        if type(other) is str:
            return False
        return self.config > tuple(map(tuple, other.config))
