from twosum import solution

def test_twoSum_01():
    data = [1,2,3,2,5]
    actural = solution.twoSum(data, 5)
    expected1 = [2,3]
    expected2 = [1,2]
    assert actural == expected1 or actural == expected2