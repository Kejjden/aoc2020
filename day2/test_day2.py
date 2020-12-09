import unittest
from day2 import solve1, solve2

class TestIt(unittest.TestCase):

    def test_part1(self):
        puzzle_input = [
            '1-3 a: abcde',
            '1-3 b: cdefg',
            '2-9 c: ccccccccc'
        ]
        
        answer = solve1(puzzle_input)
        self.assertEqual(answer, 2)
        
    def test_part2(self):
        puzzle_input = [
            '1-3 a: abcde',
            '1-3 b: cdefg',
            '2-9 c: ccccccccc'
        ]
        
        answer = solve2(puzzle_input)
        self.assertEqual(answer, 1)
        
if __name__ == '__main__':
    unittest.main()