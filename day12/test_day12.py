import unittest
from day12 import solve1, solve2

class TestIt(unittest.TestCase):
    
    def __init__(self, *args, **kwargs):
        super(TestIt, self).__init__(*args, **kwargs)
        self.puzzle_input = [
            'F10',
            'N3',
            'F7',
            'R90',
            'F11'
        ]
        
        
    def test_part1(self):
        answer = solve1(self.puzzle_input)
        self.assertEqual(answer, 25)

    def test_part2(self):
        answer = solve2(self.puzzle_input)
        self.assertEqual(answer, 286)

if __name__ == '__main__':
    unittest.main()