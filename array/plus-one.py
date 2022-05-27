#!/usr/bin/python3

#plus one
def plusOne(digits):
    for i in range(len(digits)):
        idx = len(digits) - 1 - i
        if digits[idx] == 9:
            digits[idx] = 0
        else:
            digits[idx] += 1
            return digits
    return [1] + digits

def test_plus_one():
    assert plusOne([1, 2, 3]) == [1, 2, 4]
    assert plusOne([4, 3, 2, 1]) == [4, 3, 2, 2]
    assert plusOne([9]) == [1, 0]

#time complexity O(n)
#space complexity O(n)

if __name__ == '__main__':
    test_plus_one()
