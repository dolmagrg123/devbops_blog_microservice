pipeline {
     agent { any { image 'python:3.7.2' } }
     environment {
        AWS_DEFAULT_REGION = 'us-east-1'
     }
     stages {
         stage('build') {
             steps {
                    gitStatusWrapper(credentialsId: 'cb319b457f92346f3dd7f29984d4c9fa9bf084e4', gitHubContext: 'Status', description: 'Validating') {
                        withEnv(["HOME=${env.WORKSPACE}"]) {
                                 sh 'pip install flask --user'
                                 sh 'pip install boto3 --user'
                                 sh 'pip install requests --user'
                             }
                    }

                 }
         }
         stage('test') {
             steps {
                 withEnv(["HOME=${env.WORKSPACE}"]) {
                    sh 'python3 test.py'
                 }
             }
         }
     }
     }
