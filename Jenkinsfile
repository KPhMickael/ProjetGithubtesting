pipeline {
    agent any
    
    environment {
        PYTHON_ENV = 'C:/Python38'  // Adaptez selon votre installation Python
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
                    // Vérifier la version de Python et pip sur l'agent Jenkins
                    bat 'python --version'  // Vérifie la version de Python
                    bat 'pip --version'  // Vérifie la version de pip
                    
                    // Installer pytest directement sans requirements.txt
                    bat 'pip install pytest'  // Installe pytest directement
                }
            }
        }
        
        stage('Run Tests') {
            steps {
                script {
                    // Exécuter les tests avec pytest et générer un fichier XML
                    bat 'pytest --junitxml=results.xml'  // Exécution de pytest et génération du rapport
                }
            }
        }
        
        stage('Publish Test Results') {
            steps {
                // Publie les résultats de test sous forme de rapport JUnit
                junit '**/results.xml'  // Spécifie le chemin vers le fichier XML généré par pytest
            }
        }
    }

    post {
        always {
            echo 'Pipeline terminé.'
        }
    }
}
