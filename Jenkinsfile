pipeline {
     agent { docker { image 'python:3.7.2' } }
     stages {
         stage('build') {
             steps {
                    withEnv(["HOME=${env.WORKSPACE}"]) {
                         sh 'python3 -m pip install flask'
                         sh 'python3 -m pip install boto3'
                         sh 'python3 -m pip install requests'

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