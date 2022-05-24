#!/usr/bin/python3

#rotate array
def rotate(nums, k):
    if len(nums) == 0:
        return 0
    k = k % len(nums)
    nums[:] = nums[-k:] + nums[:-k]
    return nums

def test_rotate():
    assert rotate([1, 2, 3, 4, 5, 6, 7], 3) == [5, 6, 7, 1, 2, 3, 4]
    assert rotate([-1, -100, 3, 99], 2) == [3, 99, -1, -100]
    assert rotate([], 0) == 0

#time complexity: O(n)
#space complexity: O(1)

if __name__ == '__main__':
    test_rotate()
