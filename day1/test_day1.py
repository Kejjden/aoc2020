import unittest
from day1 import solve1, solve2

class TestIt(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestIt, self).__init__(*args, **kwargs)
        self.puzzle_input = [
            1721,
            979,
            366,
            299,
            675,
            1456
        ]
        
    def test_part1(self):
        answer = solve1(self.puzzle_input)
        self.assertEqual(answer, 514579)
        
    def test_part2(self):
        answer = solve2(self.puzzle_input)
        self.assertEqual(answer, 241861950)
        
if __name__ == '__main__':
    unittest.main()