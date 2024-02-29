import unittest

def str_to_bool(value):
    if not isinstance(value, str):
        raise AttributeError(f"{value} must be of type string")

    value = value.lower()
    true_values = ['y', 'yes']
    false_values = ['no', 'n']

    if value in true_values:
        return True
    if value in false_values:
        return False

class TestStrToBool(unittest.TestCase):

    def test_y_is_true(self):
        result = str_to_bool('y')
        self.assertTrue(result)

    def test_yes_is_true(self):
        result = str_to_bool('Yes')
        self.assertTrue(result)

    def test_invalid_input(self):
        with self.assertRaises(AttributeError):
            str_to_bool(1)

if __name__ == '__main__':
    unittest.main()
