#!/usr/bin/python3

#intersection of two arrays 2
def intersect(nums1, nums2):
    dict = {}
    result = []

    for n in nums1:
        dict[n] = dict.get(n, 0) + 1

    for n in nums2:
        if n in dict and dict[n] > 0:
            result.append(n)
            dict[n] -= 1

    return result

def test_intersect():
    assert intersect([1, 2, 2, 1], [2, 2]) == [2, 2]
    assert intersect([4, 9, 5], [9, 4, 9, 8, 4]) == [9, 4]

#time complexity
#space complexity

if __name__ == '__main__':
    test_intersect()
