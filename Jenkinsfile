pipeline {
    agent any

    environment {
        PYTHON_ENV = 'venv'
	WORKSPACE_DIR = 'C:\\Jenkins\\workspace'
        TEST_RESULTS_DIR = 'C:\\Jenkins'  // Dossier pour stocker les résultats
    }
    stages {
	stage('Checkout') {
            steps {
                script {
                    try {
                        checkout scm  // Vas chercher code github
                    } catch (Exception e) {
                        error "echec checkout : ${e}"
                    }
                }
            }
        }
        stage('PythonEnvironement') {
            steps {
                script { 
                    bat 'python -m venv %PYTHON_ENV%'
                    bat '%PYTHON_ENV%\\Scripts\\pip install -r requirements.txt'
                }
            }
        }
        stage('Runtest') {
            steps {
                script { 
                    bat '%PYTHON_ENV%\\Scripts\\pytest --maxfail=1 --disable-warnings -q --junitxml=%TEST_RESULTS_DIR%\\results.xml'
                }
            }
        }
        stage('CreationArtefact') {
            steps {
                script {
                    if (fileExists('%TEST_RESULTS_DIR%\\results.xml')) {
                        archiveArtifacts artifacts: '%TEST_RESULTS_DIR%\\results.xml', allowEmptyArchive: true // Creation de artefact
                    } else {
                        error "Le fichier results.xml n'a pas été trouvé."
                    }
                }
            }
        }
    }
}
