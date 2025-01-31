import heapq


class Board:
    def __init__(self, grid):
        self.grid = grid

    def __hash__(self):
        return hash(tuple(tuple(row) for row in self.grid))

    def __eq__(self, other):
        if isinstance(other, Board):
            return self.grid == other.grid
        return False

    def __lt__(self, other):
        if isinstance(other, Board):
            return self.grid < other.grid
        return NotImplemented

    def __repr__(self):
        return f"Board({self.grid})"

    def position_vide(self):
        for i, row in enumerate(self.grid):
            if 0 in row:
                return i, row.index(0)
        return None

    def moves(self):
        i, j = self.position_vide()
        mouvements = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < 3 and 0 <= nj < 3:
                new_grid = [row[:] for row in self.grid]
                new_grid[i][j], new_grid[ni][nj] = new_grid[ni][nj], new_grid[i][j]
                mouvements.append(Board(new_grid))
        return mouvements

finale = Board([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
])

begin = Board([
    [4, 7, 8],
    [2, 3, 5],
    [1, 6, 0]
])

def dijkstra_lent(start_state, target_state=finale):

    frontier = [(0, start_state)]
    costs = {start_state: 0}
    previous = {start_state: None}
    visited = set()

    while frontier:
        frontier.sort()
        current_cost, current_state = frontier.pop(0)

        if current_state == target_state:
            path = []
            while current_state:
                path.append(current_state)
                current_state = previous[current_state]
            return path[::-1]

        if current_state in visited:
            continue
        visited.add(current_state)

        for neighbor in current_state.moves():
            if neighbor in visited:
                continue
            new_cost = current_cost + 1

            if neighbor not in costs or new_cost < costs[neighbor]:
                costs[neighbor] = new_cost
                previous[neighbor] = current_state
                frontier.append((new_cost, neighbor))
    return False


def dijkstra(start_state, target_state=finale):
    frontier = []
    heapq.heappush(frontier, (0, start_state))
    costs = {start_state: 0}
    previous = {start_state: None}
    visited = set()

    while frontier:
        current_cost, current_state = heapq.heappop(frontier)

        if current_state == target_state:
            path = []
            while current_state:
                path.append(current_state)
                current_state = previous[current_state]
            for i in range(len(path)):
                path[i] = path[i].grid
                path[i] = path[i][0] + path[i][1] + path[i][2]
            return len(path), path[::-1]

        if current_state in visited:
            continue
        visited.add(current_state)

        for neighbor in current_state.moves():
            if neighbor in visited:
                continue
            new_cost = current_cost + 1

            if neighbor not in costs or new_cost < costs[neighbor]:
                costs[neighbor] = new_cost
                previous[neighbor] = current_state
                heapq.heappush(frontier, (new_cost, neighbor))

    return None