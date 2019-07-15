from unittest import TestCase


def max_loss(p):

    # deal with small lists
    if len(p) < 2:
        return 0

    high = p[0]
    low = p[0]
    maxloss = 0
    for i in range(0, len(p)):

        if p[i] > high:
            # found new high, reset lowest point
            high = p[i]
            low = p[i]

        if p[i] < low:
            # found new low, check if new maxloss
            low = p[i]
            if high - low > maxloss:
                maxloss = high - low
    return maxloss


'''
___edge cases___

zero/one item list
very large list
negative values in list
constant list - not a problem
increasing list 
'''


class TestSuite(TestCase):

    def full_tests(self):

        standard1 = [0, 2, 3, 2, 0, 5, 4]
        self.assertEqual(max_loss(standard1), 3)
        standard2 = [5, 0, 3, 0, 2, 3, 0]  # max at left edge
        self.assertEqual(max_loss(standard2), 5)
        standard3 = [3, 3, 3, 3, 3, 2]  # max at right edge
        self.assertEqual(max_loss(standard3), 1)
        standard4 = [10, 5, 10, 6]  # loss of 5 should not be replaced by loss of 4
        self.assertEqual(max_loss(standard4), 5)

        decimals = [0, 2.5, 5.5, 3.2, 1.2, 4.535, 3.7887]
        self.assertEqual(max_loss(decimals), 4.3)

        empty = []
        self.assertEqual(max_loss(empty), 0)

        constant = [2, 2, 2, 2, 2, 2]
        self.assertEqual(max_loss(constant), 0)

        increasing = [0, 1, 2, 3, 4, 5]
        self.assertEqual(max_loss(increasing), 0)

        print("all tests passed")


if __name__ == "__main__":
    test = TestSuite()
    test.full_tests()
