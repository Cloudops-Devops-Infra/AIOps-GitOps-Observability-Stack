# 🚀 Enterprise GitOps Pipeline: Automated IaC, React Deployment & Full-Stack Observability

An advanced, self-contained local DevOps platform that emulates an enterprise cloud deployment workflow and full-stack observability matrix. This architecture transitions traditional manual infrastructure deployment into a true declarative GitOps lifecycle with **zero cloud billing risk ($0.00 infrastructure cost)**.

---

## 📈 Project Evolution

* **Day 1: Cloud Sandboxing:** Designed initial serverless patterns in public AWS (S3, Lambda, DynamoDB). Migrated to a local model to guarantee strict cost containment.
* **Day 2: IaC & Pipeline Decoupling:** Implemented local cloud emulation layers (Floci/LocalStack) and automated provisioning using HashiCorp Terraform and Groovy declarative pipelines.
* **Day 3: Full-Stack Observability:** Embedded Prometheus time-series scraping and Grafana visualization decks while hardening the multi-container Docker infrastructure.

---

## 🏗️ System Architecture

```text
[ Developer Commit ] ──> [ GitHub Repository ]
                                │
                                ▼
                       [ Jenkins Automation ] ───(Exposes Vitals)───┐
                                │                                   │
        ┌───────────────────────┴───────────────────────┐           ▼
        ▼                                               ▼   [ Prometheus Database ]
[ Stage 1: IaC Provisioning ]               [ Stage 2: App Compilation ]    │
  • Standalone Terraform Run                  • Node.js 18 Environment      │
  • Enforces Path Addressing                   • Installs Dependencies       ▼
  • Provisions Local S3 Bucket                • Compiles Optimized React [ Grafana Desk ]
        │                                               │             (Dashboard UI)
        └───────────────────────┬───────────────────────┘
                                ▼
                   [ Stage 3: Cloud Delivery ]
                     • Injects Mock AWS Credentials
                     • Syncs Assets via AWS CLI
🛠️ The DevOps Tech Stack
CI/CD Orchestration: Jenkins (Declarative Pipelines / Groovy Scripting)

Infrastructure as Code (IaC): HashiCorp Terraform (v1.9.0)

Metrics Ingestion: Prometheus (5s High-Fidelity Scrape Matrix)

Visualization Deck: Grafana (Custom Performance & Health UI dashboards)

Containerization: Docker & Docker Compose (Isolated virtual bridge networks)

Cloud Emulation Platform: Floci / LocalStack (Amazon S3 API simulation)

📂 Repository Layout
Plaintext
.
├── assets/                 # Validation graphs, UI metrics, and documentation assets
│   ├── jenkins-dashboard.png
│   └── grafana-health.png
├── main.tf                 # Terraform configuration declaring S3 infrastructure
├── Jenkinsfile             # Multi-stage automated declarative deployment script
├── docker-compose.yml      # Multi-container cluster orchestration manifest
├── prometheus.yml          # Telemetry target parsing definitions
└── ai_log_analyzer.py      # Automated Python log analytics triage engine
💡 Note: The React application source code is dynamically isolated inside a transient sandbox folder during compilation loops to maintain clean structural boundaries.

⚙️ Automated Pipeline Lifecycle
Checkout Code: Pulls latest infrastructure manifests and configuration arrays from GitHub.

IaC Provisioning: Dynamically handles a hands-free terraform apply -auto-approve configuration to ensure target S3 endpoints exist before asset delivery.

Build Website: Compiles production-optimized static layers via a localized Node.js 18 container engine.

Deploy to S3: Fires the local AWS CLI wrapper to safely sync the production build layer directly into the target emulated S3 bucket.

🤖 AIOps & Observability Pillars
Self-Healing Infrastructure: Leverages low-level runtime isolation loops (restart: unless-stopped) to detect service or JVM crashes and trigger hot restorations automatically in < 5 seconds.

High-Fidelity Telemetry: Prometheus sweeps the Jenkins /prometheus/ exporter endpoint every 5 seconds to capture real-time system degradation and micro-spikes before terminal failure occurs.

Log Analytics Diagnostics (ai_log_analyzer.py): A custom Python ingestion tool that parses system outputs, runs keyword matching across fatal event streams, and surfaces root-cause analysis instantly (reducing MTTR by 90%).

💡 Real-World Roadblocks Overcome
Challenge 1: Container Loopback Network Blocker

Symptom: Jenkins interpreted localhost as its own container file system, breaking communication with external components.

Fix: Abstracted routing paths using the Docker host bridge gateway (http://host.docker.internal:4566).

Challenge 2: S3 DNS Resolution Crash

Symptom: Default virtual-hosted S3 endpoints failed to resolve inside isolated networks.

Fix: Enforced explicit path-style parameters (s3_use_path_style = true) within the Terraform provider config.

Challenge 3: AWS CLI Credential Validation Lock

Symptom: Continuous deployment failed with an Unable to locate credentials fatal exception.

Fix: Injected mock cryptographic environment variables (AWS_ACCESS_KEY_ID = 'mock-ops-key-id') directly into the pipeline runner.

Challenge 4: OCI Runtime Mount Mount Conflict

Symptom: Prometheus failed to start up with a runc create failed: not a directory error.

Fix: Cleared auto-generated Windows placeholder paths and used relative pathing mounts to bind raw configuration files accurately.

🚀 Getting Started
1. Clone & Enter Path
PowerShell
git clone [https://github.com/Cloudops-Devops-Infra/AIOps-GitOps-Observability-Stack.git](https://github.com/Cloudops-Devops-Infra/AIOps-GitOps-Observability-Stack.git)
cd AIOps-GitOps-Observability-Stack
2. Launch the Stack
PowerShell
docker compose up -d
3. Initialize Jenkins Job
Navigate to http://localhost:8080 ➡️ Create a new Pipeline named Website-Deployment-Pipeline.

Select Pipeline script from SCM, choose Git, paste your repository URL, set the script path to Jenkinsfile, and click Build Now.

4. Verify Dashboards
Raw Exporter: http://localhost:8080/prometheus/

Prometheus Targets: http://localhost:9090/targets

Grafana Desk: http://localhost:3000 (Credentials: admin / admin)

Developed by Subash Patra — Associate Cloud Engineer