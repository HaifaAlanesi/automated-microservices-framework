## 🌐 Architecture & Traffic Flow
1. **User Request:** A user visits `https://haifa.work`.
2. **Global Edge:** Cloudflare receives the request and handles SSL/TLS termination.
3. **Secure Tunnel:** Traffic is routed through an egress-only **Argo Tunnel** (cloudflared).
4. **Service Discovery:** The tunnel communicates with the Kubernetes **ClusterIP Service** using internal DNS.
5. **Load Balancing:** K3s distributes the request to one of the healthy Flask pods.
6. **Persistence:** The Flask app interacts with a **Redis** instance to track global vote counts.

   
## Real-world HPA Scaling Test Results:
NAME               REFERENCE                     TARGETS    REPLICAS
flask-deployment   Deployment/flask-deployment   97%/50%    5
flask-deployment   Deployment/flask-deployment   51%/50%    5
