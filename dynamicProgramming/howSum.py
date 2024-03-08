def howSum(targetSum, numbers):
    
    if targetSum == 0: return []
    if targetSum < 0: return None

    for num in numbers:
        rem = targetSum-num
        result = howSum(rem, numbers)
        if result is not None: 
            return result + [num]
    return None

def howSum_dynamic(targetSum, numbers, memo = None):
    if memo is None:
        memo = {}
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0: return []
    if targetSum < 0: return None

    for num in numbers:
        rem = targetSum-num
        result = howSum_dynamic(rem, numbers,memo)
        if result is not None:
            memo[targetSum] = result + [num]
            return result + [num]
    memo[targetSum]= None
    return None

print(howSum_dynamic(7,[3,4,6,7]))
print(howSum_dynamic(7,[2,3,4]))
print(howSum_dynamic(7,[4,3,2]))
print(howSum_dynamic(7,[2,4]))
print(howSum_dynamic(8,[2,4,3,5]))
print(howSum_dynamic(300,[14,7]))


# print(howSum(7,[3,4,6,7]))
# print(howSum(7,[2,3,4]))
# print(howSum(7,[2,4]))
# print(howSum(8,[2,4,3,5]))
# print(howSum(300,[14,7]))