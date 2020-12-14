import unittest
import requests
import os
#import sys
#sys.path.append("C:\\Users\\nana-\\data_engineer_pjt")

from src.recommendations import recommendations

# from pathlib import Path


# ROOT = Path(__file__).resolve().parents[2]

def post_stress():
    payload = {
            'sentence':'hi',
        }
    for i in range(0,1000):
        response = requests.post('http://localhost:5000',data=payload)


if __name__=='__main__':
    print('stress test')
    post_stress()
