## E2E-ML-Pipeline-MLOps-MLFlow

This is an End to End ML project right from Data Ingestion and Deployment.
This project predicts Wine Quality, but has more emphasis on How the project is developed, How is the data ingested, data transformationdone, model trained, ML-Ops, ML-Flow and deployment via GitHub Actions.

For AWS - GitHub Deployment below services were used :
IAM -
   AM (Identity and Access Management) is an AWS security service that lets you securely control access to AWS resources.
   To create a new user
ECR - 
   Amazon Elastic Container Registry (ECR) is AWS’s Docker image repository service. It’s like Docker Hub, but hosted inside AWS, private and tightly integrated with IAM + ECS + EKS.
   To create an ECR rergistry
EC2 - 
   Amazon EC2 (Elastic Compute Cloud) is AWS’s virtual server service.
   To create instance
Github Actions -
   GitHub’s built-in automation system. It lets you run workflows (scripts) automatically when something happens in your repo — like pushing code, creating a pull request, or even on a schedule.
   To facilitate CI-CD

## Project Structure
```
E2E-ML-Pipeline-MLOps-MLFlow
├─ app.py
├─ config
│  └─ config.yaml
├─ Dockerfile
├─ dvc.yaml
├─ LICENSE
├─ main.py
├─ params.yaml
├─ ProjectSteps.md
├─ README.md
├─ requirements.txt
├─ research
│  └─ trials.ipynb
├─ schema.yaml
├─ setup.py
├─ src
│  └─ ML_MLOps_MLFlow_Pipeline
│     ├─ components
│     │  └─ __init__.py
│     ├─ config
│     │  ├─ configuration.py
│     │  └─ __init__.py
│     ├─ constants
│     │  └─ __init__.py
│     ├─ entity
│     │  ├─ config_entity.py
│     │  └─ __init__.py
│     ├─ pipeline
│     │  └─ __init__.py
│     ├─ utils
│     │  ├─ common.py
│     │  └─ __init__.py
│     └─ __init__.py
├─ template.py
└─ templates
   └─ index.html

```

## 📡 Tech stack learned and implemented
- Pandas
- Numpy
- Matplotlib
- Seaborn
- Scikit-learn
- ElasticNet model
- Modular Project Structure
- ML Experiments : DagsHub
- Integration : Project + GitHub + DagsHub + AWS + GitHub Actions + MLOps

## Project endpoints
   `http://3.26.182.93:8080/`

## Key Observations

ElasticNet - is Elastic Net is a linear regression model with regularization, combining:
      L1 (Lasso) → encourages sparsity (some coefficients become exactly 0).
      L2 (Ridge) → shrinks coefficients but keeps all of them non-zero.

Parameters tuned - alpha and l1_ratio

Model Observations  -
      alpha = 0 → No regularization → behaves like standard linear regression.
      alpha ↑ (increase) → stronger regularization:
         Coefficients shrink more toward 0.
         High alpha can lead to underfitting.
      l1_ratio = 0 → Pure Ridge (L2)
         All coefficients shrink but none become exactly zero.
      l1_ratio = 1 → Pure Lasso (L1)
         Encourages sparsity → some coefficients exactly zero.

## Screenshot 
![App Preview](images/quality.png)
![CI/CD Pipeline](images/cicd.png)


