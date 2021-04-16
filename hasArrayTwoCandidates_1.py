# just like two sum
# solution 1 hash map. 
def hasArrayTwoCandidates(array, sum):
    myhash = dict()
    N = len(array)

    for i in range(N):
        temp = sum - array[i]
        if temp in myhash:
            return True
        else:
            myhash[array[i]] = True
    
    return False


assert hasArrayTwoCandidates([0,-1,2,-3,1], -2) == True
assert hasArrayTwoCandidates([1,-2,1,0,5], 0) == False
