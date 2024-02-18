import time

def canConstruct(target : str, strings : list[str]) -> bool:
    
    if target == '' : 
        return True

    for string in strings:
        if target.startswith(string):
            rem = target.removeprefix(string)
            if canConstruct(rem,strings):
                return True
    
    return False

def canConstructDynamic(target : str, strings : list[str], memo = None) -> bool:
    
    if memo == None:
        memo = {}
    
    if target == '' : 
        return True

    if target in memo:
        return memo[target]

    for string in strings:
        if target.startswith(string):
            rem = target.removeprefix(string)
            if canConstructDynamic(rem,strings,memo):
                memo[target] = True
                return True
    memo[target] = False
    return False



print(canConstruct('abcdef',['abc','ef','d','def','bc']))
print(canConstruct('skateboard',['bo','rd','at','def','bc']))
start_time = time.time()
print(canConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeef',
['bo','rd','at','def','bc','eeee','ee','e','eeeeee']))
end_time = time.time()
print(f"Time taken for normal: {end_time - start_time} seconds")


print(canConstructDynamic('abcdef',['abc','ef','d','def','bc']))
print(canConstructDynamic('skateboard',['bo','rd','at','def','bc']))

start_time = time.time()
print(canConstructDynamic('eeeeeeeeeeeeeeeeeeeeeeeeeef',
['bo','rd','at','def','bc','eeee','ee','e','eeeeee']))
end_time = time.time()
print(f"Time taken for dynamic: {end_time - start_time} seconds")