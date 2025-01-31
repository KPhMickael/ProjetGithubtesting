pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/KPhMickael/jenkinsrepo.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'python3 -m pip install -r requirements.txt'
                    } else {
                        bat 'python -m pip install -r requirements.txt'
                    }
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    if (isUnix()) {
                        sh 'python3 -m pytest script.py'
                    } else {
                        bat 'python -m pytest script.py'
                    }
                }
            }
        }
        stage('Code Quality Check') {
            steps {
                script {
                    def pylintCommand = isUnix() ? 'python3 -m pylint' : 'python -m pylint'
                    def pylintOutput = "pylint-report.txt"
                    if (isUnix()) {
                        sh "${pylintCommand} script.py > ${pylintOutput}"
                    } else {
                        bat "${pylintCommand} script.py > ${pylintOutput}"
                    }
                }
            }
            post {
                always {
                    archiveArtifacts artifacts: 'pylint-report.txt', allowEmptyArchive: true
                }
            }
        }
    }
}
