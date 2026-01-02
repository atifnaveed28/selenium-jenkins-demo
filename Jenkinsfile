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
                // Create a virtual environment
                bat 'python -m venv venv'

                // Upgrade pip and install dependencies
                bat 'venv\\Scripts\\activate && pip install --upgrade pip'
                bat 'venv\\Scripts\\activate && pip install -r requirements.txt'
            }
        }

        stage('Run Selenium Tests') {
            steps {
                // Run your login test in headless mode
                bat 'venv\\Scripts\\activate && pytest D:\\All_Fiverr_Projects\\SDET Learning\\selenium-jenkins-demo\\tests\\test_login.py --headless'
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
