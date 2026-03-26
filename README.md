 HEAD
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

📈 Performance & Auto-scaling Validation
To test the resilience of the framework, I performed a synthetic load test using a wget loop to simulate high traffic. The Horizontal Pod Autoscaler (HPA) was configured with a target of 50% CPU utilization.

Observed Scaling Event:

Plaintext
NAME               REFERENCE                     TARGETS    MINPODS   MAXPODS   REPLICAS   AGE
flask-deployment   Deployment/flask-deployment   0%/50%     1         5         1          15m
flask-deployment   Deployment/flask-deployment   97%/50%    1         5         4          18m
flask-deployment   Deployment/flask-deployment   110%/50%   1         5         5          20m
flask-deployment   Deployment/flask-deployment   45%/50%    1         5         5          25m
Key Takeaways:

Dynamic Response: The cluster successfully detected the CPU spike and triggered a scale-out from 1 to 5 replicas within 3 minutes.

Stability: Once the load test concluded, the HPA maintained the replicas until the cooldown period was met, ensuring no "flapping" occurred.

Load Balancing: Verified that the ClusterIP Service distributed the incoming tunnel traffic evenly across the newly provisioned pods.
81ce2f6 (docs: add HPA load test results and performance validation)
