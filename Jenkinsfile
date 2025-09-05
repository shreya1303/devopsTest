pipeline {
    agent any

    environment {
        PYTHON_VERSION = '3.11'
    }

    stages {
        stage('Checkout') {
            steps {
                echo '🔄 Checking out code...'
                checkout scm
            }
        }

        stage('Setup Python') {
            steps {
                echo '🐍 Setting up Python...'
                // Requires Jenkins plugin: "Python" or use sh with pyenv or docker
                sh '''
                    python3 --version
                    python3 -m venv venv
                    source venv/bin/activate
                    pip install --upgrade pip
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                echo '📦 Installing dependencies...'
                sh '''
                    source venv/bin/activate
                    pip install -r requirements.txt || true
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo '🧪 Running unit tests...'
                sh '''
                    source venv/bin/activate
                    python -m unittest test_calculator.py
                '''
            }
        }
    }

    post {
        always {
            echo '🧹 Cleaning up...'
            sh 'rm -rf venv'
        }
        success {
            echo '✅ Build succeeded!'
        }
        failure {
            echo '❌ Build failed!'
        }
    }
}
