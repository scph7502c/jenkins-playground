pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
    }

    stages {
        stage('Fetch code from GitHub') {
            steps {
                git branch: 'main', url: 'https://github.com/scph7502c/jenkins-playground.git'
            }
        }

        stage('Create venv and install dependencies') {
            steps {
                sh '''
                    python3 -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run tests') {
            steps {
                sh '''
                    . ${VENV_DIR}/bin/activate
                    pytest
                '''
            }
        }
    }
}

