pipeline {
    agent any

    environment {
        DOCKER_IMAGE_NAME = 'paas-client-lib'
    }

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build(DOCKER_IMAGE_NAME, '.')
                }
            }
        }

        stage('Run tests') {
            steps {
                script {
                    docker.image(DOCKER_IMAGE_NAME).inside {
                        sh './run_tests.sh'
                    }
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
        failure {
            echo "Tests failed!"
        }
        success {
            echo "Tests passed!"
        }
    }
}
