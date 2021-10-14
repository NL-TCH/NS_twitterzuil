pipeline {
  agent any
  stages {
    stage('Cloning Git') {
      steps {
        git(url: 'https://github.com/NL-TCH/NS_twitterzuil.git', branch: 'jenkins_branch', credentialsId: 'github_usertoken')
      }
    }

    stage('Building image') {
      steps {
        script {
          dockerImage = docker.build(imagename, "-f Site/Dockerfile .")
        }

      }
    }

    stage('Deploy Image') {
      steps {
        script {
          docker.withRegistry( '', registryCredential ) {
            dockerImage.push("$BUILD_NUMBER")
            dockerImage.push('latest')

          }
        }

      }
    }

    stage('Remove Unused docker image') {
      steps {
        sh "docker rmi $imagename:$BUILD_NUMBER"
        sh "docker rmi $imagename:latest"
      }
    }

    stage('error') {
      steps {
        sh '''sudo su

&& ls &&
pwd &&
tree &&
docker-compose up -d --force-recreate --build --no-deps --remove-orphans'''
      }
    }

  }
  environment {
    imagename = 'dockerteun/ns'
    registryCredential = 'docker_usertoken'
    args = 'Site/.'
  }
}