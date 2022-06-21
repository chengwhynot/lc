from twosum import solution

def test_twoSum_01():
    data = [1,2,3,2,5]
    actural = solution.twoSum(data, 5)
    expected1 = [2,3]
    expected2 = [1,2]
    assert actural == expected1 or actural == expected2
def test_twoSum_02():
    result = solution.twoSum([1,2,3,4,5,6], 7)
    expected1 = [0,5]
    expected2 = [2,3]
    assert (expected1 == result or expected2 == result) 

def test_twoSum_empty():
    result = solution.twoSum([], 7)
    expected = [-1,-1]
    assert (expected == result)

def test_twoSum_not_exist():
    result = solution.twoSum([1,2,3,4,5,6], 12)
    expected = [-1, -1]
    assert (expected == result)

def test_without_order():
    result = solution.twoSum([7,3,4,2], 5)
    expected = [1,3]
    assert (expected == result)

def test_with_dup_values():
    result = solution.twoSum([7,3,4,3], 7)
    expected1 = [1,2]
    expected2 = [2,3]
    assert (expected1 == result or expected2 == result)
