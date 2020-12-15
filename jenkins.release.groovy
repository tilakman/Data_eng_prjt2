def build_app(){
  bat 'docker-compose up -d --build'
}

def e2e_test(){
  echo 'release-specific testing here'
  bat 'C:/Users/nana-/Anaconda3/python.exe test_app.py'
  bat 'C:/Users/nana-/Anaconda3/python.exe test_recommendations.py'
}
}
def user_acceptance(){
  input "proceed with deployment to live?"
}

def test_app(){
  e2e_test()
  user_acceptance()
}

def down_app(){
  sh 'docker-compose down'
}


def live_app(){
  echo 'merge with main'
}

return this






def down_app(){
  bat 'docker-compose down'
}

return this
