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
        stage('Check for Tag 1') {
            when { tag 'tag-*' }
            steps {
                echo env.TAG_NAME
            }
        }
    }
}

def addTagNameCheck() {
    addPhase(name:'Check Tag Name 3', priority:900)

    /* groovylint-disable-next-line SpaceAfterClosingBrace */
    if (env.TAG_NAME != null) {
        echo "Tag Name: ${TAG_NAME}"
    }
}

addTagNameCheck()
