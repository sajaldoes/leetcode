import sys

# Ideas:
    # 1. a
    # 2. b


class Solution:
    def solution(self, nums1, nums2):

        hash_map = {}
        result = []
        for i in nums1:
            if i not in hash_map: hash_map[i] = 1
            else: hash_map[i] += 1
        
        for i in nums2:
            if i in hash_map and hash_map[i]>0:
                hash_map[i]-=1
                result.append(i)

        return result


def main():
    input_lines = sys.stdin.readlines()
    num_vars = 2 # Number of variables in a test case

    # Process each test case
    results = []
    for i in range(0, len(input_lines), num_vars):
        list1 = input_lines[i].strip()
        list2 = input_lines[i+1].strip()
        # For list input
        list1 = list1[1:-1].split(',') 	# String to a list of strings
        list1 = [int(num) for num in list1] 	# Convert list of strings to list of integers

        list2 = list2[1:-1].split(',') 	# String to a list of strings
        list2 = [int(num) for num in list2] 	# Convert list of strings to list of integers

        # For Solution class
        solution = Solution()
        result = solution.solution(list1, list2) 	# Change the function and the parameter
        results.append(result)

    for result in results:
        print(result)

if __name__ == '__main__':
    main()
