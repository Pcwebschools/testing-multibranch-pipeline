def gitTag = null
pipeline {
    agent any
    stages {
        stage('Stage 1') {
            steps {
                echo 'Hello world! from stage 1'
            }
        }
        stage('Stage 2') {
            steps {
                echo 'Hello world! from stage 2'
            }
        }
        stage('Stage TAG_NAME') {
            when {
                expression {
                    TAG_NAME != null
                }
            }
            steps {
                echo 'TAG_NAME'
            }
        }
    }
}
