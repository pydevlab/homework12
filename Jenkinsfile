pipeline {
  environment {
      registry = "pydevlab/testbuild"
      registryCredential = 'dockerhub-cred'
      dockerImage = ''
  }
  agent any
  stages {
      stage('Cloning git repository') {
          steps {
              git branch: 'main', url: 'https://github.com/pydevlab/homework12.git'
          }
      }
      stage('Building image') {
          steps{
              script {
                  dockerImage = docker.build registry + ":$BUILD_NUMBER"
              }
         }
      }
      stage('Push image to DockerHub') {
          steps{
              script {
                  docker.withRegistry( '', registryCredential ) {
                      dockerImage.push()
					  dockerImage.push('latest')
 
                  }
              }
          }
      }
      stage('Deploy to staging') {
          steps {
	      sh "docker-compose down"
	      sh "docker-compose up -d"
        }
     }
	  
  }
}
