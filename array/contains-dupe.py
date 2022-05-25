#!/usr/bin/python3

#contains duplicate
def containsDuplicate(nums):
    hash = {}
    for i in nums:
        if i in hash:
            return True
        else: 
            hash[i] = 1
    return False

def test_contains_dupes():
    assert containsDuplicate([1, 2, 3, 1]) == True
    assert containsDuplicate([1, 2, 3, 4]) == False
    assert containsDuplicate([1,1,1,3,3,4,3,2,4,2]) == True

#time complexity o(n)
#space complexity o(n)

if __name__ == '__main__':
    test_contains_dupes()
