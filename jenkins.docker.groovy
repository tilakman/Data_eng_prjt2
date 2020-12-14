def build_app(){
  bat 'docker-compose up -d --build'
}

def test_app(){
  bat 'C:/Users/nana-/Anaconda3/python.exe test_app.py'
}

def down_app(){
  bat 'docker-compose down'
}

return this
