# 🚀 Enterprise-Grade GitOps Pipeline: Automated IaC Provisioning & React Deployment

An advanced, self-contained DevOps pipeline that emulates an enterprise cloud deployment workflow completely on a local workstation. This project transitions traditional manual infrastructure deployment into a true **GitOps lifecycle**, utilizing **Jenkins** for orchestration, **HashiCorp Terraform** for Infrastructure as Code (IaC), and **Docker** to encapsulate the continuous integration runner and target cloud environment.

---

## 🏗️ System Architecture

The pipeline automates the journey from an infrastructure/code change in the repository to a live application hosted on an emulated cloud platform, eliminating manual misconfigurations.

```text
[ Developer Commit ] ──> [ GitHub Repository ]
                                │
                                ▼
                       [ Jenkins Automation ]
                                │
        ┌───────────────────────┴───────────────────────┐
        ▼                                               ▼
[ Stage 1: IaC Provisioning ]               [ Stage 2: App Compilation ]
  • Downloads Standalone Terraform            • Downloads isolated Node.js
  • Forces Path-Style Routing                 • Installs dependencies (`npm i`)
  • Provisions Local S3 Bucket (v2)           • Compiles optimized React build
        │                                               │
        └───────────────────────┬───────────────────────┘
                                ▼
                   [ Stage 3: Cloud Delivery ]
                     • Injects dummy AWS payload variables
                     • Syncs binary assets via AWS CLI
                     • Targets Local Cloud Emulator Network
🛠️ The DevOps Tech Stack
CI/CD Orchestration: Jenkins (Declarative Pipeline / Groovy Scripting)

Infrastructure as Code (IaC): HashiCorp Terraform (v1.9.0)

Containerization & Networking: Docker (Isolated networks bridging the host and runners)

Application Framework: React.js (Node.js 18 compilation runtime)

Local Cloud Platform: Floci / LocalStack (Emulating Amazon S3 API structures)

Command Line Interface: AWS CLI (Configured with dynamic virtual key signing)

📂 Repository Layout
Plaintext
.
├── main.tf               # Terraform configuration declaring the S3 infrastructure blueprint
├── Jenkinsfile           # Enterprise declarative multi-stage automation script
└── README.md             # Comprehensive architecture and engineering documentation
💡 Note: The React application source code (package.json, src/) is systematically cloned into a transient sandbox directory (/app) during runtime execution to maintain structural boundary isolation between platform code and application business logic.

⚙️ Automated Pipeline Stages
1. Checkout Code
Dynamically pulls the infrastructure declarative configurations from GitHub and immediately triggers an isolated horizontal clone of the target functional React source directory into a decoupled subfolder.

2. Infrastructure Provisioning (IaC)
Bootstraps a self-contained, user-space Terraform binary within the workspace. Initializes provider subsystems and evaluates configuration state against the environment. It then executes an automated, hands-free provisioning run (terraform apply -auto-approve) to guarantee that the required target cloud architecture exists before application transport begins.

3. Build Website
Deploys a portable Node.js execution runtime directly inside the pipeline. Isolates package structures, processes npm install, injects OpenSSL backward-compatibility flags, and compiles a highly compact, production-optimized compilation artifact ready for edge-network delivery.

4. Deploy to Floci S3
Instantiates the AWS CLI delivery layer, overrides global routing variables to map directly onto the internal Docker container proxy matrix (host.docker.internal), and standardizes cross-directory synchronization, moving the React frontend static layers directly into the provisioned bucket.

🖼️ Pipeline Visual Verification
Jenkins Automation Stage View
Below is the validated proof execution showing the entire declarative orchestration pipeline passing with a clean, consecutive green metrics state:

Live Cloud-Hosted Application
The application running perfectly, hosted directly out of the code-defined, path-routed emulated Amazon S3 bucket instance:

💡 Real-World Engineering Roadblocks Overcome
Building an automated pipeline from scratch exposes classic architectural challenges. Below are the design hurdles resolved during engineering:

🛡️ Challenge 1: Docker Container Loopback Networking Breakdown
The Symptom: Jenkins executing commands inside a container interpreted localhost as its own internal filesystem, rendering it blind to the cloud emulator running on the host machine.

The Resolution: Abstracted network paths by implementing a custom variable layer in the Terraform configuration, routing Jenkins traffic out of the container boundary using the host bridge endpoint (http://host.docker.internal:4566).

🌐 Challenge 2: S3 DNS Hosted-Style Address Routing Failure
The Symptom: By default, the AWS Terraform provider uses Virtual Hosted-Style bucket structures (e.g., http://bucket-name.localhost:4566). The internal container proxy DNS could not resolve these custom ad-hoc subdomains, leading to immediate no such host crashes.

The Resolution: Enforced Path-Style Addressing inside the AWS provider configuration block by setting s3_use_path_style = true. This forced Terraform to communicate over structural URL paths (http://host.docker.internal:4566/bucket-name), bypassing container DNS layout limitations.

🔑 Challenge 3: AWS CLI Credential Initialization Trap
The Symptom: The automated deployment agent threw a terminating error Unable to locate credentials, blocking asset transport despite communicating with a local mock emulator that required no authentication.

The Resolution: Configured a global environment {} block directly within the declarative Jenkinsfile, injecting persistent dummy cryptographic payloads (AWS_ACCESS_KEY_ID = 'mock_access_key'). This satisfied the security validator check inside the AWS CLI utility wrapper without exposing sensitive production keys.

🚀 How to Run Locally
Prerequisites
Docker & Docker Desktop installed and active

Windows PowerShell or Linux Bash terminal shell

Step 1: Spin up the Local Cloud & Automation Environments
Ensure your local containers are provisioned and active:

PowerShell
docker start jenkins
docker start floci
Step 2: Configure the Jenkins Automation Job
Access the Jenkins UI at http://localhost:8080 using your admin keys.

Select New Item -> Create a Pipeline named Website-Deployment-Pipeline.

Scroll to the Pipeline configuration section, change the definition to Pipeline script, and paste the contents of the Jenkinsfile present in this repository.

Hit Save and click Build Now.

Developed by Subash Patra — Associate Cloud Engineer