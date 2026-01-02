pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/atifnaveed28/selenium-jenkins-demo'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Selenium Tests') {
            steps {
                sh 'pytest tests/test_login.py'
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
