from collections import defaultdict

class Solution:
	def print_order(self) -> int:
		rules = []
		print_list = []
		with open("input/day5Input.txt", 'r') as fd:
			text = fd.read()
			chunks = text.split("\n\n")

			graph = defaultdict(list)
			for rule in chunks[0].strip().splitlines():
				x, y = map(int, rule.split("|"))
				graph[x].append(y)

		sum_middle = 0
		for page in chunks[1].strip().splitlines():
			print(page)
			if self.check_page(page, graph):
				middle_index = len(page.split(",")) // 2
				sum_middle += int(page.strip().split(",")[middle_index])
		return sum_middle
	
	def check_page(self, page: str, graph: dict) -> bool:
		page_sequence = list(map(int, page.strip().split(",")))
		visited = set()
		for curr_page in page_sequence:
			# print(f"Checking page: {curr_page}")
			for page_before in graph[curr_page]:
				# print(f"Page {curr_page} has a preceding page {page_before}")
				if page_before in visited:
					# print(f"Failed at page {curr_page}, page_before {page_before} not in visited.")
					return False
			visited.add(curr_page)
			# print(f"Visited: {visited}")
		return True




solution = Solution()
print("result: ", solution.print_order())
