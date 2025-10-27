# 🧭 LLM Travel Assistant – End-to-End MLOps Deployment

## 🚀 Overview
The **LLM Travel Assistant** is an intelligent conversational travel guide powered by **Groq LLMs**, capable of generating personalized trip itineraries, travel tips, and destination insights.  
This project demonstrates a complete **MLOps pipeline**, from model inference to deployment and observability.

## 🧠 Features
- **Conversational LLM Integration:** Leveraged **Groq LLM** for ultra-fast natural language inference.
- **Streamlit Frontend:** Interactive UI for dynamic travel assistance and trip planning.
- **Cloud Deployment:** Hosted on **Google Cloud VM** for scalable infrastructure.
- **Containerization & Orchestration:** Built using **Docker**, **Minikube**, and **kubectl** for Kubernetes-based orchestration.
- **Monitoring & Logging:** Integrated **ELK Stack** (**Elasticsearch**, **Logstash**, **Filebeat**, **Kibana**) for centralized log management and visualization.
- **CI/CD Ready:** Modular design supports continuous integration and deployment pipelines.

## ⚙️ Tech Stack
`Groq LLM` · `Streamlit` · `Python` · `Docker` · `Minikube` · `kubectl` · `GCP VM` · `Elasticsearch` · `Filebeat` · `Logstash` · `Kibana`

## 🧩 Architecture
```
User → Streamlit UI → Groq API → Dockerized Service → GCP VM
                                    ↓
                           ELK Stack for Logging
```
- **Filebeat**: Collects logs from application containers.
- **Logstash**: Processes and sends data to Elasticsearch.
- **Elasticsearch**: Stores and indexes logs.
- **Kibana**: Visualizes system metrics and logs.

## ☁️ Deployment
- Deployed on **Google Cloud VM**
- Dockerized microservices for scalability
- Kubernetes used for container orchestration
