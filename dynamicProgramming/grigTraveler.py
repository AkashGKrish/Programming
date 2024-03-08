memo = {}

def gridtravelever(m,n):
    if m == 0 or n == 0:
        return 0
    if m == 1 and n == 1:
        return 1
    return gridtravelever(m-1,n) + gridtravelever(m,n-1)

def gridtravelever_dynamic(m,n):
    grid = (m,n)
    if m == 0 or n == 0:
        return 0
    if m == 1 and n == 1:
        return 1
    if grid in memo:
        return memo[grid]
    
    result = gridtravelever_dynamic(m-1,n) + gridtravelever_dynamic(m,n-1)
    memo[grid] = result
    return result

# print(gridtravelever(1,0))
# print(gridtravelever(1,1))
# print(gridtravelever(2,3))
# print(gridtravelever(3,3))
# print(gridtravelever(3,4))
# print(gridtravelever(18,18))

print(gridtravelever_dynamic(1,0))
print(gridtravelever_dynamic(1,1))
print(gridtravelever_dynamic(2,3))
print(gridtravelever_dynamic(3,3))
print(gridtravelever_dynamic(3,4))
print(gridtravelever_dynamic(18,18))
print(gridtravelever_dynamic(180,180))