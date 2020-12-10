import unittest
from day5 import solve1, solve2

class TestIt(unittest.TestCase):
    
    def __init__(self, *args, **kwargs):
        super(TestIt, self).__init__(*args, **kwargs)
        self.puzzle_input = [
            'FBFBBFFRLR',
            'BFFFBBFRRR',
            'FFFBBBFRRR',
            'BBFFBBFRLL'
        ]

    def test_part1(self):
        answer = solve1(self.puzzle_input)
        self.assertEqual(answer, 820)

if __name__ == '__main__':
    unittest.main()