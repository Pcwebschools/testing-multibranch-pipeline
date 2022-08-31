pipeline {
    agent any
    stages {
        stage('Stage 1') {
            steps {
                echo 'Hello world!'
            }
        }
        stage('Stage TAG_NAME') {
            steps {
                echo env.TAG_NAME
            }
        }
    }
}
