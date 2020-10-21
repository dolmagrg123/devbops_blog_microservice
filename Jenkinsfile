pipeline {
     agent { docker { image 'python:3.7.2' } }
     stages {
         stage('build') {
             steps {
                    withEnv(["HOME=${env.WORKSPACE}"]) {
                         sh 'pip install flask'
                         sh 'pip install boto3'
                         sh 'pip install requests'

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