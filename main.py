from pathfinder import Pathfinder

matrix = [
    [1,1,1,1,1,1,1],
    [1,1,1,1,0,0,0],
    [1,1,1,1,1,1,1],
];

pt = Pathfinder(True);

pt.find_path(matrix, [0,0], [6,2]);