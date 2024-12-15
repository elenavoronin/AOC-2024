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
			if self.check_page(page, graph) == False:
				new_page = self.order_page(page, graph)
				print(new_page)
				middle_index = len(new_page) // 2
				sum_middle += int(new_page[middle_index])
		return sum_middle
	
	def check_page(self, page: str, graph: dict) -> bool:
		page_sequence = list(map(int, page.strip().split(",")))
		visited = set()
		for curr_page in page_sequence:
			for page_before in graph[curr_page]:
				if page_before in visited:
					return False
			visited.add(curr_page)
		return True

	def order_page(self, page: str, graph: dict) -> list:
		def dfs(curr_page):
			if curr_page in visited:  # If already processed, skip
				return
			visited.add(curr_page)    # Mark as visited

			# Recursively process all prerequisites
			for page_before in graph.get(curr_page, []):
				if page_before not in visited and page_before in page_sequence:  # Only process unvisited pages
					dfs(page_before)
			# Add the current page after all prerequisites are processed
			ordered_page.append(curr_page)

		page_sequence = list(map(int, page.strip().split(",")))
		ordered_page = []  # Final ordered list
		visited = set()    # Tracks pages that have been processed

		for curr_page in page_sequence:
			if curr_page not in visited:  # Start a DFS only if not visited
				dfs(curr_page)

		return ordered_page



solution = Solution()
print("result: ", solution.print_order())
