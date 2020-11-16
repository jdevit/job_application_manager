import unittest

class DatabaseTest(unittest.TestCase):

    def test_insert_format_count(self):
        test_dict = {}
        correct_dict = {'role': '0', 'company': '0', 'date': '0', 'website': '0', 'status': '0'}

        self.assertEqual(len(test_dict), len(correct_dict))
