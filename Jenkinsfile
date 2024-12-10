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
            // Exemple d'action à toujours exécuter
            echo 'Pipeline exécuté, nettoyage ou autres actions peuvent être effectuées ici.'
            // Vous pouvez ajouter ici des étapes comme nettoyer, notifier, ou autre
        }
    }
}
