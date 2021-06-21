pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                sh '''echo "Pulling Repository"'''
                git branch: 'main', credentialsId: '08459a1a-4c01-43e3-adc8-e5b63c45116d', url: 'https://github.com/TomBrov/WorldOfGames'
                sh '''echo "Repository Pulled"
                      chmod 777 *
                      chmod 777 */*'''
            }
        }
        stage('Run') {
            steps {
                sh '''cd Dockerimage
                      pip install -r requirements.txt
                      cd ..
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
