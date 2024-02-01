# Dynamic Programming Techniques

## Memoization Recipe

1. Make it work (correctness)
    [] Visualize the problem as a tree
    [] Implement tree using recursion
    [] Test it (large input can take longer)

2. Make it efficient
    [] add memo object
        - Needs keys which represents arguements to our function.
        - And values of that object represents values for those function calls
        - Like a Map
    [] Add base cases to return memo values
        - Memo will fetch you the result
    [] Store return values into the memo
