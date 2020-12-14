import unittest
#import sys
#sys.path.append("C:\\Users\\nana-\\data_engineer_pjt")

from src.recommendations import recommendations

# from pathlib import Path


# ROOT = Path(__file__).resolve().parents[2]

class FlaskTest(unittest.TestCase):
    def setUp(self):
        self.sentence="hi"
  

    def tearDown(self):
        pass

    def test_recommendations(self):
        result=recommendations(self.sentence)
        self.assertEqual(len(result),20)

if __name__=='__main__':
    print('function test')
    unittest.main()
