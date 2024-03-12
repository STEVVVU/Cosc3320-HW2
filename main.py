import time
import random

# Initialize parameters for the knapsack problem
n = 20  # number of items
W = 200  # maximum capacity of the knapsack

# Define the bottom-up DP algorithm
def knapsack_bottom_up(values, weights, n, W):
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], values[i - 1] + dp[i - 1][w - weights[i - 1]])
            else:
                dp[i][w] = dp[i - 1][w]
    return dp[n][W]

# Define the recursive algorithm without memoization
def knapsack_recursive(values, weights, n, W):
    if n == 0 or W == 0:
        return 0
    if weights[n - 1] > W:
        return knapsack_recursive(values, weights, n - 1, W)
    return max(knapsack_recursive(values, weights, n - 1, W),
               values[n - 1] + knapsack_recursive(values, weights, n - 1, W - weights[n - 1]))

# Define the recursive algorithm with memoization
def knapsack_recursive_memo(values, weights, n, W, memo):
    if n == 0 or W == 0:
        return 0
    if memo[n][W] is not None:
        return memo[n][W]
    if weights[n - 1] > W:
        memo[n][W] = knapsack_recursive_memo(values, weights, n - 1, W, memo)
    else:
        memo[n][W] = max(knapsack_recursive_memo(values, weights, n - 1, W, memo),
                         values[n - 1] + knapsack_recursive_memo(values, weights, n - 1, W - weights[n - 1], memo))
    return memo[n][W]

# Timing function
def time_function(func, *args):
    start = time.time()
    result = func(*args)
    end = time.time()
    return result, end - start


for i in range(1, 11):
  # Initialize memoization array for the recursive algorithm with memoization
  memo = [[None for _ in range(W + 1)] for _ in range(n + 1)]
  
  values = [random.randint(1, 100) for _ in range(n)]  # random values for the items
  weights = [random.randint(1, 100) for _ in range(n)]  # random weights for the items
  print("Weights : ", weights)
  print("Values : ", values)
  
  # Time and execute the bottom-up DP algorithm
  bottom_up_result, bottom_up_time = time_function(knapsack_bottom_up, values, weights, n, W)
  
  # Time and execute the recursive algorithm without memoization
  recursive_result, recursive_time = time_function(knapsack_recursive, values, weights, n, W)
  
  # Time and execute the recursive algorithm with memoization
  recursive_memo_result, recursive_memo_time = time_function(knapsack_recursive_memo, values, weights, n, W, memo)
  
  # Displaying the results
  results = {
      "Bottom-Up DP": {
          "Result": bottom_up_result,
          "Time (s)": bottom_up_time
      },
      "Recursive without Memoization": {
          "Result": recursive_result,
          "Time (s)": recursive_time
      },
      "Recursive with Memoization": {
          "Result": recursive_memo_result,
          "Time (s)": recursive_memo_time
      }
  }
  print(i)
  print("Bottom Up Approach", bottom_up_time, "seconds,", bottom_up_result)
  print("Recursive Non Memo", recursive_time, "seconds,", recursive_result)
  print("Recursive Memo", recursive_memo_time, "seconds,", recursive_memo_result)