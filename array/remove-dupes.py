#!/usr/bin/python3

#remove duplicates from a sorted array
def removeDuplicates(nums):
    if len(nums) == 0:
        return 0
    i = 0
    for j in range(1, len(nums)):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]
    return i + 1

def test_remove_duplicates():
    assert removeDuplicates([1, 1, 2]) == 2
    assert removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]) == 5
    assert removeDuplicates([]) == 0

#time complexity: O(n)
#space complexity: O(1)

if __name__ == '__main__':
    test_remove_duplicates()
