import unittest
import requests
import os
from bs4 import BeautifulSoup
#import sys
#sys.path.append("C:\\Users\\nana-\\data_engineer_pjt")

from src.recommendations import recommendations

# from pathlib import Path


# ROOT = Path(__file__).resolve().parents[2]

class FlaskTest(unittest.TestCase):
    def setUp(self):
        self.sentence="I will be re-tweeting some of your better, most imaginative and hopefully insightful tweets. Make them good (great)! Important stuff."
  

    def tearDown(self):
        pass

    def test_a_index(self):
        response = requests.get('http://localhost:5000')
        self.assertEqual(response.status_code, 200)

    def test_b_search(self):
        payload = {
            'sentence':self.sentence,
            'form_type':'recommendations'
        }

        response = requests.post('http://localhost:5000',data=payload)
        soup = BeautifulSoup(response.text, "html.parser")
        
        table=soup.find_all("tr")[:2]
        firstrow=str(table[1])
        result = "<tr id=\"7135\"> <td>7135</td> <td>\"@Natasha_tut13: @realDonaldTrump  I like to read your tweets and I am delighted with you, intelligent, decent, strong man!\"  Thanks.</td> </tr>"
        
        self.assertEqual(result, firstrow)

if __name__=='__main__':
    print('integration test')
    unittest.main()
