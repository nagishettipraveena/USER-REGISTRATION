pipeline {
    agent any
    
    stages {
        stage('Build') {
            steps {
                // Example: Build your project
                sh 'mvn clean install'
            }
        }
        stage('Test') {
            steps {
                // Example: Run tests
                sh 'mvn test'
            }
        }
        stage('Deploy') {
            steps {
                // Example: Deploy your application
                sh 'hello.py'
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
