pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/atifnaveed28/selenium-jenkins-demo.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run Selenium Tests') {
            steps {
                bat 'pytest tests/test_login.py'
            }
        }
    }

    post {
        success {
            echo 'Selenium tests passed!'
        }
        failure {
            echo 'Selenium tests failed!'
        }
    }
}
