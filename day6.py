class Solution:
	def check_moves(self) ->int:
		moves = 0
		grid = []
		with open("input/day6.txt") as fd:
			for line in fd:
				grid.append(list(line.strip()))
		x = 0
		y = 0
		directions = {
			"up": "^",
			"down": "v",
			"left": "<",
			"right": ">"
		}
		for row in range(len(grid)):
			for col in range(len(grid[0])):
				if grid[row][col] in directions.values():
					x,y = row, col
					print("x: ", x, "y: ", y)
					dir = [key for key, value in directions.items() if value == grid[row][col]][0]
		
		grid[x][y] = "X"
		while True:
			if self.check_obstacles(grid, x, y, dir):
				x, y = self.update_position(x, y, dir)
				moves += self.make_moves(grid, x, y)
				print(dir)
			else:
				new_x, new_y = self.update_position(x, y, dir)
				if not (new_x >= 0 and new_x < len(grid) and new_y >= 0 and new_y < len(grid[0])):
					moves += 1
					break
				else:
					dir = self.change_directions(dir)
		self.print_grid(grid)
		return moves


	def print_grid(self, grid: list[list[str]]) -> None:
		for row in grid:
			print("".join(row))
		print("\n")  # Add a blank line for readability

	def check_obstacles(self, grid: list[list[str]], x: int, y: int, dir: str) -> bool:
		new_x, new_y = self.update_position(x, y, dir)
		if (new_x >= 0 and new_x < len(grid) and new_y >= 0 and new_y < len(grid[0])):
			if grid[new_x][new_y] in [".", "<", ">", "v", "^", "X"]:
				return True
		return False

	def make_moves(self, grid: list[list[str]], x: int, y : int) -> int:
		if grid[x][y] in [".", "<", ">", "v", "^"]:
			grid[x][y] = "X"
			return 1
		return 0

	def change_directions(self, dir: str) ->str:
		if dir == "up":
			return "right"
		if dir == "right":
			return "down"
		if dir == "down":
			return "left"
		if dir == "left":
			return "up"


	def update_position(self, x: int, y: int, dir: str) -> tuple:
		if dir == "up":
			return x - 1, y
		if dir == "down":
			return x + 1, y
		if dir == "left":
			return x, y - 1
		if dir == "right":
			return x, y + 1
		return x, y

solution = Solution()
print("distinct moves: ", solution.check_moves())
