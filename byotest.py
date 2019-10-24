def test_are_equal(actual, expected):
    assert expected == actual, "Expected {0}, got {1}".format(expected, actual)

def test_not_equal(a, b):
    assert a != b, "Expected {0} to equal to {1}".format(a, b)

def test_is_in(collection, item):
    assert item in collection, "{0} does not contain {1}".format(collection, item)
    
def test_not_in(item, collection):
    assert(item not in collection), "{0} is in {1}".format(item, collection)

def test_between(lower_limit, upper_limit, num):
    assert(lower_limit <= num <= upper_limit), "{0} is not between {1} and {2}".format(num, lower_limit, upper_limit)

test_are_equal(1, 2)
test_not_equal("1", 1)
test_is_in([1, 3, 4], 2)
test_not_in(2, [1,2,3,4])
test_between(1, 5, 6)
print("Passed all tests")