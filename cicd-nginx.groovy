#!/usr/bin/env groovy

//Author: Carlos Alvarado
//Jenkins Pipeline to handle the Continuous Integration and Continuous Deployment on Okteto.
//Prerequisites: you should install the Custom tools plugin on Jenkins, ... 
//...get the okteto CLI and Kubectl. You also need to get your Okteto Token and save it on a Jenkins Credential


node {
    
    env.OKTETO_DIR = tool name: 'okteto', type: 'com.cloudbees.jenkins.plugins.customtools.CustomTool'
    env.HOME = "${WORKSPACE}"
    env.CONTAINER_IMAGE = 'registry.cloud.okteto.net/calvarado2004/backend-django'
    env.KUBECTL_DIR = tool name: 'kubectl', type: 'com.cloudbees.jenkins.plugins.customtools.CustomTool'
    env.GIT_PROJECT = 'https://github.com/calvarado2004/django-api-rest.git'
    
    stage ('Prepare Environment with Okteto ') {
        withCredentials([string(credentialsId: 'okteto-token', variable: 'SECRET')]) {
            cleanWs deleteDirs: true
            def output = sh returnStdout: true, script: '''
            ${OKTETO_DIR}/okteto login --token ${SECRET}
            '''
            println output
        }
    }
    
    stage ('Download the source code from GitHub'){
            git url: "${GIT_PROJECT}"
    }
    
    
    stage('Deploy Nginx to okteto'){
        withCredentials([string(credentialsId: 'okteto-token', variable: 'SECRET')]) {
            def output = sh returnStdout: true, script: '''
            ${OKTETO_DIR}/okteto login --token ${SECRET}
            cd ${HOME}/nginx-k8s
            ${OKTETO_DIR}/okteto namespace
            ${KUBECTL_DIR}/kubectl apply -f kubernetes.yaml
            ${KUBECTL_DIR}/kubectl rollout status deployment.apps/nginx-api-rest
            '''
            println output
        }
    }
}