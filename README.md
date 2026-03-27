
# ☁️ High-Availability Multi-Tier AWS Architecture
### *Automated Infrastructure as Code (IaC) with Terraform* 


## 🚀 Technical Architecture Overview

<img width="1376" height="768" alt="Automated-microservice-framework" src="https://github.com/user-attachments/assets/5c623edb-1fd8-4441-a0c5-304ec6c22e31" />

### The architecture is designed to demonstrate full-stack DevOps principles.

## 🌐 Architecture & Traffic Flow
1. **User Request:** A user visits `https://haifa.work`.
2. **Global Edge:** Cloudflare receives the request and handles SSL/TLS termination.
3. **Secure Tunnel:** Traffic is routed through an egress-only **Argo Tunnel** (cloudflared).
4. **Service Discovery:** The tunnel communicates with the Kubernetes **ClusterIP Service** using internal DNS.
5. **Load Balancing:** K3s distributes the request to one of the healthy Flask pods.
6. **Persistence:** The Flask app interacts with a **Redis** instance to track global vote counts.

   ---

## 🛠️ Key Features

* **Infrastructure as Code:** 100% of the environment (VPCs, Subnets, EC2, RDS) is provisioned and managed using **Terraform**.
* **High Availability:** Architecture spans multiple zones with automated failover for both compute (ALB/EC2) and database (Multi-AZ RDS) tiers.
* **Security Isolation:** All sensitive workloads are placed in non-public subnets, accessible only through defined internal peering and load balancers.
* **Database Expertise:** Leveraging a professional **DBA background** to implement encrypted, high-performance RDS configurations.
* **Verification:** Deployment is validated with a successful `curl -I` test returning `HTTP/1.1 200 OK`.

---

## 📂 Project Structure
```bash
├── terraform/
│   ├── main.tf          # Provider and Backend configuration
│   ├── vpc.tf           # Network isolation and Peering logic
│   ├── rds.tf           # Secure Database tier setup
│   ├── variables.tf     # Environment variables
│   └── outputs.tf       # Infrastructure endpoints
└── README.md

**Developed by Haifa Alanesi**


