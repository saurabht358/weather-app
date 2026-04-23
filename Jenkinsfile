pipeline {
    agent any

    environment {
        IMAGE = "saurabht358/weather-app"
        TAG = "${BUILD_NUMBER}"
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/saurabht358/weather-app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat "docker build -t %IMAGE%:%TAG% ."
            }
        }

        stage('Push Image') {
            steps {
                bat "docker push %IMAGE%:%TAG%"
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                bat """
                kubectl set image deployment/weather-app weather-app=saurabht358/weather-app:%BUILD_NUMBER%
                """
            }
        }
    }
}