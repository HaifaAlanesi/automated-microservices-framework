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
