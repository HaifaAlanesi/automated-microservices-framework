🚀 Technical Architecture Overview
<img width="1376" height="768" alt="Haifamix-AWS-Multi-Tier-Architecture" src="[PASTE_LINK_TO_YOUR_IMAGE_HERE]" />

The architecture is designed to demonstrate full-stack DevOps principles using Infrastructure as Code (Terraform).
🌐 Architecture & Traffic Flow
User Request: A user visits your custom domain (e.g., haifamix.work).

Global Edge: AWS CloudFront receives the request, providing low-latency delivery and SSL/TLS termination at the edge.

Load Balancing: Traffic is routed to a Primary Application Load Balancer (ALB), which checks the health of the target groups.

Secure Compute: The ALB distributes traffic to healthy EC2 instances hosted within isolated Private Subnets across multiple Availability Zones.

VPC Peering: Secure, private communication is established between the Primary VPC and a dedicated RDS VPC.

Persistence: The application interacts with a highly available Amazon RDS instance for secure data management.

🛠️ Key Features
Infrastructure as Code: 100% of the environment (VPCs, Subnets, EC2, RDS) is provisioned and managed using Terraform.

High Availability: Architecture spans multiple zones with automated failover for both compute (ALB/EC2) and database (Multi-AZ RDS) tiers.

Security Isolation: All sensitive workloads are placed in non-public subnets, accessible only through defined internal peering and load balancers.

Verification: Deployment is validated with a successful curl -I test returning HTTP/1.1 200 OK.


Developed by Haifa Alanesi  | LinkedIn



 
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

