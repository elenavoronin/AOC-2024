import copy

class Solution:
	def check_moves_loop(self) ->int:
		grid = []
		with open("input/day6.txt") as fd:
			for line in fd:
				grid.append(list(line.strip()))
		directions = {
			"up": "^",
			"down": "v",
			"left": "<",
			"right": ">"
		}
		for row in range(len(grid)):
			for col in range(len(grid[0])):
				if grid[row][col] in directions.values():
					start_x,start_y = row, col
					start_dir = [key for key, value in directions.items() if value == grid[row][col]][0]
		
		grid[start_x][start_y] = "."
		count = 0
		for i in range(len(grid)):
			for j in range(len(grid[0])):
				if (i, j) == (start_x, start_y) or grid[i][j] == "#":
					continue
				# Place an obstacle and simulate
				grid[i][j] = "#"
				if self.simulation(grid, start_x, start_y, start_dir):
					count += 1
					print(count)
				# Reset the grid
				grid[i][j] = "."

		return count

	def simulation(self, grid: list[list[str]], x: int, y:int, dir: str) ->bool:
		# // check if the guard is stuck in a loop with the obstacle we placed
		# can't be the spot where he starts		
		direction_order = ["up", "right", "down", "left"]
		moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

		visited_states = set()
		visited_states.add((x, y, dir))			
		while True:
				move_x, move_y = moves[dir]
				new_x, new_y = x + move_x, y + move_y
				if not (new_x >= 0 and new_x < len(grid) and new_y >= 0 and new_y < len(grid[0])):
					return False
				if grid[new_x][new_y] == "#":
					dir = direction_order[(direction_order.index(dir) + 1) % 4]
				else:
					x, y = new_x, new_y
				if (x, y, dir) in visited_states:
					return True  # Loop detected
				visited_states.add((x, y, dir))

	# def print_grid(self, grid: list[list[str]]) -> None:
	# 	for row in grid:
	# 		print("".join(row))
	# 	print("\n")  # Add a blank line for readability

	def check_obstacles(self, grid: list[list[str]], x: int, y: int, dir: str) -> bool:
		if (x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0])):
			if grid[x][y] in ["."]:
				return True
		return False

solution = Solution()
print("possible obstruction positions: ", solution.check_moves_loop())
