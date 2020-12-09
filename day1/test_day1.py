import unittest
from day1 import solve1, solve2

class TestDay1(unittest.TestCase):

    def test_part1(self):
        puzzle_input = [
            1721,
            979,
            366,
            299,
            675,
            1456
        ]
        
        answer = solve1(puzzle_input)
        self.assertEqual(answer, 514579)
        
    def test_part2(self):
        puzzle_input = [
            1721,
            979,
            366,
            299,
            675,
            1456
        ]
        
        answer = solve2(puzzle_input)
        self.assertEqual(answer, 241861950)
        
if __name__ == '__main__':
    unittest.main()