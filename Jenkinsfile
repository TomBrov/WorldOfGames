pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                sh '''echo "Pulling Repository"'''
                git branch: 'dev', credentialsId: 'dbcab98a-98f1-44d9-a438-bc6ed51e8ce5', url: 'https://github.com/TomBrov/WorldOfGames'
                sh '''echo "Repository Pulled"
                      chmod 777 *'''
            }
        }
        stage('Run') {
            steps {
                sh '''pip install -r requirements.txt
                      docker-compose up --build -d'''
            }
        }
        stage('Test') {
            steps {
                sh '''cd tests
                      chmod +x *
                      python ./e2e.py'''
            }
        }
        stage('Finalize') {
            steps {
                sh ''' docker-compose down '''
            }
        }
    }
}