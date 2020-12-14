import unittest
from src.recommendations import recommendations


class FlaskTest(unittest.TestCase):
    def setUp(self):
        self.sentence="hi"
  

    def tearDown(self):
        pass

    def test_recommendations(self):
        result=recommendations(self.sentence)
        print("sentence : ",self.sentence)
        print("result : ",result)
        self.assertEqual(len(result),20)

if __name__=='__main__':
    print('function test')
    unittest.main()
