def canSum(targetSum, numbers ):
    if targetSum == 0:
        return True
    if targetSum < 0:
        return False
    for num in numbers:
        rem = targetSum-num
        if canSum(rem,numbers) == True:
            return True
    return False

def canSum_dynamic(targetSum, numbers, memo = None ):
    if memo is None:
        memo = {}
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return True
    if targetSum < 0:
        return False
    for num in numbers:
        rem = targetSum-num
        if canSum_dynamic(rem,numbers, memo) == True:
            memo[targetSum] = True
            return True
    memo[targetSum]= False
    return False
    



print(canSum_dynamic(7,[3,4,6,7]))
print(canSum_dynamic(7,[2,3,4]))
print(canSum_dynamic(7,[2,4]))
print(canSum_dynamic(8,[2,4,3,5]))
print(canSum_dynamic(300,[14,7]))


# print(canSum(7,[3,4,6,7]))
# print(canSum(7,[2,3,4]))
# print(canSum(7,[2,4]))
# print(canSum(8,[2,4,3,5]))
# print(canSum(300,[14,7]))
