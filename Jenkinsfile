pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/atifnaveed28/selenium-jenkins-demo.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
                // Create virtual environment
                bat 'python -m venv venv'

                // Upgrade pip properly
                bat 'venv\\Scripts\\python.exe -m pip install --upgrade pip'

                // Install dependencies
                bat 'venv\\Scripts\\python.exe -m pip install -r requirements.txt'
            }
        }

        stage('Run Selenium Tests') {
            steps {
                // Run Selenium test (workspace-relative path)
                bat 'venv\\Scripts\\python.exe -m pytest tests/test_login.py'
            }
        }
    }

    post {
        success {
            echo 'Selenium login test passed!'
        }
        failure {
            echo 'Selenium login test failed!'
        }
    }
}
