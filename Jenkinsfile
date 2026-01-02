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
                bat '"C:\\Users\\Atif Naveed\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" -m venv venv'

                // Upgrade pip and install dependencies
                bat 'venv\\Scripts\\activate && "C:\\Users\\Atif Naveed\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" -m pip install --upgrade pip'
                bat 'venv\\Scripts\\activate && "C:\\Users\\Atif Naveed\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Run Selenium Tests') {
            steps {
                // Run your Selenium login test
                bat 'venv\\Scripts\\activate && "C:\\Users\\Atif Naveed\\AppData\\Local\\Programs\\Python\\Python312\\python.exe" -m pytest D:\\All_Fiverr_Projects\\SDET Learning\\selenium-jenkins-demo\\tests\\test_login.py'
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
