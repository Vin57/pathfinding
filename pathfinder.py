from pathfinding.core.grid import Grid
from pathfinding.core.node import Node
from pathfinding.finder.a_star import AStarFinder

class Pathfinder:
    def __init__(self, debug:bool = False) -> tuple[list, int]:
        self.debug = debug;

    def find_path(self, matrix, start, end):
        grid = Grid(matrix=matrix);

        start_node = grid.node(x=start[0], y=start[1]);
        end_node = grid.node(x=end[0], y=end[1]);

        # 3. create a find with a movement style
        finder = AStarFinder();

        path, runs = finder.find_path(start_node, end_node, grid);

        if (self.debug):
            print(grid.grid_str(path=path, start=start_node, end=end_node, path_chr='·'));
            print('Running ' + str(runs) + ' time(s) to find a path');
        
        return path