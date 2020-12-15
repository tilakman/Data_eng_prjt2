def build_app(){
  bat 'docker-compose up -d --build'
}

def stress_test(){
    echo 'manual stress test, launch locust -f locustfile.py and go to http://localhost:8089/'
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

def release_app(){
    echo 'you can merge the develop branch on the release branch'
}

return this
