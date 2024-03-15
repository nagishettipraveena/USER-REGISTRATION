pipeline {
    agent any
    
    stages {
        stage('Build') {
            steps {
                // Example: Build your project
                echo 'mvn clean install'
            }
        }
        stage('Test') {
            steps {
                // Example: Run tests
                echo 'mvn test'
            }
        }
        stage('Deploy') {
            steps {
                // Example: Deploy your application
                echo 'hello.py'
            }
        }
    }
    
    post {
        success {
            // Example: Send notification on success
            echo 'Pipeline succeeded! Sending notification...'
            // notifySuccess()
        }
        failure {
            // Example: Send notification on failure
            echo 'Pipeline failed! Sending notification...'
            // notifyFailure()
        }
    }
}
