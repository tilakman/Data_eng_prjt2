pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        echo 'Building Docker Images'
        bat 'docker build -t app .'
      }
    }

    stage('Test') {
          steps {
            echo 'Starting docker services'
          }
        }

        stage('Run Docker Image') {
          steps {
            echo 'Running Flask app'
            bat 'docker run -p 5000:5000 -d --name app_c app'
          }
        }

    stage('Testing') {
      steps {
        echo 'Deploying Now'
        bat 'python test_app.py'
      }
    }

    stage('Stop Containers') {
      parallel {
        stage('Stop Containers') {
          steps {
            bat 'docker rm -f app_c'
            bat 'docker rmi app'
          }
        }

        stage('error') {
          steps {
            bat '#docker stop redis'
            bat '#docker rm redis'
          }
        }

      }
    }

  }
}
