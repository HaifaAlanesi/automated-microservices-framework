## 🚀 Technical Architecture Overview

![Microservices Framework Architecture Diagram](image_14<img width="1376" height="768" alt="Automated-microservice-framework" src="https://github.com/user-attachments/assets/9a230c59-f0a1-4a7f-8517-4469cf61b3c9" />
.png)

This diagram provides a comprehensive view of the automated microservices framework developed for this project. The architecture is designed to demonstrate full-stack DevOps principles, with a specific focus on automated orchestration, secure edge networking, and stateful service management.

### Key Architectural Concepts Proven:

* **Secure Edge Networking:** Traffic flows from the **Public Internet** through the **Cloudflare Global Edge**, utilizing an egress-only **Argo Tunnel** (the black line in the diagram) directly to the `cloudflared` ingress in the **Edge & Orchestration Subnet**. This establishes a Zero Trust security posture by hiding the origin IP.
* **Automated Scaling:** A **Horizontal Pod Autoscaler (HPA)** hex-icon is visible, receiving metric data (dotted line) from the cluster's **Metrics Server**. It dynamically scales the **flask-microservice (pod)** deployment (light blue boxes) in the **Application Subnet** based on load.
* **Persistent & Encrypted State:** The Flask deployment interacts with the **Redis Database Tier** via standard Kubernetes services. Data persistence is managed by a **Redis Cluster StatefulSet**, which stores data on a **Persistent Volume**. Crucially, this tier demonstrates **Data Encryption at Rest** and **Managed Backups**, satisfying production security requirements.
* **Single-Node K3s Cluster:** The entire environment is contained within a single **Ubuntu VM**, which acts as both the control plane and worker node, showcasing efficient, single-node orchestration.





## 🌐 Architecture & Traffic Flow
1. **User Request:** A user visits `https://haifa.work`.
2. **Global Edge:** Cloudflare receives the request and handles SSL/TLS termination.
3. **Secure Tunnel:** Traffic is routed through an egress-only **Argo Tunnel** (cloudflared).
4. **Service Discovery:** The tunnel communicates with the Kubernetes **ClusterIP Service** using internal DNS.
5. **Load Balancing:** K3s distributes the request to one of the healthy Flask pods.
6. **Persistence:** The Flask app interacts with a **Redis** instance to track global vote counts.

   
