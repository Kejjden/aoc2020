import unittest
from day3 import solve1, solve2

class TestIt(unittest.TestCase):
    
    def __init__(self, *args, **kwargs):
        super(TestIt, self).__init__(*args, **kwargs)
        self.puzzle_input = [
            '..##.......',
            '#...#...#..',
            '.#....#..#.',
            '..#.#...#.#',
            '.#...##..#.',
            '..#.##.....',
            '.#.#.#....#',
            '.#........#',
            '#.##...#...',
            '#...##....#',
            '.#..#...#.#'
        ]

    def test_part1(self):
        answer = solve1(self.puzzle_input)
        self.assertEqual(answer, 7)

    def test_part2(self):
        answer = solve2(self.puzzle_input)
        self.assertEqual(answer, 336)

if __name__ == '__main__':
    unittest.main()