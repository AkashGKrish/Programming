def bestSum (targetSum,numbers):
    
    if targetSum == 0: return []
    if targetSum < 0: return None
    
    short_combo = None

    for num in numbers:
        rem = targetSum-num
        rem_combination = bestSum(rem,numbers)
        if rem_combination is not None:
            combination = rem_combination + [num]
            if short_combo is None or len(combination) < len (short_combo):
                short_combo = combination

    return short_combo

 
 
def bestSumDynamic (targetSum,numbers, memo = None):
    
    if memo is None:
        memo = {}

    if targetSum in memo:
        return memo[targetSum]
    
    if targetSum == 0: return []
    if targetSum < 0: return None
    
    short_combo = None

    for num in numbers:
        rem = targetSum-num
        rem_combination = bestSumDynamic(rem,numbers, memo)
        if rem_combination is not None:
            combination = rem_combination + [num]
            
            if short_combo is None or len(combination) < len (short_combo):
                short_combo = combination
    
    memo[targetSum] = short_combo
    return short_combo 

# print(bestSum(7,[5,3,4,7]))
# print(bestSum(8,[5,3,2]))
# print(bestSum(8,[1,4,5,]))
# print(bestSum(100,[1,2,5,25]))

print(bestSumDynamic(7,[5,3,4,7]))
print(bestSumDynamic(8,[5,3,2]))
print(bestSumDynamic(8,[1,4,5,]))
print(bestSumDynamic(100,[1,2,5,25]))