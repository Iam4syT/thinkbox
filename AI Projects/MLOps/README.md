# MLOps Pipeline & Model Lifecycle Engine

[![Python](https://img.shields.io/badge/Language-Python%203.9+-3776AB?style=flat-square&logo=python)](https://www.python.org/)
[![ZenML](https://img.shields.io/badge/Orchestrator-ZenML-4B0082?style=flat-square)](https://zenml.io/)
[![MLflow](https://img.shields.io/badge/Tracking-MLflow-0194E2?style=flat-square&logo=mlflow)](https://mlflow.org/)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](#)

> **Automated end-to-end Machine Learning pipeline for dataset validation, experiment tracking, model registry, CI/CD deployment, and continuous drift monitoring.**

---

## 1. Project Overview

The **MLOps Engine** provides a scalable infrastructure for managing machine learning models from raw data ingestion to production serving and monitoring.

### Key Capabilities
- **Automated Data Ingestion & Validation**: Ingestion pipelines with data cleaning and schema validation.
- **Experiment Tracking**: Track model metrics, hyperparameters, and artifacts via MLflow & ZenML.
- **CI/CD & Model Deployment**: Continuous integration and deployment of trained models.
- **Drift Monitoring**: Real-time evaluation of data drift and model degradation.

---

## 2. Directory Structure

```
MLOps/
├── mlops-project/
│   ├── customer-satisfaction-mlops-main/  # ZenML & MLflow end-to-end customer satisfaction pipeline
│   ├── .env.example                       # Environment secrets template
│   ├── .gitignore                         # Python & ZenML ignore rules
│   └── README.md                          # Detailed pipeline documentation
└── README.md                              # Primary project overview
```

---

## 3. Quickstart & Execution

1. **Navigate to the pipeline directory:**
   ```bash
   cd "/Users/4syt/Documents/thinkbox/AI Projects/MLOps/mlops-project"
   ```

2. **Explore Detailed Subproject Documentation:**
   See [`mlops-project/README.md`](./mlops-project/README.md) for full installation and execution steps.

---

## 4. License

Distributed under the **MIT License**. Part of the Thinkbox AI Projects series.
