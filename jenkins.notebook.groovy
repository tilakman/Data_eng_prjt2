def build_app(){
  bat 'C:/Users/nana-/anaconda3/python.exe src/train.py'
}


def test_app(){
  bat 'C:/Users/nana-/anaconda3/python.exe test_recommendations.py'
}

def release_app(){
    echo 'you can merge the notebook branch on the develop branch'
}

return this
