
# Ideas:
	# 1. create a copy of the list, then replace the elements
	# 2. b

class Solution:
	def rotate(self, nums, k):
		nums2 = list(nums)
		n = len(nums)

		for i in range(n):
			nums[(i+k)%n] = nums2[i]

		print(nums) 


if __name__ == '__main__':

	list1 = input()
	# For list input
	list1 = list1[1:-1].split(",") # String to a list of strings
	list1 = [int(num) for num in list1] # Convert list of strings to list of integers

	int1 = input()
	# Convert string to integer
	int1 = int(int1)

	# For Solution class
	solution = Solution()
	solution.rotate(list1, int1) # Change the function and the parameter