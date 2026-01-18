# <!-- Instructions
# These are the rules of the Game of Life (as stated in Wikipedia):

# The universe of the Game of Life is an infinite, two-dimensional orthogonal grid of square cells, each of which is in one of two possible states, alive or dead, (or populated and unpopulated, respectively).

# Every cell interacts with its eight neighbours, which are the cells that are horizontally, vertically, or diagonally adjacent. At each step in time, the following transitions occur:

# Any live cell with fewer than two live neighbours dies, as if by underpopulation.
# Any live cell with two or three live neighbours lives on to the next generation.
# Any live cell with more than three live neighbours dies, as if by overpopulation.
# Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
# Using these rules, implement the Game. (Hint: use Classes !!!!)
# Use a few different initial states to see how the game ends.

# Notes:

# Display the grid after each generation
# The end of the game is fully determined by the initial state. So have it pass through your program and see how it ends.
# Be creative, but use classes
# The game can have fixed borders and can also have moving borders. First implement the fixed borders. Each “live” cell that is going out of the border, exits the game.
# Bonus: Make the game with ever expandable borders, make the maximum border size a very large number(10,000) so you won’t cause a memory overflow -->


import time


class GameOfLife:
    def __init__(self, rows, cols, initial_alive=None):
        """
        rows, cols: grid size (fixed borders)
        initial_alive: iterable of (r, c) tuples for alive cells
        """
        self.rows = rows
        self.cols = cols
        self.grid = [[0 for _ in range(cols)] for _ in range(rows)]

        if initial_alive:
            for r, c in initial_alive:
                if 0 <= r < rows and 0 <= c < cols:
                    self.grid[r][c] = 1

        self.generation = 0

    def display(self):
        print(f"Generation {self.generation}")
        for r in range(self.rows):
            line = []
            for c in range(self.cols):
                line.append("#" if self.grid[r][c] == 1 else ".")
            print(" ".join(line))
        print()

    def count_neighbors(self, r, c):
        count = 0
        for dr in (-1, 0, 1):
            for dc in (-1, 0, 1):
                if dr == 0 and dc == 0:
                    continue
                rr = r + dr
                cc = c + dc
                # fixed borders: outside is dead
                if 0 <= rr < self.rows and 0 <= cc < self.cols:
                    count += self.grid[rr][cc]
        return count

    def step(self):
        new_grid = [[0 for _ in range(self.cols)] for _ in range(self.rows)]

        for r in range(self.rows):
            for c in range(self.cols):
                alive = self.grid[r][c] == 1
                neighbors = self.count_neighbors(r, c)

                if alive:
                    # 1) underpopulation
                    if neighbors < 2:
                        new_grid[r][c] = 0
                    # 2) lives on
                    elif neighbors in (2, 3):
                        new_grid[r][c] = 1
                    # 3) overpopulation
                    else:
                        new_grid[r][c] = 0
                else:
                    # 4) reproduction
                    if neighbors == 3:
                        new_grid[r][c] = 1
                    else:
                        new_grid[r][c] = 0

        changed = (new_grid != self.grid)
        self.grid = new_grid
        self.generation += 1
        return changed

    def run(self, max_generations=50, delay=0.2, stop_if_stable=True):
        """
        max_generations: how many generations to simulate
        delay: seconds between prints
        stop_if_stable: stop if grid doesn't change anymore
        """
        self.display()
        for _ in range(max_generations):
            changed = self.step()
            self.display()
            time.sleep(delay)

            if stop_if_stable and not changed:
                print("Stopped: pattern became stable (no changes).")
                break


# -------------------- Some initial states --------------------

def blinker(top, left):
    # Period-2 oscillator (3 in a row)
    return [(top, left), (top, left + 1), (top, left + 2)]


def block(top, left):
    # Still life (2x2)
    return [(top, left), (top, left + 1), (top + 1, left), (top + 1, left + 1)]


def glider(top, left):
    # Moves diagonally
    return [
        (top, left + 1),
        (top + 1, left + 2),
        (top + 2, left),
        (top + 2, left + 1),
        (top + 2, left + 2),
    ]


if __name__ == "__main__":
    # Choose one pattern to test (or combine them)
    alive_cells = []
    alive_cells += blinker(5, 5)
    alive_cells += block(2, 2)
    alive_cells += glider(10, 10)

    game = GameOfLife(rows=20, cols=20, initial_alive=alive_cells)
    game.run(max_generations=60, delay=0.15, stop_if_stable=True)
