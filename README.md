# Dynamic Programming Techniques

## Memoization Recipe

### Make it work (correctness)

    1. Visualize the problem as a tree
    2. Implement tree using recursion
    3. Test it (large input can take longer)

### Make it efficient

    1. add memo object
        - Needs keys which represents arguements to our function.
        - And values of that object represents values for those function calls
        - Like a Map
    2. Add base cases to return memo values
        - Memo will fetch you the result
    3. Store return values into the memo
