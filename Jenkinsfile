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
                bat 'python -m venv venv'
                bat 'venv\\Scripts\\activate && pip install --upgrade pip'
                bat 'venv\\Scripts\\activate && pip install -r requirements.txt'
            }
        }

        stage('Run Selenium Tests') {
            steps {
                bat 'venv\\Scripts\\activate && pytest tests/test_login.py'
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
