pipeline {
  agent any
  stages {
    stage('docker image') {
      steps {
        sh 'sudo docker buildx build --platform linux/amd64,linux/arm64,linux/arm/v7 -t dockerteun/stockbot:latest --push Site/.'
      }
    }

  }
}