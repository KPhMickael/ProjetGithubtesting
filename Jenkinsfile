pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/KPhMickael/ProjetGithubtesting.git'
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
        stage('Code Quality Check') {
            steps {
                script {
                    def pylintCommand = isUnix() ? 'python3 -m pylint' : 'python -m pylint'
                    def pylintOutput = "pylint-report.txt"
                    if (isUnix()) {
                        sh "${pylintCommand} --rcfile=pylintrc src/**/*.py > ${pylintOutput}"
                    } else {
                        bat "${pylintCommand} --rcfile=pylintrc src/**/*.py > ${pylintOutput}"
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
