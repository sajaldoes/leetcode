import sys

# Ideas:
    # 1. a
    # 2. b


class Solution:
    def solution(self, x):
        l,r = 0, x+1

        while l < r:
            mid = (l+r)//2
            if mid*mid > x:
                r = mid
            else:
                l = mid + 1
        
        return l-1


def main():
    input_lines = sys.stdin.readlines()
    num_vars = 1 # Number of variables in a test case

    # Process each test case
    results = []
    for i in range(0, len(input_lines), num_vars):
       
        # For single integer input
        k = int(input_lines[i].strip())

        # For Solution class
        solution = Solution()
        result = solution.solution(k) 	# Change the function and the parameter
        results.append(result)

    for result in results:
        print(result)

if __name__ == '__main__':
    main()