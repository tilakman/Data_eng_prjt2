pipeline {
  agent any
  stages {
    stage('Build') {
      steps {
        echo 'Building Docker Images'
        sh 'docker build -t app .'
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
            sh 'docker run -p 5000:5000 -d --name app_c app'
          }
        }
      }
    }

    stage('Testing') {
      steps {
        echo 'Deploying Now'
        sh 'python test_app.py'
      }
    }

    stage('Stop Containers') {
      parallel {
        stage('Stop Containers') {
          steps {
            sh 'docker rm -f app_c'
            sh 'docker rmi app'
          }
        }

        stage('error') {
          steps {
            sh '#docker stop redis'
            sh '#docker rm redis'
          }
        }

      }
    }

  }
}
