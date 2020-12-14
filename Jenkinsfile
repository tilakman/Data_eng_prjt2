def groovyfile
pipeline{
  agent any

  stages {
	  stage ('Build Scripe'){
	  	steps{
			script{
				 def filename = 'jenkins.' + env.BRANCH_NAME + '.groovy'
				 groovyfile = load filename
			}
		}
	}

    stage('train model'){
      steps{
        script{
          groovyfile.build_app()
        }
      }
    }
    stage('test model'){
      steps{
        script{
          groovyfile.test_app()
        }
      }
    }
    }
}
