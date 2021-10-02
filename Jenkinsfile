pipeline {
  agent any
  stages {
    stage('docker image') {
      parallel {
        stage('docker image') {
          steps {
            sh '''docker buildx create --use &&

docker buildx build --platform linux/amd64,linux/arm64,linux/arm/v7 -t dockerteun/stockbot:latest --push Site/.'''
          }
        }

        stage('whoami') {
          steps {
            sh 'whoami'
          }
        }

      }
    }

  }
}