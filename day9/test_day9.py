import unittest
from day9 import solve1, solve2

class TestIt(unittest.TestCase):
    
    def __init__(self, *args, **kwargs):
        super(TestIt, self).__init__(*args, **kwargs)
        self.puzzle_input = [
            35,
            20,
            15,
            25,
            47,
            40,
            62,
            55,
            65,
            95,
            102,
            117,
            150,
            182,
            127,
            219,
            299,
            277,
            309,
            576
        ]
        
        
    def test_part1(self):
        answer = solve1(self.puzzle_input, 5)
        self.assertEqual(answer, 127)

    def test_part2(self):
        answer = solve2(self.puzzle_input, 5)
        self.assertEqual(answer, 62)

if __name__ == '__main__':
    unittest.main()