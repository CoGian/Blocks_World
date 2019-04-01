# The Class that Represents the state of Cubes
class BlockState(object):

    def __init__(self, config, n, objects, parent=None, action="Initial", cost=0, f=0, ):

        self.n = n

        self.cost = cost

        self.parent = parent

        self.action = action

        self.config = config

        self.children = []

        self.f = f

        self.objects = objects

    def expand(self):

        index_of_cube1 = 0
        for cube1 in self.config:
            # if cube1 is clear and free to move
            if cube1 == -1:

                # find others free cubes and save their indexes
                clear_cubes_indexes = self.find_others_free_cubes(index_of_cube1)

                # if there are free cubes move cube1 over other free cube and create a child(new configuration of cubes)
                for index in clear_cubes_indexes:
                    new_config = list(self.config)
                    new_config[index] = index_of_cube1

                    if self.is_on_table(index_of_cube1):
                        action = 'Move(' + self.objects[index_of_cube1] + ',' + 'table' + ',' + self.objects[index] + ')'
                    else:
                        action = 'Move(' + self.objects[index_of_cube1] + ',' + self.objects[self.config.index(index_of_cube1)] \
                                     + ',' + self.objects[index] + ')'

                    child = BlockState(tuple(new_config), self.n, self.objects, parent=self, action=action, cost=self.cost+1)
                    self.children.append(child)

                # if cube1 not on table move cube1 on table  and create a child(new configuration of cubes)
                if not self.is_on_table(index_of_cube1):
                    new_config = list(self.config)
                    new_config[self.config.index(index_of_cube1)] = -1

                    action = 'Move(' + self.objects[index_of_cube1] + ',' + self.objects[
                        self.config.index(index_of_cube1)] + ',table)'
                    child = BlockState(tuple(new_config), self.n, self.objects, parent=self, action=action,
                                       cost=self.cost + 1)
                    self.children.append(child)

            index_of_cube1 += 1

    # find and return indexes of free cubes except cube1's index
    def find_others_free_cubes(self, index_of_cube1):
        clear_cubes_indexes = []
        index_of_cube2 = 0
        for cube2 in self.config:
            if cube2 == -1 and index_of_cube1 != index_of_cube2:
                clear_cubes_indexes.append(index_of_cube2)
            index_of_cube2 += 1

        return clear_cubes_indexes

    # check if cube1 is on table
    def is_on_table(self, index_of_cube1):
        return index_of_cube1 not in self.config

    def __eq__(self, other):
        return self.config == other.config

    def __lt__(self, other):
        return  self.config < other.config

