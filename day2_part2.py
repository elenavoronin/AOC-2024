class Solution:

	def safety_score(self) -> int:
		count = 0
		with open("input/day2Input.txt", 'r') as fd:
			for line in fd:
				line_split = list(map(int, line.split()))
				if self.line_safe_after_remove_level(line_split):
					count += 1
		return 	count				

	def line_safe(self, line_split) -> bool:
		if len(line_split) == 1:
			return True
		increase = 0
		decrease = 0
		step_increase_max = float('-inf')
		step_decrease_max = float('-inf')
		step_increase_min = float('inf')
		step_decrease_min = float('inf')
		for i in range(len(line_split) - 1):
			if line_split[i] > line_split[i+1]:
				decrease += 1
				step_decrease_max = max(step_decrease_max, abs(line_split[i+1] - line_split[i]))
				step_decrease_min = min(step_decrease_min, abs(line_split[i+1] - line_split[i]))
			else:
				increase += 1
				step_increase_max = max(step_increase_max, abs(line_split[i + 1] - line_split[i]))
				step_increase_min = min(step_increase_min, abs(line_split[i + 1] - line_split[i]))
			if (decrease > 0 and increase > 0):
				return False
		if (decrease > 0):
			if (step_decrease_max <= 3 and step_decrease_min >= 1):
				return True
		if (increase > 0):
			if (step_increase_max <= 3 and step_increase_min >= 1):
				return True
		return False
	
	def line_safe_after_remove_level(self, line_split) -> bool:
		for i in range(len(line_split)):
			temp = line_split[:i] + line_split[i+1:]
			if self.line_safe(temp):
				return True
		return False


solution = Solution()
print(solution.safety_score())
