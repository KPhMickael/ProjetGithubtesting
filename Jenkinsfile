pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/user/repo.git'
            }
        }
        stage('Install dependencies') {
            steps {
                sh '''
                python3 -m venv venv
                source venv/bin/activate
                pip install -r requirements.txt
                '''
            }
        }
        stage('Run Tests') {
            steps {
                sh 'source venv/bin/activate && pytest --junitxml=report.xml'
            }
        }
        stage('Publish Test Results') {
            steps {
                junit 'report.xml'
            }
        }
    }
}
