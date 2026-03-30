
# ☁️ # Automated Microservices Framework with GitOps & Cloudflare
A highly secure, automated, and scalable microservices infrastructure that securely bridges a local cluster with the public internet. This project demonstrates modern cloud-native practices, Infrastructure as Code (IaC), and secure edge networking without exposing local home network ports.

### *Automated Infrastructure as Code (IaC) with Terraform* 

---
---
**Developed by Haifa Alanesi**

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




---

## 🏗️ Architecture Overview

The infrastructure is logically segmented into three distinct subnets within a simulated Virtual Private Cloud (VPC) environment to mirror a production-grade cloud setup.

### 1. Edge & Orchestration Subnet (`10.0.1.0/24`)
* **Host OS:** Ubuntu 
* **Orchestration:** K3s (Lightweight Kubernetes)
* **Ingress & Security:** Cloudflare Argo Tunnel (`cloudflared`) creates a secure outbound-only connection to the Cloudflare Global Edge. This allows traffic to securely reach the cluster without opening inbound firewall ports.
* **Monitoring:** Kubernetes Metrics Server to track cluster resource usage.

### 2. Application Subnet (`10.0.2.0/24`)
* **Host OS:** Ubuntu VM
* **Web Tier:** Containerized Python Flask microservices controlled via a Kubernetes `Deployment`.
* **Dynamic Scaling:** A Horizontal Pod Autoscaler (HPA) that automatically scales pods up and down based on real-time resource metrics.
* **Internal Routing:** A Kubernetes `ClusterIP` service mapping to port `5000` for seamless internal load balancing.

### 3. Stateful Services Subnet (`10.0.3.0/24`)
* **Database Tier:** A highly available Redis Cluster deployed as a Kubernetes `StatefulSet`.
* **Data Persistence:** Backed by Kubernetes Persistent Volumes to prevent data loss during pod restarts.
* **Security:** Strict data encryption at rest with automated managed backups.

---

## 🛠️ Technology Stack

| Layer | Technologies Used |
| :--- | :--- |
| **Compute** | Ubuntu Virtual Machines |
| **Container Orchestration** | K3s (Kubernetes) |
| **Edge Networking** | Cloudflare Global Edge, Argo Tunnel (`cloudflared`) |
| **Microservices** | Python Flask |
| **Database & Cache** | Redis (StatefulSet) |
| **Auto-scaling** | Kubernetes Metrics Server, Horizontal Pod Autoscaler (HPA) |

---

## 🚀 Key Features

* **Zero-Trust Network Access:** Cloudflare Argo Tunnel ensures the local environment remains completely invisible to public internet scans.
* **Automated Scaling:** The Flask web tier actively responds to traffic spikes automatically.
* **High Availability:** Redis data persistence is managed via native Kubernetes volume claims.
* **Network Segmentation:** Strict isolation between the public edge, the application logic, and the backend data store.

---
## 📬 Contact & Connect

If you have any questions about this architecture or want to discuss DevOps and Cloud Engineering, feel free to reach out!

* **LinkedIn:** [linkedin.com/in/haifa-alanesi](https://www.linkedin.com/in/haifa-alanesi-73a35329b)
* **GitHub:** [github.com/HaifaAlanesi](https://github.com/HaifaAlanesi)



