pipeline {  
    environment {
        registry = "calvarado2004/django-rest-sample"
        registryCredential = 'dockerhub'
        dockerImage = ''
        dockerHome = tool 'docker'
        PATH = "${dockerHome}/bin:${PATH}"
    } 
    agent any

    stages {
        stage('Cloning Git Repository') {
            steps {
                git 'https://github.com/calvarado2004/django-api-rest.git'
            }
            
        }
        stage('Building Docker image') {
            steps{
                script {
                    dockerImage = docker.build registry + ":$BUILD_NUMBER"
                }
            }
        }
        stage('Deploy Docker Image') {
            steps{
                script {
                    withCredentials(
                        [usernamePassword(
                                credentialsId: 'dockerhub', passwordVariable: 'pass', usernameVariable: 'user'
                            )
                        ]
                    ) { 
                        sh "docker login -u ${user} -p ${pass}"
                        dockerImage.push()
                    }
                }
            }
        }
    }
}