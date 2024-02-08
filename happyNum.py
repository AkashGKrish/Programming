def happyNum (n, memo = None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    numTostr = str(n)
    sum = 0
    for digit in numTostr:
        digit = int(digit)
        sum += digit**2
    if sum == 1:
        memo[n] = True
        
        print(f"From if: {memo}")
        return memo[n]
    else:
        memo[n] = False
        print(f"From else: {memo}")
        return happyNum (sum,memo)
    

print(happyNum(41))