#!/usr/bin/python3

#single number
def singleNumber(nums):
    a = 0
    for i in nums:
        a ^= i
    return a

def test_single_number():
    assert singleNumber([2, 2, 1]) == 1
    assert singleNumber([4, 1, 2, 1, 2]) == 4
    assert singleNumber([1]) == 1

#time complexity o(n)
#space complexity o(1) -> bit manipulation trick

if __name__ == '__main__':
    test_single_number()
