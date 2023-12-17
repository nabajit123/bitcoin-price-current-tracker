# Top-Down (Memoization) Approach:

#     Recursive Calls: In the top-down approach, the original problem is solved by recursively 
#       breaking it down into smaller subproblems.
#     Memoization: To avoid redundant computations, the results of subproblems are stored in a 
#       data structure (usually an array or a dictionary). This way, if a subproblem has already been solved, its result can be directly retrieved instead of recomputing it.


def fib_top_down(n, memo={}):
    if n <= 1:
        return n
    if n not in memo:
        memo[n] = fib_top_down(n-1, memo) + fib_top_down(n-2, memo)
    return memo[n]


# Bottom-Up (Tabulation) Approach:

#     Iterative Solution: In the bottom-up approach, you start by solving the smallest subproblems 
#       and gradually build up to the original problem.
#     Tabulation: Results of subproblems are stored in a table or array, and the solution to each 
#       subproblem is computed iteratively based on previously computed results.

def fib_bottom_up(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


# Key Differences:

#     Recursion vs. Iteration: Top-down uses recursion to break the problem into subproblems, 
#       while bottom-up uses iteration to solve subproblems and build up to the original problem.
#     Memoization vs. Tabulation: Top-down uses memoization to store and reuse the results of 
#       subproblems, while bottom-up uses tabulation to fill in a table with results as it iterates through the subproblems.
#     Function Call Overhead: Top-down may incur additional function call overhead due to recursion,
#        while bottom-up typically avoids this overhead.

# In general, both approaches are valid dynamic programming strategies, and the choice between them
#        often depends on the specific problem and programming preferences. Top-down can be more intuitive and easier to write, but bottom-up is often more efficient and avoids potential issues with recursion depth.