pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/your-username/selenium-jenkins-demo.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Selenium Tests') {
            steps {
                sh 'pytest'
            }
        }
    }

    post {
        success {
            echo 'Login test passed'
        }
        failure {
            echo 'Login test failed'
        }
    }
}
