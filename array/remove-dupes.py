#remove duplicates from an array
def removeDuplicates(self, nums: List[int]) -> int:
    if len(nums) == 0:
        return 0
    i = 0
    for j in range(1, len(nums)):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]
    return i + 1

def test_remove_duplicates():
    nums = [1, 1, 2]
    assert removeDuplicates(nums) == 2
    nums = [0,0,1,1,1,2,2,3,3,4]
    assert removeDuplicates(nums) == 5
    nums = [1,1,1,2,2,3]
    assert removeDuplicates(nums) == 4

#time complexity: O(n)
#space complexity: O(1)