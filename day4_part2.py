class Solution:
	def find_x_mas(self) -> int:
		count = 0
		grid = []
		with open("input/day4Input.txt", 'r') as fd:
			for line in fd:
				grid.append(line.strip())
		
		for row in range(len(grid)):
			for col in range(len(grid[0])):
				main = self.collect_word(grid, row, col, (1, 1), 3)
				secondary = self.collect_word(grid, row, col + 2, (1, -1), 3)
				if (main == 'MAS' or main == 'SAM') and (secondary == 'MAS' or secondary == 'SAM'):
					count += 1
		return count

	def collect_word(self, grid: list[list[str]], pos_r: int, pos_c: int, dir: tuple[int, int], n: int):
		i = 0
		result =''
		while i < n and pos_r >= 0 and pos_r < len(grid) and pos_c >= 0 and pos_c < len(grid[pos_r]):
			result += grid[pos_r][pos_c]
			pos_r += dir[0]
			pos_c += dir[1]
			i += 1
		return result



solution = Solution()
print(solution.find_x_mas())
