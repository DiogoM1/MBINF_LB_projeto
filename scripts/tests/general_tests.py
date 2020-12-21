import unittest
from ..general import time_stamping

class MyTestCase(unittest.TestCase):
    def test_time_stamping(self):
        self.assertEqual(time_stamping("../../data/markdown.md"), "../../data/markdown_2020-12-20.md")


if __name__ == '__main__':
    unittest.main()
