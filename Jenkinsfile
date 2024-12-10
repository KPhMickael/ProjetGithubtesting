pipeline {
    agent any
    
    environment {
        PYTHON_ENV = 'C:/Python38'  // Adaptez selon votre installation
    }
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Install Dependencies') {
            steps {
                script {
                    bat 'pip install -r requirements.txt'  // Commande pour Windows
                }
            }
        }
        
        stage('Run Tests') {
            steps {
                script {
                    bat 'pytest --junitxml=results.xml'  // Commande pour Windows
                }
            }
        }
        
        stage('Publish Test Results') {
            steps {
                junit '**/results.xml'
            }
        }
    }

    post {
        always {
    echo 'Le pipeline est terminé.'
    // Vous pouvez ajouter ici une étape pour envoyer un message ou nettoyer des fichiers temporaires
        }
    }
}
