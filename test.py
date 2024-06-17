# Ideas:
	# 1. a
	# 2. b


class Solution:
	def solution(self, nums, k):

		return nums

if __name__ == '__main__':

	list1 = input()
	# For list input
	list1 = list1[1:-1].split(',') 	# String to a list of strings
	list1 = [int(num) for num in list1] 	# Convert list of strings to list of integers

	int1 = input()
	# Convert string to integer
	int1 = int(int1)

	# For Solution class
	solution = Solution()
	solution.solution(list1, int1) 	# Change the function and the parameter