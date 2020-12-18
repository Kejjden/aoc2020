import unittest
from day15 import solve

class TestIt(unittest.TestCase):
    

    def test_part1(self):
        inputs = [
            {'input': ['0', '3', '6'], 'answer': 436},
            {'input': ['1', '3', '2'], 'answer': 1},
            {'input': ['2', '1', '3'], 'answer': 10},
            {'input': ['1', '2', '3'], 'answer': 27},
            {'input': ['2', '3', '1'], 'answer': 78},
            {'input': ['3', '2', '1'], 'answer': 438},
            {'input': ['3', '1', '2'], 'answer': 1836}
        ]
        
        for i in inputs:
            answer = solve(i['input'], 2020)
            self.assertEqual(answer, i['answer'])

    def test_part2(self):
        inputs = [
            {'input': ['0', '3', '6'], 'answer': 175594},
        ]
        
        for i in inputs:
            answer = solve(i['input'], 30000000)
            self.assertEqual(answer, i['answer'])

if __name__ == '__main__':
    unittest.main()
