import unittest
from day10 import solve1, solve2, get_jolt_differences

class TestIt(unittest.TestCase):
    
    def __init__(self, *args, **kwargs):
        super(TestIt, self).__init__(*args, **kwargs)
        self.puzzle_input = [
            16,
            10,
            15,
            5,
            1,
            11,
            7,
            19,
            6,
            12,
            4
        ]
        
        
    def test_part1(self):
        answer = get_jolt_differences(self.puzzle_input)
        self.assertEqual(answer[1], 7)
        
    def test_part1_2(self):
        puzzle_input = [
            28,
            33,
            18,
            42,
            31,
            14,
            46,
            20,
            48,
            47,
            24,
            23,
            49,
            45,
            19,
            38,
            39,
            11,
            1,
            32,
            25,
            35,
            8,
            17,
            7,
            9,
            4,
            2,
            34,
            10,
            3
        ]
        answer = get_jolt_differences(puzzle_input)
        self.assertEqual(answer[1], 22)

    def test_part2(self):
        answer = solve2(self.puzzle_input)
        self.assertEqual(answer, 8)

if __name__ == '__main__':
    unittest.main()