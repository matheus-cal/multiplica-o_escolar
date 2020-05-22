import unittest
from mult_escolar_matheus import multiplica

class test_multiplica(unittest.TestCase):

    def test_multiplica(self):
        self.assertEqual(multiplica('99999999', '88888888'), 8888888711111112)
        self.assertEqual(multiplica('0', '99999999'), 0)
        self.assertEqual(multiplica('99999999', '1'), 99999999)


if __name__ == '__main__':
    unittest.main()
