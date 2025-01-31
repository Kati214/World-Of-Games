pipeline {
    agent {
        docker {
            image 'docker:lts'
            args '--privileged  -v /var/run/docker.sock:/var/run/docker.sock'
        } 
    }

    environment {
        DOCKER_IMAGE = "kati2070/world-of-games:latest"
        CONTAINER_NAME = "app_container"
        DUMMY_FILE = "Scores.txt"
    }
    stages {
        stage('Checkout'){
            steps{
                git branch: 'main', url: 'https://github.com/Kati214/World-Of-Games.git'
            }

        }

        stage('Build'){
            steps{
                echo 'Building Docker image using docker-compose... '
                sh 'docker-compose --version' 
                sh "docker-compose build"
            }
        }

        stage('Run'){
            steps{
                echo 'Running the application using docker-compose...'
                sh "docker-compose up -d"
            }
        }

        stage('Test'){
            steps{
                echo 'Running tests with e2e.py...'
                script{
                    try{
                        sh "python3 e2e.py"
                    }
                    catch (Exception e){
                        echo 'Tests failed, stopping containers...'
                        sh "docker-compose logs"
                        sh "docker-compose down"
                        error "Tests failed: ${e.getMessage()}"
                    }
                    
                }
            }
        }

        stage('Finalize'){
            steps {
                echo 'Stopping containers and pushing the Docker image...'
                sh "docker-compose down"
                sh "docker login -u kati2070 -p dvbirve170010"
                sh "docker-compose push"

            }
        }
    }

    post {
        always {
            echo 'Cleaning up resources...'
            sh "docker-compose down || true"
        }
        success {
            echo 'Pipeline completed successfully!'
        }

        failure {
             echo 'Pipeline failed. Check logs for details.'
        }
    }
}