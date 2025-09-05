pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/shreya1303/devopsTest.git'
            }
        }
        stage('Build') {
            steps {
                sh 'echo Building app...'
                sh 'python3 --version || python --version'
                sh 'python3 calculator.py || python calculator.py'
            }
    }
        stage('Test') {
            steps {
                sh 'echo Running tests...'
                sh 'python3 -m unittest calculator_test.py'
            }
        }
    }
}
