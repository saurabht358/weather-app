pipeline {
    agent any

    environment {
        DOCKER_HUB = "saurabht358"
        IMAGE_NAME = "weather-app"
    }

    stages {


        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $DOCKER_HUB/$IMAGE_NAME:latest .'
            }
        }

        stage('Push Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-cred', usernameVariable: 'USER', passwordVariable: 'PASS')]) {
                    sh 'echo $PASS | docker login -u $USER --password-stdin'
                    sh 'docker push $DOCKER_HUB/$IMAGE_NAME:latest'
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh 'kubectl apply -f deployment.yaml'
                sh 'kubectl apply -f service.yaml'
            }
        }
    }
}
