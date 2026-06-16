# Automated React CI/CD Deployment Pipeline via Jenkins & Floci

An automated, local DevOps CI/CD pipeline built from scratch. This pipeline orchestrates the entire lifecycle of a modern React web application—from source control checkout to local serverless cloud deployment—using an isolated, containerized environment.

## 🚀 Architecture & Tech Stack
* **CI/CD Automation:** Jenkins (Declarative Pipeline / Groovy Scripting)
* **Containerization:** Docker (Isolated Jenkins & Local Cloud networks)
* **Build Environment:** Node.js 18 / npm
* **Local Cloud Platform:** Floci / LocalStack (S3 Service Emulator)
* **Deployment Tooling:** AWS CLI

## 🛠️ Pipeline Stages
1. **Checkout Code:** Automatically pulls the latest source code from a remote GitHub repository.
2. **Build Website:** Provisions Node.js 18, installs 1,400+ dependencies, and compiles highly optimized production static assets (`html`, `js`, `css`).
3. **Archive Artifact:** Safely caches and versions the compiled build artifacts inside the Jenkins server.
4. **Deploy to Floci S3:** Interacts with the local cloud environment via the AWS CLI to sync and host the production build in an S3 bucket emulator.

## 💡 Key Roadblocks Overcome & Lessons Learned
* **Docker Shared Libraries:** Fixed missing underlying Linux library errors (`libatomic.so.1`) inside minimal, bare-bones Docker containers using root execution.
* **Modern Node.js Encryption Clashes:** Bypassed Webpack/OpenSSL 3.0 crypto compatibility issues (`ERR_OSSL_EVP_UNSUPPORTED`) using legacy provider flags without degrading Node versions.
* **Relative Path Routing:** Overrode hardcoded asset routing by manipulating the `PUBLIC_URL` environment variables during compilation to prevent blank-screen rendering in S3.
* **Container Networking & Port Allocation:** Resolved port assignment traffic jams (`0.0.0.0:4566 allocated`) to successfully establish seamless, secure routing between Docker containers.

## 🔮 Future Roadmap
* **Full-Stack Serverless Integration:** Expand the pipeline to deploy a serverless backend incorporating **AWS Lambda, API Gateway, and DynamoDB** within the local Floci environment.
* **Infrastructure as Code (IaC):** Integrate Terraform or AWS SAM templates to fully automate the provisioning of the local cloud infrastructure.

## 📊 Proof of Work

### Automated Jenkins Pipeline Success
![Jenkins Pipeline](./jenkins-pipeline.png)

### Live Application Hosted via Local S3 Bucket Emulator
![Live Application](./live-app.png)
