def build_app(){
  bat 'docker-compose up -d --build'
}

def stress_test(){
    echo 'manual stress test, go to http://localhost:8089/'
    bat 'locust -f locustfile.py'
}

def user_acceptance(){
    input 'did the app resist to the load ?'
}

def test_app(){
    stress_test()
    user_acceptance()
}

def down_app(){
  bat 'docker-compose down'
}

return this
