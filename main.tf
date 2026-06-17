variable "aws_endpoint" {
  type    = string
  default = "http://localhost:4566"
}

terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region                      = "us-east-1"
  access_key                  = "mock_access_key"
  secret_key                  = "mock_secret_key"
  skip_credentials_validation = true
  skip_metadata_api_check     = true
  skip_requesting_account_id  = true

  endpoints {
    s3 = var.aws_endpoint
  }
}

resource "aws_s3_bucket" "calc_bucket" {
  bucket        = "jenkins-serverless-react-cicd-bucket"
  force_destroy = true
}

resource "aws_s3_bucket_website_configuration" "calc_site" {
  bucket = aws_s3_bucket.calc_bucket.id

  index_document {
    suffix = "index.html"
  }
}
