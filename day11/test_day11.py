import unittest
from day11 import solve1, solve2, apply_new_rules

class TestIt(unittest.TestCase):
    
    def __init__(self, *args, **kwargs):
        super(TestIt, self).__init__(*args, **kwargs)
        self.puzzle_input = [
            'L.LL.LL.LL',
            'LLLLLLL.LL',
            'L.L.L..L..',
            'LLLL.LL.LL',
            'L.LL.LL.LL',
            'L.LLLLL.LL',
            '..L.L.....',
            'LLLLLLLLLL',
            'L.LLLLLL.L',
            'L.LLLLL.LL'
        ]
        
        
    def test_part1(self):
        answer = solve1(self.puzzle_input)
        self.assertEqual(answer, 37)

    def test_part2(self):
        answer = solve2(self.puzzle_input)
        self.assertEqual(answer, 26)

if __name__ == '__main__':
    unittest.main()