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
                    "${env.TAG_NAME}" != null
                }
            }
            steps {
                echo "${env.TAG_NAME}"
            }
        }
        stage('Check for Tag') {
            when { tag 'tag-*' }
            steps {
                en.TAG_NAME
            }
        }
    }
}
