import unittest
from Models.InterBahis import InterBahis

class InterBahisUnitTest(unittest.TestCase):

    instance = InterBahis("http://interbahis246.com")

    def setUp(self):
        pass

    def test_inter_bahis_init_cookie(self):
        self.assertEqual(self.instance.headers["Cookie"],"")


if __name__ == '__main__':
    unittest.main()