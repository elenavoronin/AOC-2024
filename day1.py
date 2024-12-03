class Solution:
	def add_input(self, col1: list[int], col2: list[int]) -> int:
		i = 0
		with open("day1Input.txt", 'r') as input:
			for line in input:
				line_split = line.split()
				if len(line_split) == 2:
					col1.append(int(line_split[0]))
					col2.append(int(line_split[1]))
				else:
					print(f"Skipping invalid line: {line.strip()}")
		total_sum = 0
		
		while col1 and col2:
			min1 = min(col1)
			min2 = min(col2)
			diff = abs(min2 - min1)
			total_sum += diff
			col1.remove(min1)
			col2.remove(min2)

		return total_sum

# Create an instance of the Solution class
solution = Solution()

# Initialize the two lists where input data will be stored
col1 = []
col2 = []

# Print the results
print("Final sum:", solution.add_input(col1, col2))
