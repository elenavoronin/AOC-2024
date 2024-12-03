from collections import Counter

class Solution:
	def similarity_score(self, col1: list[int], col2: list[int]) -> int:
		i = 0
		with open("day1Input.txt", 'r') as input:
			for line in input:
				line_split = line.split()
				if len(line_split) == 2:
					col1.append(int(line_split[0]))
					col2.append(int(line_split[1]))
				else:
					print(f"Skipping invalid line: {line.strip()}")
		sim_score = 0
		col2_count = Counter(col2)
		for num in col1:
			nr = col2_count[num]
			sim_score += num * nr

		return sim_score
# Create an instance of the Solution class
solution = Solution()

# Initialize the two lists where input data will be stored
col1 = []
col2 = []

# Print the results
print("Final similarity score:", solution.similarity_score(col1, col2))
