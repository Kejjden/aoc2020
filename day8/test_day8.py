import unittest
from day8 import solve1, solve2

class TestIt(unittest.TestCase):
    
    def __init__(self, *args, **kwargs):
        super(TestIt, self).__init__(*args, **kwargs)
        self.puzzle_input = [
            'nop +0',
            'acc +1',
            'jmp +4',
            'acc +3',
            'jmp -3',
            'acc -99',
            'acc +1',
            'jmp -4',
            'acc +6'
        ]
        
        
    def test_part1(self):
        answer = solve1(self.puzzle_input)
        self.assertEqual(answer, 5)

    def test_part2(self):
        answer = solve2(self.puzzle_input)
        self.assertEqual(answer, 8)

if __name__ == '__main__':
    unittest.main()