# Azure IoT Smart Factory Predictive Maintenance System

## 📌 Overview
This project demonstrates a cloud-based IoT smart factory system built on Microsoft Azure.  
It simulates industrial devices, collects real-time telemetry data, performs anomaly detection, and applies machine learning for predictive maintenance.

The system is designed with a **production-ready architecture** and supports **multi-cloud integration (Azure + AWS)**.

## 🏗️ Architecture
graph TD
    A[IoT Devices Simulator] --> B[Azure IoT Hub]
    B --> C[Stream Analytics]
    C --> D[Azure Functions]
    D --> E[Data Lake / Cosmos DB]
    E --> F[Azure Machine Learning]
    F --> G[Power BI Dashboard]

---

## ⚙️ Tech Stack

### Cloud & Infrastructure
- Azure IoT Hub
- Azure Functions
- Azure Stream Analytics
- Azure Machine Learning
- Azure Data Lake / Cosmos DB
- AWS RDS (Hybrid architecture)

### DevOps & IaC
- Terraform
- GitHub Actions
- Docker / AKS

### Backend
- Python (Flask)

### Monitoring
- Azure Monitor
- Datadog

---

## 📂 Project Structure
industrial-energy-ai-demo/

industrial-energy-ai-demo/
│
├── docs/                         # Documentation
├── infrastructure/              # IaC (Terraform for Azure & AWS)
├── simulator/                   # IoT device simulator
├── ingestion/                   # Azure Functions (data ingestion)
├── processing/                  # Stream processing & anomaly detection
├── ml/                          # Machine learning models
├── api/                         # Backend API (Flask)
├── data/                        # Sample data
├── dashboard/                   # Power BI dashboard
├── tests/                       # Unit tests
└── scripts/                     # Utility scripts


---

## 🔧 Key Components

### 1. Simulator
Simulates IoT devices sending telemetry data (temperature, vibration) to Azure IoT Hub.

### 2. Ingestion
Event-driven data ingestion using Azure Functions.

### 3. Processing
Real-time anomaly detection using rule-based logic and stream processing.

### 4. Machine Learning
Predictive maintenance models for equipment failure prediction.

### 5. API
REST API built with Flask for data access and prediction services.

### 6. Infrastructure
Infrastructure as Code using Terraform for Azure and AWS (multi-cloud architecture).

---

## 🚀 Features

- Real-time IoT data ingestion
- Anomaly detection (threshold-based)
- Predictive maintenance (ML-ready)
- Scalable cloud architecture
- Multi-cloud support (Azure + AWS)
- CI/CD pipeline integration

---

## ▶️ Run Locally

### 1. Install dependencies
```bash
pip install -r requirements.txt

cd api
python app.py

2. Start API server
cd api
python app.py
3. Run simulator
cd simulator
python device_simulator.py
Data Flow
Simulator → API → Anomaly Detection → Response
Future Improvements
Integrate Azure IoT Hub (real device connection)
Add Azure Functions for event-driven processing
Implement ML models (LSTM / anomaly detection)
Build Power BI dashboard
Add Terraform deployment automation
🎯 Use Cases
Smart factory monitoring
Predictive maintenance
Industrial IoT analytics
Energy optimization systems
👨‍💻 Author
Yu Tao (余泰 歌然)
Cloud Engineer | Azure | AWS | IoT | AI

⭐ Notes
This project is designed as a portfolio-level cloud engineering project, demonstrating:

Azure cloud architecture
IoT system design
DevOps & automation
AI integration
