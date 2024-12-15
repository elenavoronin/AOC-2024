class Solution:
	def find_xmas(self) -> int:
		count = 0
		grid = []
		with open("input/day4Input.txt", 'r') as fd:
			for line in fd:
				grid.append(line.strip())
		
		for row in range(len(grid)):
			for col in range(len(grid[0])):
				if grid[row][col] == 'X':  # Start checking if 'X' is found
					count += self.check_word(grid, (row, col))
		return count

	def check_word(self, grid: list[list[str]], pos: tuple[int, int]) -> int:
		directions = [
			(-1, -1), (-1, 0), (-1, 1),  # Up-left, Up, Up-right
			(0, -1),         (0, 1),    # Left, Right
			(1, -1), (1, 0), (1, 1)     # Down-left, Down, Down-right
		]
		count = 0
		for dr, dc in directions:
			r, c = pos  # Start at the current position
			matched = True  # Assume the word matches initially
		
			word = "XMAS"
			for char in word:
				if 0 <= r < len(grid) and 0 <= c < len(grid[0]):
					if grid[r][c] == char:  # Match the current character
						r += dr  # Move in the row direction
						c += dc  # Move in the column direction
					else:
						matched = False  # If characters don't match, break the loop
						break
				else:
					matched = False  # If out of bounds, break the loop
					break
			if matched:  # If the word "MAS" matches in this direction
				count += 1

		return count  # "MAS" not found in any direction


solution = Solution()
print(solution.find_xmas())
