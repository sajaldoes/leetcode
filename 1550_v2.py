import sys

# Ideas:
    # 1. a
    # 2. b


class Solution:
    def solution(self, arr):

        count = 0
        for i in range(len(arr)):
            if arr[i]%2==1:
                count+=1
            else:
                count = 0
            
            if count==3:
                return True

        return False

def main():
    input_lines = sys.stdin.readlines()
    num_vars = 1 # Number of variables in a test case

    # Process each test case
    results = []
    for i in range(0, len(input_lines), num_vars):
        list1 = input_lines[i].strip()
        # For list input
        list1 = list1[1:-1].split(',') 	# String to a list of strings
        list1 = [int(num) for num in list1] 	# Convert list of strings to list of integers

        # For single integer input
        # k = int(input_lines[i + 1].strip())

        # For Solution class
        solution = Solution()
        result = solution.solution(list1) 	# Change the function and the parameter
        results.append(result)

    for result in results:
        print(result)

if __name__ == '__main__':
    main()