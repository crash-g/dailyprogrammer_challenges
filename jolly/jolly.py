def isJolly(n, l):
    # n is the maximum element in the array l
    # note that using set on an unordered list should be O(nlog n)
    return set([abs(item-l[i-1]) for i,item in enumerate(l) if i > 0]) == set(range(1,n))

print(isJolly(4,[1,4,2,3]))
print(isJolly(8,[1,6,-1,8,9,5,2,7]))
