import numpy as np
from collections import deque
from random import shuffle


def generate_maze(size):
    maze = np.ones((size, size), dtype=int)
    maze[1::2, 1::2] = 0

    for y in range(1, size - 1, 2):
        for x in range(1, size - 1, 2):
            directions = [(0, 2), (2, 0), (0, -2), (-2, 0)]
            shuffle(directions)

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 < nx < size - 1 and 0 < ny < size - 1:
                    if maze[ny, nx] == 1:
                        maze[y + dy // 2, x + dx // 2] = 0
                        maze[ny, nx] = 0
                        break

    start = (0, 1)
    end = (size - 1, size - 2)

    maze[start] = 0
    maze[end] = 0

    return start, end, maze




def bfs(maze, start, end):
    rows, cols = maze.shape
    visited = np.zeros_like(maze, dtype=bool)
    queue = deque([(start, [])])

    while queue:
        (y, x), path = queue.popleft()

        if (y, x) == end:
            return path + [(y, x)]

        if not visited[y, x]:
            visited[y, x] = True
            for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                ny, nx = y + dy, x + dx
                if 0 <= ny < rows and 0 <= nx < cols and not visited[ny, nx] and maze[ny, nx] == 0:
                    queue.append(((ny, nx), path + [(y, x)]))

    return None
