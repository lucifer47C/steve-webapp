#  AI Model Deployment with Docker & Kubernetes

##  Build Docker Image

```bash
docker build -t <username>/ai-model .
```

Replace `<username>` with your Docker Hub username.

---

##  Push to Docker Hub

```bash
docker push <username>/ai-model
```

Make sure you're logged in to Docker Hub:

```bash
docker login
```

---

##  Apply Kubernetes Configuration

```bash
kubectl apply -f model-deployment.yaml
kubectl apply -f model-service.yaml
```

These files define the deployment and service for your AI model in Kubernetes.

---

##  Get External IP

```bash
kubectl get svc ai-model-service
```

Look for the `EXTERNAL-IP` in the output. Use it to access the model’s API endpoint:

```
http://<EXTERNAL-IP>:<PORT>
```



