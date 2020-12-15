import unittest
from day13 import solve1, solve2

class TestIt(unittest.TestCase):
    
    def __init__(self, *args, **kwargs):
        super(TestIt, self).__init__(*args, **kwargs)
        self.puzzle_input = [
            '939',
            '7,13,x,x,59,x,31,19'
        ]
        
        
    def test_part1(self):
        answer = solve1(self.puzzle_input)
        self.assertEqual(answer, 295)

    def test_part2(self):
        answer = solve2(self.puzzle_input)
        self.assertEqual(answer, 1068781)

if __name__ == '__main__':
    unittest.main()