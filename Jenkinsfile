pipeline {
    agent any
    
    environment {
        PYTHON_ENV = 'C:/Python38'  // Adaptez selon votre installation
    }
    
    stages {
        stage('Checkout') {
            steps {
                // Cloner le dépôt Git
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                // Installer les dépendances nécessaires avec pip
                script {
                    bat 'pip install -r requirements.txt'  // Commande pour Windows
                }
            }
        }

        stage('Run Tests') {
            steps {
                // Exécuter pytest et générer un rapport XML
                script {
                    bat 'pytest --junitxml=results.xml'  // Commande pour Windows
                }
            }
        }

        stage('Publish Test Results') {
            steps {
                // Publier les résultats des tests
                junit '**/results.xml'
            }
        }
    }

    post {
        always {
            // Actions à effectuer après l'exécution, comme nettoyer
        }
    }
}
