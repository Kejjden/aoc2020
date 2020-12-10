import unittest
from day6 import solve1, solve2

class TestIt(unittest.TestCase):
    
    def __init__(self, *args, **kwargs):
        super(TestIt, self).__init__(*args, **kwargs)
        self.puzzle_input = [
            'abc',
            '',
            'a',
            'b',
            'c',
            '',
            'ab',
            'ac',
            '',
            'a',
            'a',
            'a',
            'a',
            '',
            'b'
        ]

    def test_part1(self):
        answer = solve1(self.puzzle_input)
        self.assertEqual(answer, 11)

    def test_part2(self):
        answer = solve2(self.puzzle_input)
        self.assertEqual(answer, 6)

if __name__ == '__main__':
    unittest.main()