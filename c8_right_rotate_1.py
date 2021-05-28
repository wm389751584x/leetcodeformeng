def right_rotate(nums, k):
    
    # check your base case:
    if not nums: return []

    # make sure k don't overlap
    k =  k % len(nums)

    # loop pop and insert

    while k:
        nums.insert(0, nums.pop())
        k -= 1

    return nums

if __name__ == "__main__":
    print(right_rotate([1, 2, 3, 4, 5], 2))