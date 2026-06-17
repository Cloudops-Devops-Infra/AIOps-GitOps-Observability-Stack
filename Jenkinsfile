pipeline {
    agent any

    environment {
        TF_VAR_aws_endpoint = 'http://host.docker.internal:4566'
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/Cloudops-Devops-Infra/jenkins-serverless-react-cicd.git'
            }
        }

        stage('Infrastructure Provisioning') {
            steps {
                echo 'Setting up Terraform binary...'
                sh '''
                    if [ ! -f ./terraform ]; then
                        curl -fsSL -o terraform.zip https://releases.hashicorp.com/terraform/1.9.0/terraform_1.9.0_linux_amd64.zip
                        unzip -o terraform.zip
                        rm terraform.zip
                        chmod +x ./terraform
                    fi
                '''
                sh './terraform init'
                sh './terraform apply -auto-approve'
            }
        }

        stage('Build Website') {
            steps {
                echo 'Installing dependencies...'
                sh 'npm install'
                echo 'Compiling the website...'
                sh 'export NODE_OPTIONS=--openssl-legacy-provider && export PUBLIC_URL=. && npm run build'
            }
        }

        stage('Deploy to Floci S3') {
            steps {
                echo 'Deploying website to local Floci S3 bucket...'
                sh "aws --endpoint-url=http://host.docker.internal:4566 s3 sync build/ s3://jenkins-serverless-react-cicd-bucket-v2 --acl public-read"
            }
        }
    }
}
