import sys

# Ideas:
    # 1. a
    # 2. b


class Solution:
    def solution(self, n, time):

        full_rounds = time//(n-1)
        time_cal = time%(n-1)
        if full_rounds%2!=0:
            return n - time_cal
        else:
            return time_cal + 1
        


def main():
    input_lines = sys.stdin.readlines()
    num_vars = 2 # Number of variables in a test case

    # Process each test case
    results = []
    for i in range(0, len(input_lines), num_vars):
        # list1 = input_lines[i].strip()
        # # For list input
        # list1 = list1[1:-1].split(',') 	# String to a list of strings
        # list1 = [int(num) for num in list1] 	# Convert list of strings to list of integers

        # For single integer input
        n = int(input_lines[i].strip())
        k = int(input_lines[i + 1].strip())

        # For Solution class
        solution = Solution()
        result = solution.solution(n, k) 	# Change the function and the parameter
        results.append(result)

    for result in results:
        print(result)

if __name__ == '__main__':
    main()