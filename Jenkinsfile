pipeline {
    agent any

    environment {
        // Point Terraform to the Windows host emulator network
        TF_VAR_aws_endpoint = 'http://host.docker.internal:4566'
    }

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Infrastructure Provisioning') {
            agent {
                docker { image 'hashicorp/terraform:latest' }
            }
            steps {
                sh 'terraform init'
                sh 'terraform apply -auto-approve'
            }
        }

        stage('Build Website') {
            agent {
                docker { image 'node:18-alpine' }
            }
            steps {
                sh 'npm install'
                sh 'unset CI && npm run build'
            }
        }

        stage('Deploy to Floci S3') {
            agent {
                docker { image 'amazon/aws-cli:latest' }
            }
            steps {
                sh "aws --endpoint-url=http://host.docker.internal:4566 s3 sync build/ s3://jenkins-serverless-react-cicd-bucket --acl public-read"
            }
        }
    }
}
