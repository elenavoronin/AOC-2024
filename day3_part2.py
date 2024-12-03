class Solution:
	def find_mul(self) -> int:
		result = 0
		enabled = True
		with open("input/day3Input.txt", 'r') as fd:
			for line in fd:
				index = 0
				while index < len(line):
					dont_pos = line.find("don't()", index)
					do_pos = line.find("do()", index)
					if (dont_pos != -1 and (do_pos == -1 or dont_pos < do_pos)):
						enabled = False
						index = dont_pos + len("don't()")
						continue
					elif (do_pos != -1 and (dont_pos == -1 or do_pos < dont_pos)):
						enabled = True
						index = do_pos + len("do()")
						continue
					
					if enabled:
						i = line.find("mul(", index)
						if i == -1:
							break  # No more instances in this line
						try:
							num1_start = i+4
							num1_end = line.find(",", num1_start)
							if num1_end == -1:
								break
							num2_start = num1_end + 1
							num2_end = line.find(")", num2_start)
							if num2_end == -1:
								break
							num1 = int(line[num1_start:num1_end])
							num2 = int(line[num2_start:num2_end])

							result += num1 * num2
							print("num1: ", num1, "num2: ", num2)
							index = i + 1
						except ValueError:
							index += 1
		return result


solution = Solution()
print(solution.find_mul())
