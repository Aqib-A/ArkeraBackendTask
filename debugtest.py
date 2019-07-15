from unittest import TestCase


def increment_dictionary_values(d, i):
    d1 = d.copy()
    for k, v in d.items():
        d1[k] = v + i
    return d1


class TestIncrementDictionaryValues(TestCase):
    def test_increment_dictionary_values(self):
        d = {'a': 1}
        dd = increment_dictionary_values(d,1)
        ddd = increment_dictionary_values(d, -1)
        self.assertEqual(dd['a'], 2)
        self.assertEqual(ddd['a'], 0)


if __name__ == "__main__":
    test = TestIncrementDictionaryValues()
    test.test_increment_dictionary_values()
