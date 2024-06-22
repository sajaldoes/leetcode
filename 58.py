import sys

# Ideas:
    # 1. a
    # 2. b


class Solution:
    def solution(self, s):

        # s = s.replace('"','').strip().split(' ')[-1] #not needed for leetcode

        return len(s.split()[-1])


def main():
    input_lines = sys.stdin.readlines()
    num_vars = 1 # Number of variables in a test case

    # Process each test case
    results = []
    for i in range(0, len(input_lines), num_vars):
        # list1 = input_lines[i].strip()
        # For list input
        # list1 = list1[1:-1].split(',') 	# String to a list of strings
        # list1 = [int(num) for num in list1] 	# Convert list of strings to list of integers

        # For single integer input
        # k = int(input_lines[i + 1].strip())

        # For String input
        s = input_lines[i].strip()[1:-1]

        # For Solution class
        solution = Solution()
        result = solution.solution(s) 	# Change the function and the parameter
        results.append(result)

    for result in results:
        print(result)

if __name__ == '__main__':
    main()