import unittest
from day14 import solve1, solve2

class TestIt(unittest.TestCase):
    
    def __init__(self, *args, **kwargs):
        super(TestIt, self).__init__(*args, **kwargs)
        self.puzzle_input = [
            'mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X',
            'mem[8] = 11',
            'mem[7] = 101',
            'mem[8] = 0'
        ]
        
        
    def test_part1(self):
        answer = solve1(self.puzzle_input)
        self.assertEqual(answer, 165)

    def test_part2(self):
        puzzle_input = [
            'mask = 000000000000000000000000000000X1001X',
            'mem[42] = 100',
            'mask = 00000000000000000000000000000000X0XX',
            'mem[26] = 1'
        ]
        answer = solve2(puzzle_input)
        self.assertEqual(answer, 208)

if __name__ == '__main__':
    unittest.main()